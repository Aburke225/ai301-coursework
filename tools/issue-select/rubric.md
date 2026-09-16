# Rubric: is this a good first issue?

<!--
Built from the four families the lecture named, the maintainer is alive, the repo is in
use, the scope fits a newcomer, nobody else is already on it: plus the fifth surface the
evidence guide adds: am I allowed to contribute the way I actually work?
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `repo-not-archived` | The `archived:` flag on the repo line of the repo-facts block. | Reads `archived: no`. An archived repo is read-only, so no pull request can ever land in it. | required |
| `maintainer-active` | The "last 5 default-branch commits" list and the "maintainer first-response sample", both in repo facts, measured against the block's capture date. | At least one of the last 5 default-branch commits falls within 180 days of the capture date. A commit by a `[bot]` account counts only where its message shows it merged a human's pull request (a `Merge pull request #N`, or an `(#N)` suffix). | required |
| `repo-in-use` | The "latest release" and "last push to any branch" lines, measured against the capture date. | Either a release within 365 days of capture, or a push to any branch within 180 days. A repo with no releases at all passes on the push alone: young and small projects ship straight from the default branch, and absence of releases is not absence of use. | required |
| `scope-bounded` | The issue body and the whole comment thread. | The issue asks for **one** thing a newcomer could finish. Fails on: a body that is a checklist of separately shippable items, or an issue calling itself an umbrella, meta, tracking or mega issue; a change stated to span the codebase or the core internals; a design still being argued in the thread with no maintainer having settled it; a usage question rather than a change; or a feature request with no specification where the thread shows the product decision is still open. A terse body, a missing reproduction, or a bare acceptance checklist does **not** fail here on its own, grade the size of the work asked for, not the polish of the writeup. | required |
| `unclaimed` | The `assignees:` and `linked PRs:` lines of repo facts, plus every claim comment in the thread with its date, against the capture date. | All three hold: no assignee; no linked PR in the open state; and no unanswered claim comment ("I'll take this", "working on this") dated within 120 days of capture. A claim older than 120 days with no open linked PR is **stale** and does not block. A closed, unmerged linked PR is an abandoned attempt, not a claim. | required |
| `ai-policy-permits` | The "contribution policy" line of repo facts, including any AI-policy file or PR-template disclosure ask quoted there. | The policy does not ban AI-assisted contributions outright. A ban fails. Conditions **pass**: disclose the assistance, understand and test what you submit, have a human review the output. Those are terms to meet rather than walls. Silence passes: most repos state nothing, and nothing is not a restriction. | required |
| `newcomer-signposted` | The issue's labels, and the `author_association` of whoever opened it. | Carries a newcomer-facing label (`good first issue`, `help wanted`, `beginner`) **or** was opened by an `OWNER`, `MEMBER` or `COLLABORATOR`. Ranking only. It never gates a verdict, because a friendly label tells you what a maintainer intended, not how big the work is. | preferred |

## Verdict rule

`accept` only if **every** `required` check passes. One required `fail` produces `reject`.

`unclear` on a required check counts as a **fail**. A first issue whose safety I cannot
verify from the evidence in front of me is not one I should take, and in eval mode the
bundle is the whole world, so missing evidence is a real answer rather than a gap I may
fill by guessing.

`preferred` checks never change the verdict. Among issues already accepted, one carrying a
newcomer label or filed by a maintainer is the better place to start.
