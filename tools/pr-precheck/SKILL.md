---
name: pr-precheck
description: Grade one candidate pull request against the plan it implements and decide whether it is ready to submit. Use before opening a PR, or when grading a PR package snapshot in eval mode.
---

# pr-precheck: is this pull request ready to submit?

One question about one pull request: **is it ready to submit?** Never a different question,
never more than one package per run, never from impression. This tool executes `rubric.md`
by the steps in `procedure.md`.

A PR package is a candidate pull request: title, description, commit list, diff, test
evidence: read against **the plan it claims to implement** and the issue that plan belongs
to. The plan is the spine: most checks in the rubric are a comparison against it.

## What this tool reads

| File | Live mode | Eval mode |
|---|---|---|
| `rubric.md` | the checks and the verdict rule | same |
| `procedure.md` | the operating steps | same |
| `references/evidence-guide.md` | where each fact lives | same |
| `scope.md` | read **first**; gates the run | ignored entirely |
| `voice-guide.md` | held against the outgoing PR text | ignored entirely |

## Modes

**Live mode.** My own submission, checked before it goes out. Inputs: my `plan.md` including
its deviation notes, the diff on my branch against the base, my draft PR title and
description, and my test evidence, read against my issue. Issue-side evidence, the thread,
the PR template, the stated contribution and AI policy: comes from the real repo. A
house-chain student reads the house plan and house repro pack instead; the same checks grade
the same things there.

**Eval mode.** The package bundle is the whole world. Every fact comes from the bundle text;
nothing is fetched and nothing else is read. Eval mode always grades a complete package:
every check, full verdict rule, no shortcuts for missing context.

## The scope seam

In live mode, read `scope.md` before anything else. It names where the PR must live and the
house rules there. Refuse to grade work outside the scoped repo.

**If the scope's repo line still carries an unfilled placeholder, stop without grading** and
say so: the run cannot proceed until the cohort's scope file is in place, and the student
should get it from their instructor. Never guess a scope, never infer one from the diff,
never fall back to grading without one. This stop is a designed outcome, not a break, the
tool did run.

In eval mode, ignore `scope.md` entirely.

## The voice seam

In live mode, read `voice-guide.md` and hold the outgoing PR text: title and description , 
against my own rules. Report every rule the draft breaks in the summary, quoting the rule and
the line that breaks it.

**A voice-guide break is feedback, never a verdict change.** It does not move `accept` to
`reject` on its own. The one exception is where `rubric.md` itself carries a check that reads
the voice guide; that check then gates like any other.

In eval mode, ignore `voice-guide.md` entirely: voice is personal and carries no gold labels.
Communication standards that apply to everyone belong in the rubric instead.

## The refusal rule

If `rubric.md` has no checks, or `procedure.md` has no steps, **refuse to grade and say so.**
A tool that invents checks at runtime produces verdicts that look like judgement and are
noise, which is worse than no tool at all.

Instruction comments inside a template are not content: a file carrying only its shipped
comments is still empty. Name the empty file and stop.

## Workflow

1. Live mode: read `scope.md`, confirm the package is in scope, stop if the repo line is a
   placeholder. Eval mode: skip.
2. Check `rubric.md` and `procedure.md` for content. Refuse if either is empty.
3. Execute `procedure.md` from its first stage: read the package in the order it sets, record
   what it says to record, then run the checks in the order it fixes.
4. Grade every check `pass`, `fail`, or `unclear`, each with one line of evidence, the fact
   or quote that decided it.
5. Assemble the verdict by the rubric's verdict rule, exactly as `procedure.md` directs.
6. Live mode: hold the title and description against `voice-guide.md`; report breaks in the
   summary.
7. Emit the summary, then the JSON block.

## Verdict space

Binary: `accept` (ready to submit) or `reject` (hold). No third verdict, no "accept with
reservations", no score. Reservations belong in check evidence lines.

## Output

A readable per-check summary may come first. The reply then ends with a fenced JSON block,
and nothing follows it:

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

The harness parses the last fenced JSON block, so it must be present, valid, and last.

## Grading discipline

- **Evidence first.** No grade without the fact that decided it.
- **Grade the thing, not the polish.** A terse complete PR can be ready; a beautiful confident
  one can be hiding drift. Every check reads the artifact against the plan, the issue, and the
  stated standards: never the formatting.
- **The rubric decides, not the run.** A check that passes by its stated condition passes, even
  where it feels wrong. Note the tension in the summary; fix it in the rubric.
- **The procedure decides how, not the run.** Follow `procedure.md` as written. Where it has a
  gap, report the gap rather than inventing a step.
- **Unclear defaults to fail.** A pull request I cannot verify from the package is one that is
  not ready to submit.
