# Bug: config parser rejects nested blocks

## Environment

- app version 2.9.0, staging

## Steps to reproduce

1. Save the following snippet as config.yml and start the app.

```yaml
server:
  port: 8080
```

2. Observe startup failure.

## Actual behavior

Startup aborts with `config_parser: unexpected block at line 2`.

## Expected behavior

The nested block parses and the server starts on port 8080.
