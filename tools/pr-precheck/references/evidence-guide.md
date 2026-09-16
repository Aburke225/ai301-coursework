# Evidence guide: where the facts live in a PR package

Four families, one per failure shape the lecture named.

## Family 1: plan fidelity (silent drift)

Mechanical, hunk by hunk. For each hunk: **which promised item, or which recorded deviation,
is this?** A hunk answering neither is drift.

Drift has a signature: it is almost always *competent*. The rename is a better name. The
reworked helper is cleaner. The second fix is a real bug. None of that matters, a maintainer
who agreed to review one change is being handed two, and the second arrived unannounced.

- **Passes:** a diff matching the plan; a diff diverging with the divergence written into the
  plan's deviation notes and, where the posted intent changed, into the thread.
- **Fails:** a fix bundled with a rename; a plan promising two things where the diff has one
  and says nothing.

Drift runs both directions. Delivering less than the plan, silently, is the same failure as
delivering more.

**Additive changes drift too.** A PR that only adds files still gets the hunk-by-hunk read: a
fixture nobody planned or a helper belonging to another issue is drift regardless of whether
anything was modified.

## Family 2: test evidence (not tested)

Evidence is output. An assertion about output is not evidence.

- **Passes:** commands and their captured output, showing the subject before and after,
  through the path the change actually touched. A named check that could not run, with the
  reason, passes as an honest gap.
- **Fails:** "tested locally", "verified working", "all tests pass" with nothing shown. A
  before/after exercising a path the diff never changed. Any check that went red and was
  quietly dropped from the write-up.

**Where the issue asked for something absent**, the before/after is symmetric with the
reproduction: the search that found nothing, then the same search finding it. `pytest
tests/integration -q` reporting `no tests ran`, then reporting a pass count, is a complete
before/after, the command is identical and only the result moved.

The plan's test plan is the checklist: whatever it named, the evidence shows, or says why not.

## Family 3: diff quality (unreviewable)

Read the diff as the maintainer will, a request for their attention. Everything in it that
is not the change is a tax on that attention.

- Working notes swept in: `plan.md`, `pr_draft.md`, `test_evidence.md` are mine, not part of
  the change. `git status` before calling the diff done is the habit; `.git/info/exclude` is
  the belt.
- Debugging leftovers: prints, temporary logging, commented-out attempts.
- A formatting or lint pass riding along on untouched lines. This repo's
  `docs/CONTRIBUTING.md` asks explicitly that lint and type findings not be bulk-fixed outside
  their own issue.
- Generated files and lockfiles the change did not require.
- A virtualenv, a `.pytest_cache`, or fixture scratch output. Easy to create while testing and
  easy to miss.

## Family 4: standards and communication (standards wall)

The family that sinks otherwise excellent pull requests, and the cheapest to satisfy, which
is what makes losing points here so annoying.

- **The template.** Every section gets real content. `N/A` with a reason counts; deleting the
  section does not. For this repo, `.github/PULL_REQUEST_TEMPLATE.md` asks for Summary, Issue,
  Changes, Testing (a six-item checklist), Screenshots/Demo, and Notes for Reviewers.
- **The conventions.** Branch shape `<type>/<issue-number>-<short-description>`, and the
  commit convention the contributing guide states.
- **The disclosure.** Course work is AI-assisted by design. Where a policy requires
  disclosure, it is owed, always, and its absence fails the package however good the code is.
  Where no policy is stated, the course's own practice applies: say it anyway, in the
  description, in my own words.

A repo banning AI-assisted contributions outright is a wall, not a term: the package fails and
the honest move is a different issue.
