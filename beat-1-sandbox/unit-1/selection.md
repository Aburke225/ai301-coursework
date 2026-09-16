# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/5

**Verdict output**

```
issue-select, live mode, 3 candidates, scope codepath/pathreview-ai301-fa26-s1

ACCEPTED (ranked by fit profile)

1. #5   Add end-to-end ingestion test with a sample resume fixture
   repo-not-archived    pass   archived: no
   maintainer-active    pass   last default-branch commit 2026-08-24 by Aburke225, 21 days before today, not a bot
   repo-in-use          pass   no releases published; last push to any branch 2026-09-10, inside the 180-day push window
   scope-bounded        pass   one test module named (tests/integration/test_ingestion_pipeline.py), effort stated 4-6 hours; no umbrella or tracking language, thread empty so no unsettled design debate
   unclaimed            pass   assignees: none; linked PRs: none; 0 comments, so no claim comment of any age
   ai-policy-permits    pass   docs/CONTRIBUTING.md states no AI policy; silence passes
   newcomer-signposted  pass   no newcomer label, but opened by Aburke225 (OWNER)        [preferred]
   fit: ingestion plus test infrastructure, which is the centre of the profile rather than its
   edge. The work is reading a pipeline carefully and building the seams to exercise it, and
   the evidence is a pytest run rather than a service that has to be stood up first.

2. #13  Add an integration test that runs the full RAG pipeline against a mock LLM
   all six required checks pass; preferred pass (OWNER-filed, no newcomer label)
   fit: the same test-infrastructure shape, one layer away from the profile's stated area , 
   retrieval and generation rather than ingestion and parsing.

3. #12  Add snapshot tests for prompt templates to catch accidental changes
   all six required checks pass; preferred pass (good first issue + OWNER-filed, the
   strongest newcomer signal of the three)
   fit: ranked last despite the friendliest label. The issue asks for a policy as much as a
   test, "developers must consciously version templates", and the profile says to avoid
   changes whose resolution is a judgement call rather than a technical one.

REJECTED

(none, all three candidates passed every required check)

```
```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/5",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo line reads archived: no"},
      {"name": "maintainer-active", "grade": "pass", "evidence": "last default-branch commit 2026-08-24 by Aburke225, 21 days before today, inside the 180-day window"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "no releases; last push to any branch 2026-09-10, inside the 180-day push window"},
      {"name": "scope-bounded", "grade": "pass", "evidence": "one test module named, effort stated 4-6 hours, no umbrella or tracking language, empty thread"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; linked PRs: none; thread has 0 comments"},
      {"name": "ai-policy-permits", "grade": "pass", "evidence": "docs/CONTRIBUTING.md states no AI policy; silence passes"},
      {"name": "newcomer-signposted", "grade": "pass", "evidence": "labels: enhancement, ingestion, tests, tier-2, no newcomer label; opened by Aburke225 (OWNER)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/13",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo line reads archived: no"},
      {"name": "maintainer-active", "grade": "pass", "evidence": "last default-branch commit 2026-08-24 by Aburke225"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "last push to any branch 2026-09-10"},
      {"name": "scope-bounded", "grade": "pass", "evidence": "one test module named (tests/integration/test_rag_pipeline.py), effort stated 4-6 hours"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; linked PRs: none; 0 comments"},
      {"name": "ai-policy-permits", "grade": "pass", "evidence": "no AI policy stated in docs/CONTRIBUTING.md"},
      {"name": "newcomer-signposted", "grade": "pass", "evidence": "no newcomer label; opened by Aburke225 (OWNER)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/12",
    "checks": [
      {"name": "repo-not-archived", "grade": "pass", "evidence": "repo line reads archived: no"},
      {"name": "maintainer-active", "grade": "pass", "evidence": "last default-branch commit 2026-08-24 by Aburke225"},
      {"name": "repo-in-use", "grade": "pass", "evidence": "last push to any branch 2026-09-10"},
      {"name": "scope-bounded", "grade": "pass", "evidence": "one test module named (tests/unit/test_prompt_templates.py), effort stated 3-5 hours"},
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; linked PRs: none; 0 comments"},
      {"name": "ai-policy-permits", "grade": "pass", "evidence": "no AI policy stated in docs/CONTRIBUTING.md"},
      {"name": "newcomer-signposted", "grade": "pass", "evidence": "labels include good first issue; opened by Aburke225 (OWNER)"}
    ],
    "verdict": "accept"
  }
]
```

