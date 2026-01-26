# cucli - ClickUp CLI

A command-line interface for ClickUp.

## Installation

```bash
uv install
```

## Setup

Set your ClickUp API key as an environment variable:

```bash
export CLICKUP_API_KEY=pk_your_api_key_here
```

Or add it to your `.env` file (if you use a tool like `direnv`):

```
CLICKUP_API_KEY=pk_your_api_key_here
```

## Usage

### List workspaces

```bash
cucli workspaces
```

Output in JSON format (default):

```json
[
  {
    "id": "26411634",
    "name": "Liveheats",
    "color": "#02bcd4"
  }
]
```

Output in table format:

```bash
cucli workspaces --format table
```

```
ID        NAME       COLOR
------------------------------
26411634  Liveheats  #02bcd4
```

Output raw JSON (useful for debugging or when models don't match):

```bash
cucli workspaces --raw
```

### Get task details

```bash
cucli task <task_id>
```

Output in different formats:

```bash
# JSON (default)
cucli task 86abc123

# Table format
cucli task 86abc123 --format table

# Markdown format (description only)
cucli task 86abc123 --format markdown

# Markdown description only (useful for piping to other tools)
cucli task 86abc123 --md-only
```

Get raw JSON response:

```bash
cucli task 86abc123 --raw
```

### Get help

```bash
cucli --help
cucli workspaces --help
```

## Development

Add a dependency:

```bash
uv add <package>
```

Run the CLI:

```bash
uv run cucli <command>
```

## Testing

Install test dependencies:

```bash
uv sync --extra test
```

Run all tests:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

### VCR Recording

Tests use [pytest-recording](https://github.com/kiwicom/pytest-recording) with [VCR.py](https://vcrpy.readthedocs.io/) to record and replay HTTP interactions. This means tests can run without making actual API calls after the first recording.

To record new cassettes:

```bash
export CLICKUP_API_KEY=pk_your_actual_api_key_here
uv run pytest
```

Cassettes are stored in `tests/cassettes/` and should be committed to the repository.

See [tests/README.md](tests/README.md) for more details.
