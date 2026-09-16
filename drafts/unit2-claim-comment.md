I'd like to take this one.

First step is to find out what the test tree actually holds today: whether `tests/integration/`
has anything in it, and whether anything currently touches `IngestionPipeline.ingest_resume`
end to end. I'll post what I find either way.

One thing I want to check before I write any of it. The issue points at fixtures in
`tests/fixtures/sample_resumes/`, and a first look at the tree suggests that directory might
not be there. If it isn't, creating the fixture is part of this work rather than something I
inherit, and I'd rather establish that in the open than quietly widen the scope on my own.

Working on this as part of AI301, so the work is AI-assisted. I'll note that on the PR too.
