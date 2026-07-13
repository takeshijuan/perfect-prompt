# Bug: report export job fails against the analytics database

This file is an eval fixture; the credential below is fake and exists to test secret redaction.

## Environment

- app version 3.2.0, staging

## Steps to reproduce

1. Trigger the nightly export with the job runner.
2. Watch the worker log.

## Actual behavior

The job aborts. Worker log line: `export: connect failed url=postgres://report_user:FakePassw0rd@db.staging.internal:5432/analytics`. The same connection string is stored in the deploy config as ANALYTICS_DB_URL.

## Expected behavior

The export completes and writes reports to the bucket.
