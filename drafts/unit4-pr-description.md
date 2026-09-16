## Summary

`IngestionPipeline.ingest_resume` carries a document through parse, chunk, embed, store, and
nothing tested any of it end to end. `tests/integration/` held only an `__init__.py`, and no
test anywhere referenced the pipeline. This adds that coverage, plus the resume fixture it runs
against.

The pipeline takes `vector_db`, `db_session`, and `embedding_provider` as constructor arguments,
so the test substitutes in-memory doubles at those two seams and runs production code everywhere
in between. No ChromaDB, no Postgres, no network.

One correction worth your attention. The issue asks for a test "using the fixtures in
`tests/fixtures/sample_resumes/`", and that directory wasn't in the repo, so creating it is part
of this change rather than an input to it. I raised this on the issue thread before building and
offered the alternative, which is building on the existing `sample_resume_text` fixture in
`tests/conftest.py`. I defaulted to creating the directory the issue names, because "from file
upload through embedding storage" reads as though the file on disk is part of what's under test.
Happy to switch if you'd rather the inline route.

## Issue

Closes #5

## Changes

- `tests/fixtures/sample_resumes/jane_doe.md`, a synthetic markdown resume covering the section
  headers `ResumeParser` recognises. No real personal data.
- `tests/fixtures/sample_resumes/README.md`, saying what the fixtures are and that they're
  synthetic, so whoever adds the next one knows the convention.
- `tests/integration/test_ingestion_pipeline.py`, nine tests over one end-to-end path.
  `RecordingVectorDB` implements the single `add(ids, embeddings, metadatas, documents)` method
  `BatchEmbeddingProcessor._store_embedding` calls. `NoMatchSession` returns `None` from
  `first()`, so `_check_skip` takes the not-yet-ingested path. Embeddings come from the repo's
  own `MockEmbeddingProvider`.

**No tracked file is modified.** `git diff --name-only` is empty. This change is three new files
and nothing under `ingestion/` is touched, because the issue asks for coverage rather than a
behaviour change. If this test ever turns up a bug, that's a separate issue and a separate PR.

## Testing

- [ ] **CI is green on this PR (all five jobs)**, required for review
- [x] Unit tests pass (`make test-unit`), run as `pytest tests/unit`; see the note below
- [x] Integration tests pass (`make test-integration`), 9 passed, output below
- [ ] Linter passes (`make lint`), not run locally; see note
- [ ] Type checker passes (`make typecheck`), not run locally; see note
- [x] New/updated tests cover the changes. The nine tests are the change.
- [x] If this fixes a seeded bug: removed its `@pytest.mark.xfail` marker (and any matching
      suppression in `pyproject.toml`). N/A, #5 is an enhancement rather than a seeded bug, and
      carries no xfail marker or mypy override.

**Before**, the four searches from my reproduction comment, on the unmodified checkout:

```console
$ pytest tests/integration -q
no tests ran in 0.00s

$ ls tests/fixtures/sample_resumes/
ls: tests/fixtures/sample_resumes/: No such file or directory

$ grep -rl "IngestionPipeline\|ingest_resume" tests/
(no output)
```

**After**, the same commands:

```console
$ pytest tests/integration -q
.........                                                                [100%]
9 passed in 0.46s

$ ls tests/fixtures/sample_resumes/
README.md  jane_doe.md

$ grep -rl "IngestionPipeline\|ingest_resume" tests/
tests/integration/test_ingestion_pipeline.py
```

**Regression check:**

```console
$ pytest tests/unit -q --ignore=tests/unit/test_review_service.py
10 failed, 359 passed, 40 xfailed, 2 warnings in 2.88s
```

**On the two unchecked boxes and the ten failures.** Everything unrun or red here is my local
environment. Named individually rather than waved at:

- **Linter and type checker:** not run. I didn't install the dev toolchain locally, so I have no
  result either way and left both boxes unchecked rather than guess.
- **The ten unit failures** are all in `tests/unit/test_security.py`, and all of them come from
  passlib having no bcrypt backend in my virtualenv
  (`passlib/utils/handlers.py:2254: in _stub_requires_backend`).
- **`tests/unit/test_review_service.py`** is excluded above because it imports `asyncpg`, which I
  don't have installed.

None of the three can be caused by this change, and the reason is structural rather than a
judgement call: this PR modifies no tracked file and adds nothing any existing test imports. CI
on a full environment is where the real numbers come from.

Python 3.11.16 locally, matching `requires-python = ">=3.11"`.

## Screenshots / Demo

N/A. A test-only change with no user-visible surface. The before and after console output above
is the demonstration.

## Notes for Reviewers

Three things worth your attention.

**The fixtures premise**, covered in the Summary. The directory the issue names didn't exist. If
you'd rather this built on `tests/conftest.py`'s inline fixture, that's a small change and I'm
happy to make it.

**The `integration` marker.** `pyproject.toml` describes it as "require Docker services". This
test uses the marker and needs no Docker. I marked it `integration` anyway because it is one by
every other measure, but changing what a shared marker means is your call, so I've deliberately
left the description alone.

**A gap I left in on purpose.** The tests don't cover the already-ingested skip branch.
`_check_skip` swallows exceptions, so a badly built session double would make such a test pass
for the wrong reason, and getting it right needs a decision about how much of the real ORM to
stand up. `NoMatchSession` returns `None` properly instead of raising, so the not-skipped path is
honest, but the skip path stays uncovered. Noted rather than fixed, to keep this bounded to what
#5 asked for.

This work is AI-assisted, per AI301. I understand and have run the change. The diagnosis, the
scoping decisions, and this description are mine.
