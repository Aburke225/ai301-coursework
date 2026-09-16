# Rubric: is this reproduction package ready to post?

<!--
Built from the proof families the lecture named: the environment is recorded, the steps are
complete and followable, the behaviour shown matches the issue rather than an adjacent one,
the outcome is stated honestly, and the words respect the repo's conventions.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| `env-recorded` | The report's environment record, read against the issue's own version claims in repo facts. | Names the operating system, the version of the software under test (a release tag, a commit sha, or a branch plus a date), and the version of any dependency the behaviour runs through. A missing dependency version passes only where the behaviour does not route through one. "Latest" and "current main" are not versions, they name a moving target the reader cannot return to. | required |
| `steps-rerunnable` | The steps section, read as though by a stranger holding the public repo and nothing else. | Every input needed to reach the reported state is present in the report or reachable from it: the commands as run, the file or fixture contents inline or linked publicly, and the starting state. Fails when any input lives somewhere the reader cannot reach, a private repo, an unshared config, "my usual setup". Terseness passes: three lines carrying everything is complete. | required |
| `artifact-matches-issue` | The report's pasted artifact, error text, command output, a listing, a measurement, read side by side with what the issue describes. | The artifact shows **the issue's** subject. Fails when it shows an adjacent or self-inflicted result instead: a different error or code path than the issue names, a run against a version the issue does not concern, or a state the reporter's own edit created. Also fails when the artifact shows only that the software starts, a version banner, a session opening, without touching the subject at all. | required |
| `gap-shown-for-non-bugs` | For an issue asking for something that does not yet exist (a feature, a test, docs): the artifact, read against the thing the issue says is missing. | The report demonstrates the absence rather than asserting it: the command that finds nothing, the directory listing that comes back empty, the example that does not run, the suite that collects zero tests. A claim that something is missing, with no artifact showing the search, fails. `unclear` where the issue describes a runtime behaviour instead, in which case `artifact-matches-issue` carries the weight. | required |
| `outcome-honest` | The report's stated conclusion, read against its own artifact. | The conclusion matches what the artifact shows. **An evidenced cannot-reproduce passes in full**, a real attempt, the environment and steps recorded, and the observed non-failure stated plainly is a complete and useful result. A confident root-cause diagnosis with no artifact behind it fails, as does a confirmation the artifact does not support. Where the report found the issue's own premise to be wrong, saying so plainly passes; quietly working around it does not. | required |
| `claim-is-specific` | The candidate claim comment, read against the issue text. | Names something only a reader of *this* issue could write: the specific behaviour, file, or gap at stake, plus a concrete first step. Fails where the comment would read identically on any other issue in the tracker ("I'd like to work on this, please assign me"). A claim promises investigation and a report back; it does not promise a fix or a date. | required |
| `conventions-respected` | The contribution-policy line in repo facts, and any stated template or disclosure ask. | The package meets the repo's stated asks. Where the policy requires disclosing AI assistance, the posted text discloses it. An outright ban on AI-assisted contributions fails the package. Silence passes: where nothing is stated, the course's own disclosure practice applies and the repo is owed nothing extra. | required |
| `reader-effort-low` | The report's ordering, and whether the artifact is pasted or described. | The reader meets environment, then steps, then artifact, then conclusion, with the artifact pasted rather than summarised. Ranking only: never holds a package that proves its case out of order. | preferred |

## Verdict rule

`ready` (the skill's JSON reports `accept`) only if **every** `required` check passes. One
required `fail` produces `hold` (`reject`).

`unclear` on a required check counts as a **fail**, with one stated exception:
`gap-shown-for-non-bugs` grades `unclear` when the issue describes a runtime behaviour
rather than a missing thing, and an `unclear` there does **not** hold the package, that
check simply does not apply, and `artifact-matches-issue` carries the weight instead.

`preferred` checks never change the verdict. They rank the packages already ready.
