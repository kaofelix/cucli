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

## Commands

### Workspaces & Spaces

```bash
cucli workspaces                                             # List all workspaces
cucli spaces <team_id>                                       # List spaces in a workspace
cucli folders <space_id>                                     # List folders in a space
cucli lists <folder_id>                                      # List lists in a folder
cucli create-folder <space_id> --name "Folder Name"        # Create a folder
cucli create-list <folder_id> --name "List Name"            # Create a list (supports --description, --markdown-description, --due-date, --due-date-time, --priority, --assignee, --status)
```

### Tasks

```bash
cucli task <task_id>                                        # Get task details (supports --md-only for description only)
cucli tasks <team_id>                                        # List tasks (filters: --status, --space-id, --list-id, --assignee, --tag, --include-closed, --page)
cucli create-task <list_id> --name "Task Name"               # Create a task (supports --description, --status, --priority, --assignee, --tag, --due-date, --start-date, --time-estimate, --points, --parent for subtasks)
cucli update-task <task_id>                                  # Update task (fields: --name, --status, --priority, --description, --markdown-description, --due-date, --start-date, --time-estimate, --points, --assignee-add, --assignee-remove, --parent)
cucli delete-task <task_id>                                  # Delete a task (prompts for confirmation unless --yes)
cucli task-members <task_id>                                 # Get members with explicit access to a task
cucli add-dependency <task_id>                               # Add dependency (use --depends-on <id> or --dependency-of <id>)
cucli delete-dependency <task_id>                            # Remove dependency (use --depends-on <id> or --dependency-of <id>)
cucli create-attachment <task_id> --file /path/to/file      # Upload a file as attachment
```

### Comments

```bash
cucli task-comments <task_id>                                # Get comments on a task
cucli add-comment <task_id> --text "Comment text"           # Add comment to task (supports --assignee, --no-notify)
cucli list-comments <list_id>                                # Get comments on a list
cucli add-list-comment <list_id> --text "Comment text"       # Add comment to list (supports --assignee, --no-notify)
```

### Checklists

```bash
cucli create-checklist <task_id> --name "Checklist Name"                      # Create a checklist
cucli create-checklist-item <checklist_id> --name "Item Name"                 # Create checklist item (supports --assignee)
cucli update-checklist <checklist_id>                                         # Update checklist (--name, --position where 0 = top)
cucli update-checklist-item <checklist_id> <checklist_item_id>                # Update checklist item (--name, --resolved, --assignee, --parent)
cucli delete-checklist <checklist_id>                                         # Delete a checklist
cucli delete-checklist-item <checklist_id> <checklist_item_id>               # Delete a checklist item
```

### Lists

```bash
cucli list-members <list_id>                                 # Get members with explicit access to a list
```

### Tags

```bash
cucli tags <space_id>                                        # List all tags in a space
cucli create-tag <space_id> --name "Tag Name" --fg-color "#000000" --bg-color "#FFFFFF"  # Create a tag
cucli add-tag <task_id> <tag_name>                           # Add a tag to a task
cucli remove-tag <task_id> <tag_name>                        # Remove a tag from a task
```

### Goals

```bash
cucli goals <team_id>                                        # List goals in a workspace (supports --include-completed)
cucli goal <goal_id>                                         # Get detailed information about a specific goal
cucli create-goal <team_id> --name "Goal Name" --due-date <timestamp>         # Create a goal (supports --start-date, --description, --multiple-owners --owner <id>, --color)
cucli update-goal <goal_id>                                   # Update goal (--name, --due-date, --description, --color, --add-owner, --remove-owner)
cucli delete-goal <goal_id>                                   # Delete a goal
cucli create-key-result <goal_id> --name "Key Result Name"    # Create a key result (--type: number|currency|boolean|percentage|automatic, --unit, --steps-start, --steps-end, --owner, --task, --list)
cucli update-key-result <key_result_id>                       # Update key result (--steps-current, --note)
cucli delete-key-result <key_result_id>                      # Delete a key result
```

### Help

```bash
cucli --help                                                  # Show global help
cucli <command> --help                                        # Show help for a specific command
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
