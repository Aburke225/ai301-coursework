# Procedure: how this tool grades a PR package

## Read order

Read the package once, in this order, before grading anything. Five of the seven checks are
comparisons, and each needs its right-hand side written down before the pull request can
colour it.

1. **The issue context.** One line: what this PR is supposed to change or add.
2. **The repo-facts block.** Record the PR-template sections the repo asks for, its stated
   commit and branch conventions, the checks it says it runs, and the contribution policy , 
   specifically whether AI assistance is banned, must be disclosed, or is unmentioned.
3. **The plan-context block** (live: my own `plan.md`). Record two lists:
   - **Promised**: every distinct change the plan commits to.
   - **Deviations**: every divergence the plan itself records, with its reason.
   These are the whole right-hand side of `diff-matches-plan`. Build them before reading the
   diff, or the diff will quietly redefine what the plan "meant".
4. **The candidate PR**, in its own order: title, description, commit list, diff, test
   evidence. Read the diff hunk by hunk and write one line per hunk saying what it changes.

## Evidence gathering

| Check | Where the fact comes from | What to record |
|---|---|---|
| `diff-matches-plan` | The per-hunk list against Promised + Deviations | Each hunk traced / untraced; each promised item delivered / undelivered |
| `description-promises-only-the-diff` | The description against the per-hunk list | Each claim present / absent in the diff; each hunk mentioned / unmentioned |
| `evidence-shows-before-and-after` | The test-evidence section against the plan's test plan | The before state, the after state, the command producing each, and whether output is shown or asserted |
| `repo-checks-run` | The test-evidence section against the repo's stated checks | Each stated check run-and-shown / named-as-unrun-with-reason / silent |
| `diff-is-reviewable` | The diff | Any hunk that is not the change: debris, working notes, formatting, generated files |
| `standards-met` | Title, description, commits against the recorded asks and policy | Each template section filled / N-A-with-reason / missing; the disclosure present / absent / not-required |
| `issue-linked` | Title and description | The closing keyword and issue number, or absent |

Live mode gathers issue-side facts from the real repo, the thread,
`.github/PULL_REQUEST_TEMPLATE.md`, the contributing guide, and whatever the CI config names
as its checks, and PR-side facts from `plan.md`, `git diff <base>...HEAD`, the draft title
and description, and the captured test evidence.

## Check execution

Fixed order, putting the three plan-comparison checks first while the Promised and Deviations
lists are fresh and before the diff's own framing has settled:

1. `diff-matches-plan`
2. `description-promises-only-the-diff`
3. `evidence-shows-before-and-after`
4. `repo-checks-run`
5. `diff-is-reviewable`
6. `standards-met`
7. `issue-linked`

Grade each against the facts recorded during the read, not by re-reading the package. Re-read
only where a recorded fact is ambiguous, and then only the part the check names.

Every grade carries one line of evidence. A grade without one is unfinished.

**When evidence is genuinely absent**, record `unclear` and say in the evidence line what was
missing. Do not fill the absence from the issue, the repo, or from what a competent PR would
probably have done. In eval mode especially, an absence is a finding: the maintainer reading
this package would not have that fact either.

**No check may be graded from another check's conclusion.** A PR failing `diff-matches-plan`
still gets `diff-is-reviewable` graded on its own evidence. Cascading one fail through the
rest turns a single reading error into six and destroys the per-check signal the report
exists to give.

**The honest-shortfall rule, applied at grading time.** Before failing `diff-matches-plan` on
an untraced hunk, check the Deviations list for it. Before failing
`evidence-shows-before-and-after` on a missing check, look for a stated reason. A disclosed
gap passes; an undisclosed one fails. This is the single most common place two executors
disagree, so it is written here rather than left to each run.

**An additive diff is still read hunk by hunk.** A change consisting only of new files can
drift exactly as a modifying one can, a fourth file nobody planned, a helper that belongs to
a different issue. "No tracked file modified" is evidence for `diff-is-reviewable`; it is not
a pass for `diff-matches-plan`.

## Verdict assembly

1. Collect the seven grades.
2. Apply the rubric's verdict rule: `accept` only where every `required` check passes.
3. `unclear` on any required check enters as a fail.
4. Report the `preferred` grade, then set it aside; it never enters the verdict.
5. Quote the deciding check in the summary. On a `reject`, that is the first required fail in
   execution order, and its evidence line goes in verbatim so the reader gets a next step
   rather than a label. On an `accept`, quote the check that came closest to failing.
6. Live mode only: after the verdict is assembled, hold the title and description against
   `voice-guide.md` and report any broken rule, quoting both the rule and the offending line.
   **This never changes the verdict**, it is reported last, after the verdict is fixed, so it
   cannot leak into it.

The same grades produce the same verdict every time. Nothing here is a judgement call,
because every judgement was made and recorded upstream.
