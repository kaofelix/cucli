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

### List spaces in a workspace

```bash
cucli spaces <team_id>
```

Output in JSON format (default):

```json
[
  {
    "id": "90159451300",
    "name": "Team Space",
    "private": false,
    "archived": false
  }
]
```

Output in table format:

```bash
cucli spaces <team_id> --format table
```

```
ID           NAME        PRIVATE
----------------------------------------
90159451300  Team Space  No
```

Include archived spaces:

```bash
cucli spaces <team_id> --archived
```

Output raw JSON:

```bash
cucli spaces <team_id> --raw
```

### List folders in a space

```bash
cucli folders <space_id>
```

Output in JSON format (default):

```json
[
  {
    "id": "457",
    "name": "Updated Folder Name",
    "hidden": false,
    "task_count": "0"
  }
]
```

Output in table format:

```bash
cucli folders <space_id> --format table
```

```
ID      NAME                TASKS  HIDDEN
----------------------------------------
457     Updated Folder Name  0       No
```

Include archived folders:

```bash
cucli folders <space_id> --archived
```

Output raw JSON:

```bash
cucli folders <space_id> --raw
```

### List lists in a folder

```bash
cucli lists <folder_id>
```

Output in JSON format (default):

```json
[
  {
    "id": "124",
    "name": "Updated List Name",
    "archived": false,
    "task_count": "0"
  }
]
```

Output in table format:

```bash
cucli lists <folder_id> --format table
```

```
ID      NAME                TASKS  ARCHIVED
----------------------------------------
124     Updated List Name   0       No
```

Include archived lists:

```bash
cucli lists <folder_id> --archived
```

Output raw JSON:

```bash
cucli lists <folder_id> --raw
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

### List tasks

```bash
cucli tasks <team_id>
```

List tasks with filters:

```bash
# Filter by status
cucli tasks <team_id> --status "to do" --status "in progress"

# Filter by space
cucli tasks <team_id> --space-id <space_id>

# Filter by list
cucli tasks <team_id> --list-id <list_id>

# Filter by assignee
cucli tasks <team_id> --assignee <assignee_id>

# Filter by tag
cucli tasks <team_id> --tag <tag_name>

# Include closed tasks
cucli tasks <team_id> --include-closed
```

Pagination:

```bash
# Get second page
cucli tasks <team_id> --page 1
```

Output formats:

```bash
# JSON (default)
cucli tasks <team_id>

# Table format
cucli tasks <team_id> --format table

# Raw JSON (useful for debugging or when models don't match)
cucli tasks <team_id> --raw
```

### Create task

```bash
cucli create-task <list_id> --name "Task Name"
```

Create task with additional options:

```bash
# With description
cucli create-task <list_id> --name "Task Name" --description "Task description"

# With status
cucli create-task <list_id> --name "Task Name" --status "to do"

# With priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None)
cucli create-task <list_id> --name "Task Name" --priority 3

# With assignees
cucli create-task <list_id> --name "Task Name" --assignee 123 --assignee 456

# With tags
cucli create-task <list_id> --name "Task Name" --tag "tag1" --tag "tag2"

# With due date (Unix timestamp in milliseconds)
cucli create-task <list_id> --name "Task Name" --due-date 1737907200000

# With start date (Unix timestamp in milliseconds)
cucli create-task <list_id> --name "Task Name" --start-date 1737820800000

# With time estimate (milliseconds)
cucli create-task <list_id> --name "Task Name" --time-estimate 3600000

# With sprint points
cucli create-task <list_id> --name "Task Name" --points 5

# As a subtask
cucli create-task <list_id> --name "Subtask Name" --parent <parent_task_id>
```

Output in different formats:

```bash
# JSON (default)
cucli create-task <list_id> --name "Task Name"

# Table format
cucli create-task <list_id> --name "Task Name" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli create-task <list_id> --name "Task Name" --raw
```

### Update task

```bash
cucli update-task <task_id> --name "Updated Name"
```

Update task with various options:

```bash
# Update name
cucli update-task <task_id> --name "New Name"

# Update status
cucli update-task <task_id> --status "in review"

# Update priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None)
cucli update-task <task_id> --priority 1

# Update description
cucli update-task <task_id> --description "New description"

# Update markdown description
cucli update-task <task_id> --markdown-description "# New Description"

# Update due date
cucli update-task <task_id> --due-date 1737907200000

# Update start date
cucli update-task <task_id> --start-date 1737820800000

# Update time estimate
cucli update-task <task_id> --time-estimate 7200000

# Update points
cucli update-task <task_id> --points 8

# Add assignees
cucli update-task <task_id> --assignee-add 123 --assignee-add 456

# Remove assignees
cucli update-task <task_id> --assignee-remove 789

# Update parent (move to new parent)
cucli update-task <task_id> --parent <new_parent_id>
```

Output in different formats:

```bash
# JSON (default)
cucli update-task <task_id> --name "New Name"

# Table format
cucli update-task <task_id> --name "New Name" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli update-task <task_id> --name "New Name" --raw
```

### Delete task

```bash
cucli delete-task <task_id>
```

Delete with confirmation prompt (default):

```bash
cucli delete-task <task_id>
# You will be prompted to confirm: "Are you sure you want to delete task <task_id>?"
```

Skip confirmation prompt:

```bash
cucli delete-task <task_id> --yes
# or
cucli delete-task <task_id> -y
```

### Get task comments

```bash
cucli task-comments <task_id>
```

Output in JSON format (default):

```json
[
  {
    "id": "90150188973520",
    "text": "This is a comment",
    "user": "john.doe",
    "resolved": false,
    "date": "1234567890123"
  }
]
```

Output in table format:

```bash
cucli task-comments <task_id> --format table
```

```
ID              USER        TEXT                           RESOLVED
------------------------------------------------------------------------
90150188973520  john.doe    This is a comment              No
```

Output raw JSON:

```bash
cucli task-comments <task_id> --raw
```

### Add comment to task

```bash
cucli add-comment <task_id> --text "Comment text"
```

Add comment with additional options:

```bash
# With assignee
cucli add-comment <task_id> --text "Comment text" --assignee 123

# Don't notify everyone
cucli add-comment <task_id> --text "Comment text" --no-notify
```

Output in different formats:

```bash
# JSON (default)
cucli add-comment <task_id> --text "Comment text"

# Table format
cucli add-comment <task_id> --text "Comment text" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli add-comment <task_id> --text "Comment text" --raw
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
