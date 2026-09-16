# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

---

## Your pull request

**Pull request**

[LINK TO MY PULL REQUEST AGAINST codepath/pathreview-ai301-fa26-s1, once it is opened]

**Branch**

`feat/5-ingestion-e2e-test`

## Eval iterations

**Run history**

[TO FILL IN AFTER MY FULL RUN: each run's agreement score in order. The last has to match the
agreement line in the committed `eval-run.txt`.]

**Package analysis**

[TO FILL IN AFTER MY FULL RUN: naming one scored package, what my rubric decided, what the gold label
said, and why my rubric read it that way.

The shape I most want to test my rubric against is the package that's right on the engineering
and still a reject: a solid fix with real evidence that ignores the repo's stated template or
disclosure ask. Everything a code reviewer cares about passes it, and only `standards-met` holds
it. That's also the case my own PR is most at risk from, which is why I named each unrun check
individually in the description instead of gesturing at "some checks".]

**Check rationale**

The `evidence-shows-before-and-after` check from `tools/pr-precheck/rubric.md`, as it currently
reads:

> The evidence shows the issue's subject observably changing: a before and an after, through the
> real code path, with commands and their output present. For an issue asking for something
> absent, the before is the search that found nothing and the after is the same search finding it.
> Fails on assertion in place of evidence, "tested locally", "verified working", "all tests pass"
> with nothing shown, and where the evidence exercises a path the change did not touch. **An
> honestly reported failing or unrun check passes this check** where the reason is stated; a
> hidden failure does not.

Three revisions are in that wording, and all three came from packages that would otherwise have
graded wrong.

The first draft said "the evidence demonstrates the fix works", which is exactly the adjective
the CONTRACT warns about. The lecture calls this family *not tested*, and "demonstrates" gives an
executor no rule at all. Naming the failing shapes in the check's own words replaced a judgement
with a match.

The second sentence is the one my own issue forced, the same way it forced the gap check in unit
2. A test-shaped issue has no behaviour to run before the change, so "before and after" in the
ordinary sense doesn't exist. What does exist is a command whose *result* changes while the
command stays identical: `pytest tests/integration -q` moving from `no tests ran in 0.00s` to `9
passed`. Without that sentence my own PR's evidence would have graded `unclear` on the check
it's strongest on.

The bolded sentence is the one I lean on hardest. I couldn't run the linter or the type checker,
and ten unit tests fail for a missing bcrypt backend. A check that failed every package with an
unrun repo check would fail my own PR for being honest about a real constraint. Stating the
reason is the line between an honest gap and a hidden failure, and the check now says so instead
of leaving it to the grader's charity.

**Trade-offs**

What the honest-gap clause can't do is separate a real constraint from a convenient excuse. "Not run: no bcrypt
backend in my venv" and "not run: I didn't get to it" are both reasons, and this check takes
both. A stricter version would demand the reason be load-bearing, that the check genuinely
couldn't run rather than merely didn't, and I dropped that deliberately. Deciding whether
someone's stated obstacle is real is the plausibility judgement the CONTRACT's "grade the thing,
not the polish" rule exists to keep out of the rubric, and two executors wouldn't call it the
same way twice.

In practice that costs less than it sounds like, because `repo-checks-run` catches most of what
slips through.
That check requires each unrun check to be **named**, so a vague wave at "some checks didn't run"
fails there even where the reason clause would have let it past. The two cover each other. One
asks whether the reason exists, the other asks whether the gap was itemised.

My own description is written to satisfy both, with every unrun check listed individually and its
own cause beside it. Writing it that way is when I understood why the two checks needed to stay
separate instead of merging into one.

There's a second trade in the same clause, read from the other side. A package can pass this
check while its *most important* check went unrun. My rubric doesn't weight checks by importance,
because "which check mattered most" is a per-repo judgement I can't state as a general rule.

[TO FILL IN AFTER MY FULL RUN: whichever the run supports: a package whose result the honest-gap
clause changes, or a canary confirming it moved nothing it shouldn't have.]

---

Related paths: `eval-run.txt` in this directory; the tool's files in `tools/pr-precheck/`.
