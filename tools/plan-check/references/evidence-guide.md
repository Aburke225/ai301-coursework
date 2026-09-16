# Evidence guide: what good looks like in a plan package

## An account that follows the evidence

Passing shape: what the plan says is wrong or missing is what the evidence showed, and the
plan points at the line of evidence that establishes it.

The failure this file exists to catch is the confident wrong account. It rarely looks sloppy
,  usually it is the most thorough plan in the set, because someone who has decided on a cause
explains it at length. The tell is never the prose. It is a fact sitting in the package that
the plan never addresses:

- a control run showing the named component behaving correctly
- a maintainer in the thread naming a different layer
- an artifact whose traceback never enters the file the plan blames
- a search result showing the thing the issue claimed exists does not

Read the evidence for what it *rules out* and write that list down before reading the plan.
An account contradicting that list fails, however well argued.

**For a gap rather than a bug**, the same rule with a different object: the thing the plan
says is missing must be the thing the evidence showed missing. Where the evidence found the
issue's own premise wrong, a fixtures directory that is not there, a plan that quietly
plans around it has not followed the evidence, and a plan that names the correction has.

## A bounded change

The scope pair is the tool: what is in, what is explicitly not. A plan with only an "in" half
has bounded nothing.

Deferral is bounding, and this is the distinction that matters most:

- **Scoped down** (passes): "Cover the markdown path end to end. Not in scope: the PDF
  branch, which needs a binary fixture and a decision about where it lives."
- **Crept** (fails): one missing integration test becomes a test-tree reorganisation, a
  conftest refactor, and a marker taxonomy.

Count the behaviours the plan touches. One, or one plus explicit deferrals, passes. Two
unrelated behaviours with no deferral note is creep, however small the second one is.

Adding a file the issue did not mention is not automatically creep. Where the evidence showed
that file has to exist before the requested work is possible, it is part of the one change , 
provided the plan says so rather than letting it appear in the diff unannounced.

## A plan a stranger could start

The test is the first implementation step: it should name a thing, not an activity.

- Startable: "Create `tests/fixtures/sample_resumes/jane_doe.md` containing a markdown resume
  with the section headers `ResumeParser.SECTION_HEADERS` recognises."
- Not startable: "Work out what fixtures are needed and add them." / "Investigate the
  ingestion path and add appropriate coverage."

The second shape is the most common failure: a plan that has chosen to investigate rather than
chosen an approach. Investigation is legitimate work; it is not a plan to build from.

## An observable test plan

Name the command, the test id, or the measurement, and the expected-after:

    pytest tests/integration -q
    expected after: 9 passed  (before: "no tests ran in 0.00s")

Not observable: "add tests", "verify it works", "make sure nothing breaks".

Where the unit-2 evidence was a gap demonstration, the test plan re-runs the same searches
with the opposite expected result. The symmetry is the point: the command that proved the
absence is the command that proves it is gone.

## Respecting the thread

Read every maintainer comment before grading the plan comment. Three things bind: an approach
named (build on it or say why not), an approach ruled out (proposing it anyway fails), and a
direct question (answer it).

A quiet thread binds nothing. Silence is not direction, and a plan on a silent issue is held
to the repo's stated conventions only.

Where my own earlier comment raised a question the maintainer has not answered, the plan
comment says what I am doing in the absence of an answer, and stays reversible.

## Stated unknowns

An honest "nothing outstanding, and here is why" passes in full. An empty section fails. The
section exists so the gap between what the plan knows and what it assumes sits on the page
rather than in the writer's head.
