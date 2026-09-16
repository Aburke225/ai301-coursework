# Rubric: is this plan ready to post and build from?

<!--
Built from the failure families the lecture named: the diagnosis follows from the repro
evidence, the change is one bounded thing, a stranger could start executing it, the test plan
names an observable outcome, the unknowns are stated honestly, and the comment respects the
thread and the repo's conventions.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `diagnosis-follows-evidence` | The plan's account of what is wrong or missing, read against the repro-evidence block and any control, counter-example, or maintainer correction the package contains. | The account the plan gives is the one the package's own evidence supports. For a bug, the named cause is not contradicted by a control run, a maintainer's correction, or an artifact implicating a different path. For a gap, the thing the plan says is missing is the thing the evidence showed missing: including where that differs from what the issue claimed. Length and confidence are not evidence: a long, certain plan whose account the package disproves fails here. `unclear` where the package settles the question in neither direction. | required |
| `change-is-bounded` | The plan's scope pair (in / not-in), its file or area list, and its steps, read against the one thing the issue asks for. | Proposes **one** change addressing the issue. Fails when work the issue never asked for rides along: a refactor, a rename, a migration, a second fix in passing, a campaign of related cleanups. An honestly scoped-down plan that defers part of the problem with a stated reason **passes**, deferring is bounding, not shirking. | required |
| `stranger-could-start` | The plan's first implementation step and its file list. | Someone who has not read the thread could begin from the plan alone: the first step names a file or a function, not an activity. Fails on investigate-first plans that choose no layer ("profile it and optimise the hot path", "handle it upstream or vendored, whichever turns out right"), and on plans whose approach is still a menu with no choice made. | required |
| `test-plan-observable` | The plan's test-plan section, read against the evidence it builds on. | Names what will be observed to show the change worked, concretely enough to run: a command, a test id, or a measurement, with the expected-after stated. Re-running the unit-2 evidence with the expected-after named satisfies this. Where the unit-2 evidence was a gap demonstration, the same search re-run with a different expected result satisfies it. Fails on "add tests" and "verify it works" with nothing named. | required |
| `thread-respected` | The candidate plan comment, read against the thread and the stated conventions in repo facts. | Engages the direction the thread established: where a maintainer named an approach, ruled one out, or asked a question, the comment answers it rather than talking past it. Fails where the comment proposes an approach a maintainer already rejected, or ignores a direct question. Also fails where the repo's stated asks, template, disclosure, go unmet. Silence in the thread passes: with no direction to respect, there is none to contradict. | required |
| `unknowns-stated` | The plan's risks-and-unknowns section. | Names what it does not know, or states plainly that nothing is outstanding and why. An empty section fails; an honest "nothing outstanding, and here is the reason" passes. | required |
| `deviation-path-named` | Anywhere in the plan. | Says how a deviation gets recorded and where. Ranking only. | preferred |

## Verdict rule

`ready` (JSON `accept`) only if **every** `required` check passes. One required `fail`
produces `hold` (`reject`).

`unclear` on a required check counts as a **fail**, with one stated exception:
`diagnosis-follows-evidence` grades `unclear` where the package settles the question in
neither direction, and an `unclear` there does **not** sink the plan on its own, a plan may
honestly propose an account the evidence neither confirms nor contradicts, provided
`unknowns-stated` passes and the plan says so. Where `unknowns-stated` fails, the `unclear`
reverts to a fail.

`preferred` checks never change the verdict; they rank the plans already ready.
