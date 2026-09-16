# Sample resume fixtures

Fixture documents used by `tests/integration/test_ingestion_pipeline.py`.

Each file is a synthetic resume written for testing. They contain no real personal data:
names, contact details, employers, and dates are invented.

- `jane_doe.md`, a complete markdown resume exercising every section header the
  `ResumeParser` recognises (summary, experience, education, skills, projects).

Add new fixtures here when a test needs a resume shape these do not cover, and describe
the shape in this file so the next person knows what each fixture is for.
