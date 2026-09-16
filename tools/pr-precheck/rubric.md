# Rubric: is this pull request ready to submit?

<!--
Built from the four failure categories the lecture named: silent drift (plan fidelity), not
tested (test evidence), unreviewable (diff quality), and standards wall (standards and
comms).
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `diff-matches-plan` | The diff, hunk by hunk, against the plan's scope pair and its deviation notes. | Every hunk traces to something the plan proposed, **or** to a deviation the plan records. Fails where the diff does more than the plan, a rename, a refactor, a reworked adjacent function, a second fix riding along. Also fails where it does **less**: a plan promising two things and a diff delivering one, with no deviation note. A recorded deviation passes; the check rewards honesty about a change, not the absence of change. | required |
| `description-promises-only-the-diff` | The PR description, against the diff. | Every behaviour the description claims is in the diff, and the description does not omit a behaviour the diff changes. Fails both ways: promising a docs update the diff never makes, and shipping a rename the description never mentions. | required |
| `evidence-shows-before-and-after` | The test-evidence section, against the plan's test plan and the issue's subject. | The evidence shows the issue's subject observably changing: a before and an after, through the real code path, with commands and their output present. For an issue asking for something absent, the before is the search that found nothing and the after is the same search finding it. Fails on assertion in place of evidence, "tested locally", "verified working", "all tests pass" with nothing shown, and where the evidence exercises a path the change did not touch. **An honestly reported failing or unrun check passes this check** where the reason is stated; a hidden failure does not. | required |
| `repo-checks-run` | The test-evidence section, against the repo's own stated checks in repo facts: its contributing guide, CI config, or PR-template asks. | The repo's stated checks were run with their outcome visible, or each unrun check is named with the reason it could not run. Fails where the repo states checks and the evidence is silent about them. A vague gesture at "some checks" fails: each one is named or it is not accounted for. | required |
| `diff-is-reviewable` | The diff itself. | Contains only the change. Fails on debris: commented-out code, debugging prints or logging left in, a working note swept in (`plan.md`, `pr_draft.md`, `test_evidence.md`), an unrelated formatting pass, a lockfile or generated artifact the change did not require, a stray whitespace reflow across untouched lines. | required |
| `standards-met` | The template asks and contribution policy in repo facts, against the title, description, and commits. | The repo's stated asks are satisfied: template sections carry real content (an `N/A` with a reason counts; a deleted section does not), commit and branch conventions are followed, and where the policy requires disclosing AI assistance, the description discloses it. **All course work is AI-assisted by design, so a stated disclosure requirement always applies.** Where no policy is stated, the course's own practice applies and the repo is owed nothing extra. An outright ban on AI-assisted contributions fails the package. | required |
| `issue-linked` | The title and description. | Names the issue it closes in a form the repo resolves (`Fixes #N`, `Closes #N`, or the repo's stated convention). Ranking only. | preferred |

## Verdict rule

`accept` (ready to submit) only if **every** `required` check passes. One required `fail`
produces `reject` (hold).

`unclear` on a required check counts as a **fail**. A pull request whose readiness I cannot
verify from what is in front of me is not one I should ask a maintainer to spend review time
on, and in eval mode the bundle is the whole world, so a fact absent from the package is
absent from the maintainer's view too.

`preferred` checks never change the verdict; they rank the pull requests already ready.

**A note on the honest shortfall, because it decides several packages.** A PR disclosing a
limitation, a deferred edge, or a plan deviation is not penalised for the shortfall, it is
credited for the disclosure. `diff-matches-plan` reads a recorded deviation as a pass, and
`evidence-shows-before-and-after` reads a named unrun check as a pass. What fails is the
silent version of the same thing: a diff quietly doing more or less than the plan, or
evidence quietly omitting a check that went red.
