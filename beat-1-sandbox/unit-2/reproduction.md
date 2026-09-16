# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

---

## Your identity upstream

**GitHub username**

Aburke225

---

## Posted upstream

**Claim comment**

[PERMALINK TO MY CLAIM COMMENT, once it is posted]

> I'd like to take this one.
>
> First step is to find out what the test tree actually holds today: whether `tests/integration/`
> has anything in it, and whether anything currently touches `IngestionPipeline.ingest_resume`
> end to end. I'll post what I find either way.
>
> One thing I want to check before I write any of it. The issue points at fixtures in
> `tests/fixtures/sample_resumes/`, and a first look at the tree suggests that directory might
> not be there. If it isn't, creating the fixture is part of this work rather than something I
> inherit, and I'd rather establish that in the open than quietly widen the scope on my own.
>
> Working on this as part of AI301, so the work is AI-assisted. I'll note that on the PR too.

**Reproduction comment**

[PERMALINK TO MY REPRODUCTION COMMENT, once it is posted]

> Confirmed the gap. The issue's description of it is slightly off, in a way worth sorting out
> before anyone starts writing.
>
> **Environment**
>
> - OS: macOS 26.6.2 (Darwin 25.6.0), arm64
> - Under test: `codepath/pathreview-ai301-fa26-s1` @ `main`, commit `996fabe`, checked out 2026-09-14
> - Interpreter: Python 3.11.16 in a venv, per `requires-python = ">=3.11"` in `pyproject.toml`
>
> **The gap, four ways**
>
> ```console
> $ pytest tests/integration -q
>
> no tests ran in 0.00s
>
> $ ls tests/integration/
> __init__.py
>
> $ grep -rl "IngestionPipeline\|ingest_resume" tests/
> (no output)
>
> $ ls tests/fixtures/sample_resumes/
> ls: tests/fixtures/sample_resumes/: No such file or directory
> ```
>
> The integration package exists but holds nothing except its `__init__.py`. No test anywhere
> mentions the pipeline. And the whole `tests/fixtures/` tree is absent.
>
> **The premise worth correcting.** The issue says to add a test "using the fixtures in
> `tests/fixtures/sample_resumes/`". Those fixtures aren't in the repo, so they have to be created
> as part of this. I'm flagging it rather than absorbing it quietly, because it changes how big the
> issue is.
>
> There's also an alternative someone may have had in mind: `tests/conftest.py` already provides a
> `sample_resume_text` fixture as an inline string. If you'd rather the test build on that than on
> a new file on disk, say so and I'll go that way. My default is to create the directory the issue
> names, because "from file upload through embedding storage" reads to me like the file on disk is
> part of what's being tested.
>
> **What the pipeline gives us to work with**, since it changes how much of this needs real
> services:
>
> ```console
> $ python -c "
> from ingestion.pipeline import IngestionPipeline
> print([m for m in dir(IngestionPipeline) if m.startswith('ingest_')])
> "
> ['ingest_readme', 'ingest_repo_metadata', 'ingest_resume']
> ```
>
> `IngestionPipeline.__init__` takes `vector_db`, `db_session`, and `embedding_provider` as
> arguments, and the repo already ships a `MockEmbeddingProvider` in
> `ingestion/embeddings/provider.py`. So the full parse, chunk, embed, store path can run against
> in-memory doubles at those two seams, with production code everywhere in between, and no
> ChromaDB or Postgres needed to see it work.
>
> One thing for whoever reviews this. `pyproject.toml` describes the `integration` marker as
> "require Docker services". A test built this way doesn't, so either the marker's description or
> my use of it needs a decision. I'll raise it again with the plan rather than guess now.
>
> AI-assisted work, per AI301.

## Eval iterations

**Run history**

[TO FILL IN AFTER MY FULL RUN: each run's agreement score in order. The last has to match the
agreement line in the committed `eval-run.txt`.]

**Package analysis**

[TO FILL IN AFTER MY FULL RUN: naming one scored package, what my rubric decided, what the gold
label said, and why my rubric read it that way.

The one I expect to learn most from is whichever package is polished, well structured, and still
a reject. That shape is a version table, numbered steps, clean headings, and underneath all of
it an artifact that doesn't show the issue's subject. Every structure-shaped check I could have
written passes it. Only `artifact-matches-issue` holds it. If the harness agrees with me there,
the account is about why that check lists failure shapes instead of describing what a pass looks
like. If it disagrees, the disagreement is the better thing to write up.]

**Check rationale**

The `gap-shown-for-non-bugs` check from `tools/repro-check/rubric.md`, as it currently reads:

> The report demonstrates the absence rather than asserting it: the command that finds nothing,
> the directory listing that comes back empty, the example that does not run, the suite that
> collects zero tests. A claim that something is missing, with no artifact showing the search,
> fails. `unclear` where the issue describes a runtime behaviour instead, in which case
> `artifact-matches-issue` carries the weight.

This check didn't exist in my first draft, and writing it was the main thing I learned this week.

Every check I had written assumed a bug. Something runs, something goes wrong, you paste the
traceback. My own issue has no behaviour to run, because it asks for a test that doesn't exist
yet. Under the first draft my own package would have graded `unclear` on `artifact-matches-issue`
and been held, not because the package was weak but because the check couldn't see what kind of
issue it was looking at.

The fix wasn't to loosen `artifact-matches-issue`. It was to add a check covering the other kind
of issue and give it an explicit not-applicable path, so the two hand off to each other instead
of one getting stretched over both. That last sentence is the handoff, written down so an
executor is never guessing which check owns a package.

**Trade-offs**

The check gives up any judgement about whether the absence is *complete*. My report shows four
searches that came back empty. The check would have passed on one. A reader could reasonably
want the standard to be "looked everywhere it could plausibly be", but that's unbounded, and an
executor can't decide it the same way twice, so I took the weaker version that's actually
decidable.

It also means an issue whose gap is real but whose cause is misdiagnosed still passes here.
Showing that `tests/fixtures/sample_resumes/` is absent isn't the same as knowing why, and my
rubric only asks for the first. I'm fine with that. The cause is the plan's job next week, and a
repro check that started grading causes would be doing unit 3's work early.

[TO FILL IN AFTER MY FULL RUN: whichever the run supports: a package whose result this check
changes, or a canary re-run with `--only` after adding it.]

---

Related paths: `eval-run.txt` in this directory; the skill's files in `tools/repro-check/`.
