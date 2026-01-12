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
