# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

---

## Posted upstream

**GitHub username**

Aburke225

**Plan comment**

[PERMALINK TO MY PLAN COMMENT ON ISSUE #5, once it is posted]

> Following up on the reproduction with the plan I intend to build.
>
> **What's missing.** Nothing is broken. `IngestionPipeline.ingest_resume` carries a document
> through parse, chunk, embed, store, and no test touches any of it. The four searches in my
> previous comment show that.
>
> **Built on the corrected premise.** As flagged above, `tests/fixtures/sample_resumes/` isn't in
> the repo, so creating the fixture is part of this change. Unless you'd rather it built on the
> existing `sample_resume_text` fixture in `tests/conftest.py`, I'm creating the directory the
> issue names. Happy to switch if you prefer the inline route.
>
> **Planned change.** Three new files, nothing modified:
>
> - `tests/fixtures/sample_resumes/jane_doe.md`, a synthetic markdown resume covering the section
>   headers `ResumeParser` recognises, plus a short `README.md` beside it saying what the fixtures
>   are and that they hold no real personal data.
> - `tests/integration/test_ingestion_pipeline.py`, the end-to-end test. Two in-memory doubles: a
>   `RecordingVectorDB` implementing the one `add(ids, embeddings, metadatas, documents)` method
>   `BatchEmbeddingProcessor` calls, and a session double returning `None` from `first()` so
>   `_check_skip` takes the not-yet-ingested path. Embeddings come from the repo's own
>   `MockEmbeddingProvider`. Production code runs everywhere between those two seams.
>
> **Not in scope:** the PDF branch of `ResumeParser`, which needs a binary fixture and a decision
> about where it lives. Also `ingest_readme` and `ingest_repo_metadata`, and anything under
> `ingestion/`. This issue adds coverage, it doesn't change behaviour. If the test turns up a bug,
> that's a separate issue.
>
> **How I'll show it worked.** The same commands from my reproduction, with the opposite expected
> result. `pytest tests/integration -q` going from `no tests ran in 0.00s` to a real pass count,
> `ls tests/fixtures/sample_resumes/` listing the two files, and `grep -rl IngestionPipeline
> tests/` finding the new module. Plus `pytest tests/unit -q` unchanged, since none of this should
> disturb anything.
>
> **One thing I'd rather you decided than me.** `pyproject.toml` describes the `integration`
> marker as "require Docker services". My test uses that marker and needs no Docker. I'm marking
> it `integration` anyway, because it is one by every other measure, but changing what a shared
> marker means is your call. Say the word if you'd rather it were marked differently, or the
> description updated in its own change.
>
> **A gap I'm leaving in on purpose.** The test doesn't prove the already-ingested skip branch
> works. `_check_skip` swallows exceptions, so a badly built session double would pass for the
> wrong reason. Mine returns `None` properly instead of raising, but the branch itself stays
> uncovered. Noting it rather than fixing it, to keep this bounded.
>
> AI-assisted work, per AI301.

---

## Your branch

**Branch**

`feat/5-ingestion-e2e-test`

**Evidence**

**Before**, the four searches from my Unit 2 reproduction, re-run on the unmodified checkout:

```console
$ pytest tests/integration -q

no tests ran in 0.00s

$ ls tests/integration/
__init__.py

$ grep -rl "IngestionPipeline\|ingest_resume" tests/
(no output)

$ ls tests/fixtures/sample_resumes/
ls: tests/fixtures/sample_resumes/: No such file or directory
```

**After**, the same four commands against the built change:

```console
$ pytest tests/integration -q
.........                                                                [100%]
9 passed in 0.46s

$ ls tests/integration/
__init__.py  test_ingestion_pipeline.py

$ grep -rl "IngestionPipeline\|ingest_resume" tests/
tests/integration/test_ingestion_pipeline.py

$ ls tests/fixtures/sample_resumes/
README.md  jane_doe.md
```

Verbose, so the nine are visible instead of implied:

```console
$ pytest tests/integration -v
platform darwin -- Python 3.11.16, pytest-9.1.1, pluggy-1.6.0
configfile: pyproject.toml
collected 9 items

tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_fixture_is_present PASSED [ 11%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_ingest_resume_reports_chunks_and_does_not_skip PASSED [ 22%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_every_chunk_reaches_the_vector_db PASSED [ 33%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_stored_embeddings_have_the_provider_dimension PASSED [ 44%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_stored_metadata_carries_the_ingestion_context PASSED [ 55%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_stored_documents_are_the_chunk_text PASSED [ 66%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_embedding_ids_are_unique PASSED [ 77%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_source_id_is_stable_for_identical_content PASSED [ 88%]
tests/integration/test_ingestion_pipeline.py::TestResumeIngestionEndToEnd::test_different_profiles_get_different_source_ids PASSED [100%]

============================== 9 passed in 0.34s ===============================
```

**Regression check.** The plan said the unit suite should come out unchanged:

```console
$ pytest tests/unit -q --ignore=tests/unit/test_review_service.py
10 failed, 359 passed, 40 xfailed, 2 warnings in 2.88s
```

All ten failures sit in `tests/unit/test_security.py`, and every one of them comes from passlib
having no bcrypt backend installed in my virtualenv
(`passlib/utils/handlers.py:2254: in _stub_requires_backend`). `test_review_service.py` is
excluded because it imports `asyncpg`, which I don't have. Both are holes in my local
environment rather than in the repo, and CI on the pull request is where the real numbers come
from.

The strongest evidence that no regression is possible here isn't the numbers, though. It's that
`git diff --name-only` comes back empty. This change modifies no tracked file. It adds three new
ones and touches nothing any existing test imports.

## Eval iterations

**Run history**

[TO FILL IN AFTER MY FULL RUN: each run's agreement score in order. The last has to match the
agreement line in the committed `eval-run.txt`.]

**Package analysis**

[TO FILL IN AFTER MY FULL RUN: naming one scored package, what my rubric decided, what the gold
label said, and why my rubric read it that way.

The shape I most want to check myself against is a plan that's excellent on cause, scope and
buildability and still a reject. That's where a rubric built only around the engineering accepts
something it shouldn't, and only `thread-respected` catches it. If the harness agrees with me,
the account is about why the repo's stated asks live inside that check instead of getting one of
their own. If it disagrees, the disagreement is the better thing to write up.]

**Check rationale**

The `diagnosis-follows-evidence` check from `tools/plan-check/rubric.md`, as it currently reads:

> The account the plan gives is the one the package's own evidence supports. For a bug, the named
> cause is not contradicted by a control run, a maintainer's correction, or an artifact
> implicating a different path. For a gap, the thing the plan says is missing is the thing the
> evidence showed missing, including where that differs from what the issue claimed. Length and
> confidence are not evidence: a long, certain plan whose account the package disproves fails
> here. `unclear` where the package settles the question in neither direction.

The two-sentence split, one for a bug and one for a gap, is the revision that matters. My own
issue forced it.

My first draft read "the cause the plan names is the one the evidence supports", which assumes
there's a cause at all. Issue #5 has none. Nothing is broken; something is absent. Under that
first draft my own plan would have graded `unclear` on its most important check, not because the
plan was weak but because the check couldn't see what it was looking at.

What I care about most is the last clause in the gap sentence: *including where that differs
from what the issue claimed*. Without it, a plan that quietly worked around the missing fixtures
directory passes, and a plan that names the correction scores no better. That inverts the whole
point of the week. The clause makes following the evidence mean following it even when it
contradicts the issue.

**Trade-offs**

One thing it can't do is fail a plan that's right for the wrong reasons. A plan naming the correct cause
with no reasoning behind it passes as cleanly as one that traces it line by line, because the
check compares the conclusion to the evidence and never asks how the conclusion got there. I'll
take that. Grading the quality of reasoning rather than its agreement with the evidence is the
adjective-shaped judgement the template warns about, and two executors wouldn't decide it the
same way twice.

My second trade is the `unclear` exception in the verdict rule, and it's the one I'm less sure
about. Letting an `unclear` survive when `unknowns-stated` passes means a plan can propose an
account the evidence doesn't settle and still be ready. That's right for honest exploratory work.
It's also a door: someone could pair a weak account with a well-filled unknowns section and get
through a check that should have held them. The narrowness is the only mitigation. It applies to
exactly one check, it's spelled out in the verdict rule instead of left to the run, and it
reverts to a fail the moment `unknowns-stated` fails.

[TO FILL IN AFTER MY FULL RUN: whichever the run supports: a package whose result the
two-sentence split changes, or a canary confirming it moved nothing it shouldn't have.]

---

Related paths: `plan.md` and `eval-run.txt` in this directory; the skill's files in
`tools/plan-check/`.
