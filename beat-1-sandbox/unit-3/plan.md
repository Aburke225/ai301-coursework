# Plan, issue #5: end-to-end ingestion test with a sample resume fixture

## What is missing

Nothing is broken. A path is untested. `IngestionPipeline.ingest_resume` carries a document
through parse, metadata, chunk, embed, store, and no test exercises any of it end to end.

My reproduction comment shows this four ways. `pytest tests/integration -q` reports `no tests
ran`. `tests/integration/` holds only `__init__.py`. `grep -rl "IngestionPipeline\|ingest_resume"
tests/` returns nothing. And `tests/fixtures/sample_resumes/` doesn't exist.

**The issue's premise needs one correction, and this plan is built on the corrected version.**
The issue says to write the test "using the fixtures in `tests/fixtures/sample_resumes/`". That
directory isn't in the repo, so the fixture is part of this change rather than an input to it.

I raised it in the thread and offered the alternative, since `tests/conftest.py` already provides
a `sample_resume_text` fixture as an inline string. I said I'd default to creating the directory
the issue names unless told otherwise, because "from file upload through embedding storage" reads
as though the file on disk is part of what's under test.

**Why this needs no live services.** `IngestionPipeline.__init__` takes `vector_db`, `db_session`,
and `embedding_provider` as constructor arguments, and the repo already ships
`MockEmbeddingProvider` in `ingestion/embeddings/provider.py`. Doubles at those two seams leave
production code running everywhere in between.

## Scope

**In scope**

- `tests/fixtures/sample_resumes/jane_doe.md`, a markdown resume fixture covering the section
  headers `ResumeParser` recognises.
- `tests/fixtures/sample_resumes/README.md`, one short file saying what the fixtures are and that
  they contain no real personal data.
- `tests/integration/test_ingestion_pipeline.py`, the end-to-end test, with in-memory doubles for
  the vector database and the database session.

**Not in scope**

- The PDF branch of `ResumeParser`. It needs a binary fixture and a decision about whether that's
  generated or committed, and the issue asks for "a sample resume fixture", singular. Deferred on
  purpose; noted under Unknowns.
- `ingest_readme` and `ingest_repo_metadata`. Same pipeline, different entry points, not what the
  issue asks for. A second issue if anyone wants them.
- Anything under `ingestion/`. This issue adds coverage; it doesn't change behaviour. If the test
  finds a bug, that's a separate issue and a separate PR.
- The `integration` marker's definition in `pyproject.toml`, which reads "require Docker
  services". My test uses the marker and needs no Docker. I'm raising that rather than editing
  it. Changing a shared marker's meaning is a maintainer's call.

## Files

- `tests/fixtures/sample_resumes/jane_doe.md` (new)
- `tests/fixtures/sample_resumes/README.md` (new)
- `tests/integration/test_ingestion_pipeline.py` (new)

## Approach

1. Create `tests/fixtures/sample_resumes/jane_doe.md`: a synthetic markdown resume with summary,
   experience, education, skills, and projects sections, long enough to chunk into more than one
   piece.
2. Write `RecordingVectorDB` in the test module. It needs the single `add(ids, embeddings,
   metadatas, documents)` method `BatchEmbeddingProcessor._store_embedding` calls, appending each
   record to a list.
3. Write `NoMatchSession`, a session double whose `query().filter_by().first()` returns `None`, so
   `_check_skip` takes the not-yet-ingested path.
4. Build the pipeline from those two plus `MockEmbeddingProvider`, then assert across the whole
   path. The result reports chunks and doesn't skip. The number stored equals the number reported.
   Each stored vector has `MockEmbeddingProvider.EMBEDDING_DIM` floats. Metadata set at the top of
   the pipeline survives to storage. The stored document text is the chunk text. Embedding ids are
   unique. And the content-derived `source_id` is stable for identical content while differing
   across profiles.
5. Mark the module `@pytest.mark.integration`, matching the marker registered in `pyproject.toml`.

## Test plan

The reproduction's own commands, re-run with the opposite expected result:

```bash
pytest tests/integration -q
# before: "no tests ran in 0.00s"
# expected after: 9 passed

ls tests/fixtures/sample_resumes/
# before: "No such file or directory"
# expected after: README.md  jane_doe.md

grep -rl "IngestionPipeline\|ingest_resume" tests/
# before: no output
# expected after: tests/integration/test_ingestion_pipeline.py
```

Plus a regression check, since this shouldn't disturb anything:

```bash
pytest tests/unit -q
# expected after: unchanged from before the change
```

## Risks and unknowns

- **The doubles could drift from the real collaborators.** `RecordingVectorDB` implements the
  `add(...)` signature `BatchEmbeddingProcessor` calls today. If ChromaDB's interface or the
  processor's call changes, the test keeps passing against a shape nothing uses. Accepted. The
  alternative is a live ChromaDB, which is possibly what the issue's "integration" framing meant
  and which I'm deliberately not doing.
- **`_check_skip` swallows exceptions.** It wraps its query in try/except and logs a warning on
  failure, so a session double that raised would still take the not-skipped path and the test
  would pass for the wrong reason. `NoMatchSession` returns `None` properly instead of raising,
  but the test doesn't currently prove the skip branch works. Deferred and named.
- **The PDF path is untested by this change.** Stated above under Not in scope.
- **The `integration` marker's stated meaning.** Raised in the thread; not resolved by me.
- **Interpreter.** I ran Python 3.11.16, matching `requires-python = ">=3.11"`.

## If the build deviates from this plan

Any divergence gets recorded in the Deviations section below, with what changed and why. Where the
deviation changes what I promised in the thread, I update the thread too.

## Deviations

Nothing changed; the plan held. The three files under Files are the three files the change
contains, no file under `ingestion/` was touched, and the test count came out at 9, which is what
the assertion list in step 4 adds up to.

The one thing I confirmed during the build rather than before it: `tests/conftest.py`'s existing
fixtures didn't need modifying. The new module defines its own fixtures locally, so the shared
conftest is untouched and no other test's environment changes.
