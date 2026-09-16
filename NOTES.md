# AI301 Assignments 1 to 4

My working set for **issue #5** (`Add end-to-end ingestion test with a sample resume fixture`)
in `codepath/pathreview-ai301-fa26-s1`. GitHub handle on all of it: Aburke225.

Nothing is posted upstream yet. Everything below is local.

## Layout

    tools/issue-select/     A1: rubric.md, scope.md (fit profile) + the shipped SKILL/evidence-guide
    tools/repro-check/      A2: rubric.md, voice-guide.md, references/evidence-guide.md
    tools/plan-check/       A3: rubric.md, procedure.md, references/evidence-guide.md
    tools/pr-precheck/      A4: SKILL.md, rubric.md, procedure.md, references/evidence-guide.md
    beat-1-sandbox/unit-1/  selection.md
    beat-1-sandbox/unit-2/  reproduction.md
    beat-1-sandbox/unit-3/  plan.md, plan-and-implement.md
    beat-1-sandbox/unit-4/  pull-request.md
    drafts/                 my claim, repro and plan comments; the PR title and description
    branch-files/           the change itself, staged the way it sits on the branch

## Where the work stands

Built and run on Python 3.11.16, matching the project's `requires-python`:

- Demonstrated the gap four ways on a clean checkout.
- The change is three new files. `git diff --name-only` comes back empty, so nothing tracked
  moved.
- `pytest tests/integration -q` went from `no tests ran in 0.00s` to `9 passed`.
- Unit regression: 359 passed, 40 xfailed, 10 failed. All ten sit in `test_security.py` and come
  from a missing bcrypt backend in my venv. I reproduced them on a pristine checkout to be sure
  they were not mine.

## What I still owe

Every `eval-run.txt`, every **Run history** field, every **Package analysis**, and the
run-dependent half of each **Trade-offs** field are marked `[TO FILL IN AFTER MY RUN]`. I have
not spent a confirming full run yet, and a full run is about $4 of course credit, so nothing in
these files claims a result I do not have.

From each unit's starter clone:

    python3 run_eval.py --rubric <path to my rubric> --save-run eval-run.txt

Then the cheap loop on whatever disagrees: `--only issue-07,issue-12` at roughly $0.20 an item,
and save the full run only once I believe the rubric.

## Open questions I want answered upstream

- Whether the maintainer would rather the test build on `tests/conftest.py`'s existing
  `sample_resume_text` fixture than on a new file on disk. I defaulted to the file and said so.
- What to do about the `integration` marker, which `pyproject.toml` describes as "require Docker
  services" while my test needs none. Raised it rather than editing a shared marker myself.
- Whether the uncovered already-ingested skip branch is worth its own issue.
