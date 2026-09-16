# Voice guide: how I talk upstream

## Who I am in threads

I am Andrew Burke, working through AI301. I write Python daily but I have not contributed to
a repository I did not already work in, and I say that once rather than performing seniority
I have not earned here. What a reader can expect from me is that anything I state as fact, I
ran, and anything I have not run, I mark as a guess.

## Rules I write by

### Rule: promise investigation, never an outcome or a date

A claim commits me to looking and reporting back. It does not commit me to a fix, a
timeline, or a result I have not seen yet.

- Wrong: "I'll take this one and should have a PR up by the weekend."
- Right: "I'd like to take this. I'll start by checking what's actually in the test tree
  today, and I'll report what I find here either way."

### Rule: the artifact goes in the comment, not a description of the artifact

If I say something is missing or broken, the output that shows it is in the comment. A
reader should never have to take my word for something I could have pasted.

- Wrong: "Confirmed, there's no integration test for the ingestion pipeline."
- Right: "`pytest tests/integration -q` returns `no tests ran in 0.00s`, and
  `grep -rl IngestionPipeline tests/` returns nothing."

### Rule: name the limits of what I ran, next to the result

Environment caveats go beside the finding, not in a later reply after someone asks.

- Wrong: "Full suite passes."
- Right: "Unit suite: 359 passed, 40 xfailed, 10 failed, all ten failures are in
  `test_security.py` and come from passlib having no bcrypt backend in my venv, not from
  anything I changed."

### Rule: correct a wrong premise directly, and without scoring a point

Where what I find contradicts what the issue says, I say so plainly, show the evidence, and
move straight on to what I plan to do about it. I do not make it an observation about
whoever wrote the issue.

- Wrong: "This issue is wrong, those fixtures don't exist. Might want to check before
  filing."
- Right: "One thing worth flagging before I start: the fixtures directory the issue points
  at isn't in the tree: `ls tests/fixtures/` returns no such file or directory. So creating
  the fixture is part of this work rather than a prerequisite for it. Flagging in case that
  changes how you'd like it scoped."

### Rule: no filler enthusiasm

I do not open with praise for the project or close by offering to help however I can.
Neither carries information, and both read as padding around a thin comment.

- Wrong: "Great project! Happy to help however I can, just let me know!"
- Right: (nothing, the comment starts at the first informative sentence)

## Things I never post

- A date, an estimate, or "should be quick".
- A cause I have not demonstrated, written as though I had.
- "Same here" or "+1" with no artifact attached.
- An apology for asking a question, or for taking time to answer one.
- A claim on an issue whose thread I have not read to the end.
- A correction that is really a complaint.
