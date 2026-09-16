"""End-to-end ingestion tests: file on disk through to embedding storage.

These exercise the whole `IngestionPipeline.ingest_resume` path — parse, chunk, embed,
store — against a real fixture file. The two external dependencies are replaced with
in-memory doubles rather than live services:

* the vector database, by `RecordingVectorDB` below, which captures exactly what the
  batch processor would have written to ChromaDB;
* the embedding provider, by the repository's own `MockEmbeddingProvider`, which returns
  deterministic vectors so the assertions do not depend on a network call.

Everything between those two seams is production code.
"""

from pathlib import Path

import pytest

from ingestion.embeddings.provider import MockEmbeddingProvider
from ingestion.pipeline import IngestionPipeline

FIXTURE_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "sample_resumes"


class RecordingVectorDB:
    """Stands in for a ChromaDB collection, recording every add() call."""

    def __init__(self):
        self.records = []

    def add(self, ids, embeddings, metadatas, documents):
        for id_, embedding, metadata, document in zip(ids, embeddings, metadatas, documents):
            self.records.append(
                {
                    "id": id_,
                    "embedding": embedding,
                    "metadata": metadata,
                    "document": document,
                }
            )


class NoMatchSession:
    """Stands in for a DB session in which no source has been ingested before."""

    def query(self, *args, **kwargs):
        return self

    def filter_by(self, *args, **kwargs):
        return self

    def first(self):
        return None


@pytest.fixture
def vector_db():
    return RecordingVectorDB()


@pytest.fixture
def pipeline(vector_db):
    return IngestionPipeline(
        vector_db=vector_db,
        db_session=NoMatchSession(),
        embedding_provider=MockEmbeddingProvider(),
    )


@pytest.fixture
def resume_file() -> Path:
    return FIXTURE_DIR / "jane_doe.md"


@pytest.mark.integration
class TestResumeIngestionEndToEnd:
    """One resume, read from disk, carried all the way to stored embeddings."""

    def test_fixture_is_present(self, resume_file):
        """The fixture the rest of this module depends on exists and is non-empty."""
        assert resume_file.is_file()
        assert resume_file.read_text(encoding="utf-8").strip()

    def test_ingest_resume_reports_chunks_and_does_not_skip(self, pipeline, resume_file):
        """A first ingestion parses, chunks, and reports a real chunk count."""
        result = pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        assert result.skipped is False
        assert result.skip_reason is None
        assert result.chunk_count > 0
        assert result.source_id.startswith("resume_profile-123_")

    def test_every_chunk_reaches_the_vector_db(self, pipeline, vector_db, resume_file):
        """The count the pipeline reports is the count actually stored."""
        result = pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        assert len(vector_db.records) == result.chunk_count

    def test_stored_embeddings_have_the_provider_dimension(
        self, pipeline, vector_db, resume_file
    ):
        """What lands in the vector DB is a real vector of the expected width."""
        pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        assert vector_db.records
        for record in vector_db.records:
            assert len(record["embedding"]) == MockEmbeddingProvider.EMBEDDING_DIM
            assert all(isinstance(value, float) for value in record["embedding"])

    def test_stored_metadata_carries_the_ingestion_context(
        self, pipeline, vector_db, resume_file
    ):
        """Metadata set at the top of the pipeline survives to storage."""
        result = pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        for record in vector_db.records:
            assert record["metadata"]["source_type"] == "resume"
            assert record["metadata"]["profile_id"] == "profile-123"
            assert record["metadata"]["filename"] == resume_file.name
            assert record["metadata"]["source_id"] == result.source_id

    def test_stored_documents_are_the_chunk_text(self, pipeline, vector_db, resume_file):
        """The document stored beside each embedding is the text that was embedded."""
        pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        for record in vector_db.records:
            assert isinstance(record["document"], str)
            assert record["document"].strip()

        combined = " ".join(record["document"] for record in vector_db.records)
        assert "Jane Doe" in combined

    def test_embedding_ids_are_unique(self, pipeline, vector_db, resume_file):
        """Each stored chunk gets its own id, so nothing overwrites anything."""
        pipeline.ingest_resume(
            profile_id="profile-123",
            content=resume_file.read_text(encoding="utf-8"),
            filename=resume_file.name,
        )

        ids = [record["id"] for record in vector_db.records]
        assert len(ids) == len(set(ids))

    def test_source_id_is_stable_for_identical_content(self, pipeline, resume_file):
        """The dedup hash is content-derived, so the same file yields the same source_id."""
        text = resume_file.read_text(encoding="utf-8")

        first = pipeline.ingest_resume(
            profile_id="profile-123", content=text, filename=resume_file.name
        )
        second = pipeline.ingest_resume(
            profile_id="profile-123", content=text, filename=resume_file.name
        )

        assert first.source_id == second.source_id

    def test_different_profiles_get_different_source_ids(self, pipeline, resume_file):
        """The same resume ingested for two profiles does not collide."""
        text = resume_file.read_text(encoding="utf-8")

        one = pipeline.ingest_resume(
            profile_id="profile-123", content=text, filename=resume_file.name
        )
        two = pipeline.ingest_resume(
            profile_id="profile-456", content=text, filename=resume_file.name
        )

        assert one.source_id != two.source_id
