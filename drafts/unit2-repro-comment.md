Confirmed the gap. The issue's description of it is slightly off, in a way worth sorting out
before anyone starts writing.

**Environment**

- OS: macOS 26.6.2 (Darwin 25.6.0), arm64
- Under test: `codepath/pathreview-ai301-fa26-s1` @ `main`, commit `996fabe`, checked out 2026-09-14
- Interpreter: Python 3.11.16 in a venv, per `requires-python = ">=3.11"` in `pyproject.toml`

**The gap, four ways**

```console
$ pytest tests/integration -q

no tests ran in 0.00s

$ ls tests/integration/
__init__.py

$ grep -rl "IngestionPipeline\|ingest_resume" tests/
(no output)

$ ls tests/fixtures/sample_resumes/
ls: tests/fixtures/sample_resumes/: No such file or directory
```

The integration package exists but holds nothing except its `__init__.py`. No test anywhere
mentions the pipeline. And the whole `tests/fixtures/` tree is absent.

**The premise worth correcting.** The issue says to add a test "using the fixtures in
`tests/fixtures/sample_resumes/`". Those fixtures aren't in the repo, so they have to be created
as part of this. I'm flagging it rather than absorbing it quietly, because it changes how big the
issue is.

There's also an alternative someone may have had in mind: `tests/conftest.py` already provides a
`sample_resume_text` fixture as an inline string. If you'd rather the test build on that than on
a new file on disk, say so and I'll go that way. My default is to create the directory the issue
names, because "from file upload through embedding storage" reads to me like the file on disk is
part of what's being tested.

**What the pipeline gives us to work with**, since it changes how much of this needs real
services:

```console
$ python -c "
from ingestion.pipeline import IngestionPipeline
print([m for m in dir(IngestionPipeline) if m.startswith('ingest_')])
"
['ingest_readme', 'ingest_repo_metadata', 'ingest_resume']
```

`IngestionPipeline.__init__` takes `vector_db`, `db_session`, and `embedding_provider` as
arguments, and the repo already ships a `MockEmbeddingProvider` in
`ingestion/embeddings/provider.py`. So the full parse, chunk, embed, store path can run against
in-memory doubles at those two seams, with production code everywhere in between, and no
ChromaDB or Postgres needed to see it work.

One thing for whoever reviews this. `pyproject.toml` describes the `integration` marker as
"require Docker services". A test built this way doesn't, so either the marker's description or
my use of it needs a decision. I'll raise it again with the plan rather than guess now.

AI-assisted work, per AI301.