---

## Eval iterations

**Run history**

[TO FILL IN AFTER MY FULL RUN: the agreement score of each run in order. The last one has to match
the agreement line in the `eval-run.txt` I commit.]

**Issue analysis**

[TO FILL IN AFTER MY FULL RUN: naming one scored issue by id, what my rubric decided, what the gold
label said, and why my rubric read it that way.

I already know which one I want to write about: whichever scored issue wears a `good first
issue` label and is still a reject. That is where my `newcomer-signposted` check and my
`scope-bounded` check pull against each other hardest. I made `newcomer-signposted` preferred
precisely so a friendly label cannot rescue an issue whose body sinks it. If the harness agrees
with me, the account is about why the weight column does the work. If it disagrees, the
disagreement is the more interesting thing to write up.]

**Check rationale**

The `unclaimed` check from `tools/issue-select/rubric.md`, as it currently reads:

> All three hold: no assignee; no linked PR in the open state; and no unanswered claim comment
> ("I'll take this", "working on this") dated within 120 days of capture. A claim older than 120
> days with no open linked PR is **stale** and does not block. A closed, unmerged linked PR is an
> abandoned attempt, not a claim.

My first draft was one line: no assignee and no claim comment. That version can't tell a live
claim from a dead one, which is most of the work this check has to do.

Two things in the evidence guide pushed me off it. It describes a closed unmerged linked PR as
"an abandoned attempt", which is close to the opposite of a claim. And it warns that the sidebar
and the thread disagree sometimes, with instructions to believe the thread. So the check now
grades three surfaces separately, each with its own disqualifier, and it puts a date on the
comment surface instead of treating any claim as permanent.

**Trade-offs**

[TO FILL IN AFTER MY FULL RUN: an issue whose result this check changes, or a canary re-run with
`--only`.]

What I can say before running anything: the 120-day window is the trade. It lets a stale claim
through, which is what I want, because an issue nobody has touched in four months is open in
practice no matter what the thread says. The cost is that it can't see a claim that's 130 days
old and still live on a slow repo where four months of quiet is normal. I'll take that miss.

The alternative I looked at was scaling the window to the repo's own response latency. I dropped
it because it makes one check depend on another check's evidence, and then every disagreement
takes twice as long to read.

---

## Selection rationale

**Selection rationale**

**Fit and time.** Backend Python in the ingestion path, and what it produces is test
infrastructure. Both are things I said I wanted. The whole thing is reachable from a pytest run,
because the pipeline takes its vector database, its database session, and its embedding provider
as constructor arguments. Nothing has to be stood up before I can see the problem. The issue
estimates 4 to 6 hours, which I can finish inside a unit and still write the reflection properly
instead of at midnight.

**What the verdict got right, and what I weighed that it couldn't.** The rubric had the
mechanical facts right: nobody is on it, the repo is alive, the scope is one named module. Two
things it couldn't see.

The first is a ranking problem I created myself. #5 is tier-2 with no `good first issue` label.
#12 is tier-1 with one. My `newcomer-signposted` check sees that difference and #5 still came out
on top, because the check is preferred and the fit profile drives the order. I think that's
right, but I want to be honest that it's a choice and not a finding. I picked the
less-signposted issue because it sits where I want to work.

The second one bothers me more. The issue's premise isn't true. It says to use "the fixtures in
`tests/fixtures/sample_resumes/`", and that directory isn't in the repo. `tests/integration/`
holds one empty `__init__.py` and there are no resume fixtures anywhere. So the work is bigger
than the issue describes: the fixtures have to exist before the test it asks for can be written.

I only know that because I cloned the repo and looked. Every check I wrote reads the issue text
and the repo-facts block. None of them reads the tree. A false premise in an issue body is
invisible to my tool, and that's the biggest gap I've found in it so far.

**Anticipated difficulty in claiming it.** Low on contest, real on framing. It's unassigned with
an empty thread, in a classroom repo whose house rule says a classmate's claim doesn't block me,
so nobody is racing me for it.

The hard part is the writing. My claim has to say the issue is wrong about its own fixtures
without sounding like I'm scoring a point off whoever filed it. Then my plan has to stay bounded
anyway, instead of treating a missing directory as permission to reorganise the test tree.
