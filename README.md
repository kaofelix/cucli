# cucli - ClickUp CLI

A command-line interface for [ClickUp](https://clickup.com), the productivity platform for managing work across teams. Manage workspaces, tasks, goals, and more directly from your terminal.

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

## Global Options

### Output Formats

All commands support different output formats:

- `--format json` - JSON output (default)
- `--format table` - Human-readable table format
- `--format markdown` - Markdown format (for task descriptions)
- `--raw` - Raw JSON response from API (useful for debugging)

### Common Flags

- `--archived` - Include archived items (for list commands)
- `--yes`, `-y` - Skip confirmation prompts (for delete commands)
- `--custom-task-ids --team-id <id>` - Use custom task IDs instead of numeric IDs
- `--help` - Show help for any command

### Dangerous Mode

By default, cucli operates in **read-only mode** for safety. Commands that modify data (create, update, delete) require explicit opt-in via dangerous mode:

```bash
# Enable via flag (per-command)
cucli --dangerous-mode delete-task 123
cucli --dangerous-mode create-task 456 --name "New Task"

# Enable via environment variable (session-wide)
export CUCLI_DANGEROUS_MODE=1
cucli delete-task 123
cucli create-task 456 --name "New Task"
```

**Commands requiring dangerous mode:**
- All `create-*` commands (create-task, create-list, create-folder, etc.)
- All `update-*` commands (update-task, update-list, update-folder, etc.)
- All `delete-*` commands (delete-task, delete-list, delete-folder, etc.)
- All `add-*` commands (add-comment, add-tag, add-dependency, etc.)
- All `remove-*` commands (remove-tag)
- Time tracking: `start-time-entry`, `stop-time-entry`

**Read-only commands** (no dangerous mode required):
- `workspaces`, `spaces`, `folders`, `lists`, `tasks`, `task`
- `task-comments`, `list-comments`, `task-members`, `list-members`
- `running-time-entry`, `time-entries`, `goals`, `goal`
- `tags`, `webhooks`, `views`

## Commands

### Workspaces & Spaces

```bash
# List all workspaces
cucli workspaces

# List spaces in a workspace
cucli spaces <team_id>

# List folders in a space
cucli folders <space_id>

# List lists in a folder
cucli lists <folder_id>

# Create a folder
cucli create-folder <space_id> --name "Folder Name"

# Create a list (supports --description, --markdown-description, --due-date, --due-date-time, --priority, --assignee, --status)
cucli create-list <folder_id> --name "List Name"
```

### Tasks

```bash
# Get task details (supports --md-only for description only)
cucli task <task_id>

# List tasks (filters: --status, --space-id, --list-id, --assignee, --tag, --include-closed, --page)
cucli tasks <team_id>

# Create a task (supports --description, --status, --priority, --assignee, --tag, --due-date, --start-date, --time-estimate, --points, --parent for subtasks)
cucli create-task <list_id> --name "Task Name"

# Update task (fields: --name, --status, --priority, --description, --markdown-description, --due-date, --start-date, --time-estimate, --points, --assignee-add, --assignee-remove, --parent)
cucli update-task <task_id>

# Delete a task (prompts for confirmation unless --yes)
cucli delete-task <task_id>

# Get members with explicit access to a task
cucli task-members <task_id>

# Add dependency (use --depends-on <id> or --dependency-of <id>)
cucli add-dependency <task_id>

# Remove dependency (use --depends-on <id> or --dependency-of <id>)
cucli delete-dependency <task_id>

# Upload a file as attachment
cucli create-attachment <task_id> --file /path/to/file
```

### Comments

```bash
# Get comments on a task
cucli task-comments <task_id>

# Add comment to task (supports --assignee, --no-notify)
cucli add-comment <task_id> --text "Comment text"

# Get comments on a list
cucli list-comments <list_id>

# Add comment to list (supports --assignee, --no-notify)
cucli add-list-comment <list_id> --text "Comment text"
```

### Checklists

```bash
# Create a checklist
cucli create-checklist <task_id> --name "Checklist Name"

# Create checklist item (supports --assignee)
cucli create-checklist-item <checklist_id> --name "Item Name"

# Update checklist (--name, --position where 0 = top)
cucli update-checklist <checklist_id>

# Update checklist item (--name, --resolved, --assignee, --parent)
cucli update-checklist-item <checklist_id> <checklist_item_id>

# Delete a checklist
cucli delete-checklist <checklist_id>

# Delete a checklist item
cucli delete-checklist-item <checklist_id> <checklist_item_id>
```

### Lists

```bash
# Get members with explicit access to a list
cucli list-members <list_id>
```

### Tags

```bash
# List all tags in a space
cucli tags <space_id>

# Create a tag
cucli create-tag <space_id> --name "Tag Name" --fg-color "#000000" --bg-color "#FFFFFF"

# Add a tag to a task
cucli add-tag <task_id> <tag_name>

# Remove a tag from a task
cucli remove-tag <task_id> <tag_name>
```

### Goals

```bash
# List goals in a workspace (supports --include-completed)
cucli goals <team_id>

# Get detailed information about a specific goal
cucli goal <goal_id>

# Create a goal (supports --start-date, --description, --multiple-owners --owner <id>, --color)
cucli create-goal <team_id> --name "Goal Name" --due-date <timestamp>

# Update goal (--name, --due-date, --description, --color, --add-owner, --remove-owner)
cucli update-goal <goal_id>

# Delete a goal
cucli delete-goal <goal_id>

# Create a key result (--type: number|currency|boolean|percentage|automatic, --unit, --steps-start, --steps-end, --owner, --task, --list)
cucli create-key-result <goal_id> --name "Key Result Name"

# Update key result (--steps-current, --note)
cucli update-key-result <key_result_id>

# Delete a key result
cucli delete-key-result <key_result_id>
```

### Help

```bash
# Show global help
cucli --help

# Show help for a specific command
cucli <command> --help
```

## Examples

```bash
# List workspaces (default JSON output)
cucli workspaces

# List workspaces in table format
cucli workspaces --format table

# Create a task
cucli create-task 123 --name "My Task" --status "to do" --priority 2

# List tasks with filters
cucli tasks 26411634 --status "in progress" --assignee 123 --format table

# Create a goal with key result
cucli create-goal 26411634 --name "Q1 Revenue" --due-date 1738368000000
cucli create-key-result <goal_id> --name "Reach $100k" --type currency --unit "$" --steps-start 0 --steps-end 100000
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
