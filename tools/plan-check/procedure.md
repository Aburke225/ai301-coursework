# Procedure: how this skill grades a plan package

## Read order

Read the whole package once, in this order, before grading anything:

1. **The issue context.** One line: the single thing the issue asks to change or add.
   Everything downstream is measured against this line.
2. **The repo-facts block.** Note the stated template asks, the contribution policy, and any
   AI-disclosure rule. Note them even when they look irrelevant: `thread-respected` needs
   them and will not go looking later.
3. **The repro-evidence block.** Write down what the evidence actually establishes: which
   code path, which error, or which absence. Write down separately anything it **rules out**
  , a control run, a version comparison, a search that came back empty where the issue said
   something would be there. That second list is what catches a plan whose account the
   package disproves, and it is invisible if the plan is read first.
4. **The plan.**
5. **The plan comment.**

The order matters because the two heaviest checks are comparisons, and a comparison needs its
right-hand side written down before the plan can colour it. Reading the plan first makes its
account feel like the frame, and the evidence then reads as support for it.

## Evidence gathering

| Check | Where the fact comes from | What to record |
|---|---|---|
| `diagnosis-follows-evidence` | The plan's account; the repro-evidence block; maintainer comments | The account in the plan's words, then the line of evidence that supports or contradicts it. Record a contradicting line verbatim. |
| `change-is-bounded` | The scope pair, file list, and steps | Every distinct change proposed, one per line. The count is the check: more than one behaviour touched, with no stated deferral, is the fail. |
| `stranger-could-start` | The plan's first implementation step | Whether it names a file, a function, or a line. Record the step verbatim. |
| `test-plan-observable` | The plan's test-plan section | The command, test id, or measurement, plus the expected-after. If either is missing, record which. |
| `thread-respected` | The plan comment; thread highlights; the template and policy lines | Any maintainer direction, an approach named, one ruled out, a question asked, and whether the comment answers it. |
| `unknowns-stated` | The risks-and-unknowns section | Present and filled / present and empty / absent. |
| `deviation-path-named` | Anywhere in the plan | Present or absent; one line if present. |

Live rather than eval: the repro evidence is my own posted comment, the thread is the issue
page read to the end, and the policy lines come from the repo's `CONTRIBUTING.md` and PR
template as recorded in my `CLAUDE.local.md`.

## Check execution

Checks run in this fixed order, which puts the two evidence-reading checks first, while the
evidence is fresh and before the plan's framing has settled:

1. `diagnosis-follows-evidence`
2. `change-is-bounded`
3. `stranger-could-start`
4. `test-plan-observable`
5. `thread-respected`
6. `unknowns-stated`
7. `deviation-path-named`

Grade each against the facts recorded during the read, not by re-reading the package.
Re-read only where a recorded fact is ambiguous, and then only the part the check names.

Every grade carries one line of evidence, the quote or fact that decided it. A grade without
one is not finished.

**When evidence is genuinely absent**, record `unclear` and say in the evidence line what was
missing. Do not fill an absence from the issue text, from the repo, or from what a reasonable
plan would probably have said. `unclear` is a real grade with a stated consequence in the
verdict rule; a guess is not.

**No check may be graded from another check's conclusion.** A plan failing `change-is-bounded`
still gets `stranger-could-start` graded on its own evidence. Cascading one fail into the rest
turns a single reading error into six and destroys the per-check signal.

## Verdict assembly

1. Collect the seven grades.
2. Apply the rubric's verdict rule: `ready` only where every `required` check passes.
3. Handle `unclear` as the rule directs, a fail on every required check except
   `diagnosis-follows-evidence`, where an `unclear` survives if and only if `unknowns-stated`
   passed. Resolve that exception **after** both grades exist, never while grading either.
4. Report the `preferred` grade, then set it aside; it never enters the verdict.
5. Quote the deciding check. On a `hold`, that is the first required fail in execution order,
   and its evidence line goes in verbatim so the reader gets a next step rather than a label.
   On a `ready`, quote the check that came closest to failing, so the reader knows where the
   plan is thinnest.

The same grades produce the same verdict every time: nothing in this stage is a judgement
call, because every judgement was made and recorded upstream.
