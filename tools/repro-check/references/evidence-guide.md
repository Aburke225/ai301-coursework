# Evidence guide: what good looks like in a reproduction package

The rubric names the checks; this file says what a passing answer looks like, so a check
stays decidable by someone who is not me.

## The environment record

Passing shape: three lines, each naming something a reader can return to:

    OS: macOS 26.6.2 (Darwin 25.6.0), arm64
    Under test: codepath/pathreview-ai301-fa26-s1 @ main, commit 996fabe, 2026-09-14
    Interpreter: Python 3.11.16 (venv), per the project's requires-python = ">=3.11"

What fails: "latest", "current main", "my dev box", or a version for the project but none
for the dependency the behaviour actually routes through.

A dependency version is owed only where the behaviour runs through that dependency. A gap in
the project's own test tree needs no third-party version at all.

## Steps a stranger can re-run

The test is closure, not length: can a reader holding the public repo and nothing else reach
the same state? Inline the fixture or link it publicly. Commands go in as run.

Complete and terse beats complete and long. Three lines carrying setup, command, and input
are a better report than a page that mentions a config file nobody else has.

Fails on closure every time: a private repo, an unshared `.env`, a database whose contents
are never described.

## The artifact, read against the issue

Mechanical, three steps:

1. Write down what the **issue** describes, the error, the code path, the missing thing.
2. Write down what the **artifact** shows.
3. They must be the same subject.

Known ways they come apart: a different error in an adjacent path; a failure the reporter's
own edit caused; a run against a version the issue does not concern; and proof of life
(a version banner, a server starting) offered as proof of the problem.

## Showing a gap, when the issue asks for something that does not exist

Most of this course's failure modes assume a bug with behaviour to run. An issue asking for
a test, a feature, or docs has no behaviour yet, and "reproducing" it means **showing the
absence** rather than asserting it. The absence is still demonstrable, and the demonstration
is still an artifact:

- The suite that collects nothing: `pytest tests/integration -q` → `no tests ran in 0.00s`
- The path that is not there: `ls tests/fixtures/sample_resumes/` → `No such file or directory`
- The search that comes back empty: `grep -rl IngestionPipeline tests/` → no output
- The example in the docs that errors when pasted into a shell

What fails here is the assertion with no search behind it: "there's no integration test" with
nothing showing that anyone looked. An issue with no behaviour to run still gets evidence,
never a blank.

A second thing worth capturing while showing a gap: whether the issue's own description of
the gap is accurate. An issue that points at a directory which does not exist is telling you
the work is bigger than it thinks, and that belongs in the report rather than in a surprise
three days later.

## The honest outcome

Two results pass:

- **Reproduced / gap shown**, with an artifact demonstrating it.
- **Could not reproduce**, with a real attempt recorded: environment, steps tried, and what
  happened instead. Full credit, and a genuinely useful comment: it tells the maintainer the
  behaviour is conditional on something not yet captured.

One result fails: a conclusion the artifact does not support. That includes a confident
diagnosis with nothing demonstrating it, which is the most seductive failure of the set
because it reads as the most expert.

## The repo's own asks

Read the contribution policy for two things: whether AI assistance is banned outright (a
wall, stop), and whether it must be disclosed (a term: comply, in my own words). Silence is
the common case and asks nothing. Where nothing is stated, the course's practice applies: the
work is AI-assisted by design, and I say so where the repo gives me a place to say it.
