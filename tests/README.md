# Tests

This directory contains tests for the cucli project using pytest and pytest-recording.

## Setup

Install test dependencies:

```bash
uv sync --extra test
```

## Running Tests

Run all tests:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

Run specific test file:

```bash
uv run pytest tests/test_api.py
```

Run specific test:

```bash
uv run pytest tests/test_api.py::TestClickUpClient::test_init_with_api_key
```

Run tests matching a pattern:

```bash
uv run pytest -k "test_get_teams"
```

## VCR Recording

Tests are written using [pytest-recording](https://github.com/kiwicom/pytest-recording) which uses [VCR.py](https://vcrpy.readthedocs.io/) to record and replay HTTP interactions.

### How it works

1. When a test marked with `@pytest.mark.vcr` runs for the first time:
   - The actual HTTP request is made to the ClickUp API
   - The request and response are saved to a YAML "cassette" file in `tests/cassettes/`
   - Subsequent test runs will replay from the cassette instead of making real HTTP requests

2. To re-record a cassette, delete it and run the test again

### Cassettes location

Cassette files are stored in `tests/cassettes/` and are named based on the test path:
- `tests/test_api.py::TestClickUpClient::test_get_teams` → `tests/cassettes/test_api/TestClickUpClient/test_get_teams.yaml`

### Recording new cassettes

To record new cassettes:

1. Make sure you have a valid ClickUp API key:
   ```bash
   export CLICKUP_API_KEY=pk_your_actual_api_key_here
   ```

2. Run the tests that need new recordings:
   ```bash
   uv run pytest -v
   ```

3. New cassette files will be created in `tests/cassettes/`

### Re-recording existing cassettes

To update an existing cassette:

1. Delete the cassette file:
   ```bash
   rm tests/cassettes/test_api/TestClickUpClient/test_get_teams.yaml
   ```

2. Run the test again with your real API key:
   ```bash
   uv run pytest tests/test_api.py::TestClickUpClient::test_get_teams -v
   ```

### Running tests without network

Once cassettes are recorded, tests can run without any network connection or API key:

```bash
# Without setting CLICKUP_API_KEY
uv run pytest
```

### VCR configuration

The VCR configuration can be customized in `pytest.ini` or `pyproject.toml`. Current settings in `pyproject.toml`:

- Cassettes are stored in `tests/cassettes/`
- Tests are marked with `@pytest.mark.vcr` for recording
- By default, VCR will match on method, URI, and query parameters

## Test structure

- `conftest.py` - Shared pytest fixtures
- `test_api.py` - Tests for the ClickUp API client
- `test_cli.py` - Tests for CLI commands
- `test_models.py` - Tests for Pydantic models

## CI/CD

In CI/CD environments, tests should run without any network access since cassettes are committed to the repository. This ensures:
- Fast test execution
- No dependency on external API availability
- Consistent test results across environments
