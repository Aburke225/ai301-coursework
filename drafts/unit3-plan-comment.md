Following up on the reproduction with the plan I intend to build.

**What's missing.** Nothing is broken. `IngestionPipeline.ingest_resume` carries a document
through parse, chunk, embed, store, and no test touches any of it. The four searches in my
previous comment show that.

**Built on the corrected premise.** As flagged above, `tests/fixtures/sample_resumes/` isn't in
the repo, so creating the fixture is part of this change. Unless you'd rather it built on the
existing `sample_resume_text` fixture in `tests/conftest.py`, I'm creating the directory the
issue names. Happy to switch if you prefer the inline route.

**Planned change.** Three new files, nothing modified:

- `tests/fixtures/sample_resumes/jane_doe.md`, a synthetic markdown resume covering the section
  headers `ResumeParser` recognises, plus a short `README.md` beside it saying what the fixtures
  are and that they hold no real personal data.
- `tests/integration/test_ingestion_pipeline.py`, the end-to-end test. Two in-memory doubles: a
  `RecordingVectorDB` implementing the one `add(ids, embeddings, metadatas, documents)` method
  `BatchEmbeddingProcessor` calls, and a session double returning `None` from `first()` so
  `_check_skip` takes the not-yet-ingested path. Embeddings come from the repo's own
  `MockEmbeddingProvider`. Production code runs everywhere between those two seams.

**Not in scope:** the PDF branch of `ResumeParser`, which needs a binary fixture and a decision
about where it lives. Also `ingest_readme` and `ingest_repo_metadata`, and anything under
`ingestion/`. This issue adds coverage, it doesn't change behaviour. If the test turns up a bug,
that's a separate issue.

**How I'll show it worked.** The same commands from my reproduction, with the opposite expected
result. `pytest tests/integration -q` going from `no tests ran in 0.00s` to a real pass count,
`ls tests/fixtures/sample_resumes/` listing the two files, and `grep -rl IngestionPipeline
tests/` finding the new module. Plus `pytest tests/unit -q` unchanged, since none of this should
disturb anything.

**One thing I'd rather you decided than me.** `pyproject.toml` describes the `integration`
marker as "require Docker services". My test uses that marker and needs no Docker. I'm marking
it `integration` anyway, because it is one by every other measure, but changing what a shared
marker means is your call. Say the word if you'd rather it were marked differently, or the
description updated in its own change.

**A gap I'm leaving in on purpose.** The test doesn't prove the already-ingested skip branch
works. `_check_skip` swallows exceptions, so a badly built session double would pass for the
wrong reason. Mine returns `None` properly instead of raising, but the branch itself stays
uncovered. Noting it rather than fixing it, to keep this bounded.

AI-assisted work, per AI301.
