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

### Create folder

```bash
cucli create-folder <space_id> --name "Folder Name"
```

Output in different formats:

```bash
# JSON (default)
cucli create-folder <space_id> --name "New Folder"

# Table format
cucli create-folder <space_id> --name "New Folder" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli create-folder <space_id> --name "New Folder" --raw
```

### Create list

```bash
cucli create-list <folder_id> --name "List Name"
```

Create list with additional options:

```bash
# With description
cucli create-list <folder_id> --name "List Name" --description "List description"

# With markdown description
cucli create-list <folder_id> --name "List Name" --markdown-description "# List Description"

# With due date (Unix timestamp in milliseconds)
cucli create-list <folder_id> --name "List Name" --due-date 1737907200000

# With due date including time
cucli create-list <folder_id> --name "List Name" --due-date 1737907200000 --due-date-time

# With priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None)
cucli create-list <folder_id> --name "List Name" --priority 2

# With assignee
cucli create-list <folder_id> --name "List Name" --assignee 123

# With status (color)
cucli create-list <folder_id> --name "List Name" --status "red"
```

Output in different formats:

```bash
# JSON (default)
cucli create-list <folder_id> --name "New List"

# Table format
cucli create-list <folder_id> --name "New List" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli create-list <folder_id> --name "New List" --raw
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

### Create checklist

```bash
cucli create-checklist <task_id> --name "Checklist Name"
```

Output in different formats:

```bash
# JSON (default)
cucli create-checklist <task_id> --name "My Checklist"

# Table format
cucli create-checklist <task_id> --name "My Checklist" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli create-checklist <task_id> --name "My Checklist" --raw
```

### Create checklist item

```bash
cucli create-checklist-item <checklist_id> --name "Item Name"
```

Create checklist item with assignee:

```bash
cucli create-checklist-item <checklist_id> --name "Item Name" --assignee 123
```

Output in different formats:

```bash
# JSON (default)
cucli create-checklist-item <checklist_id> --name "My Item"

# Table format
cucli create-checklist-item <checklist_id> --name "My Item" --format table

# Raw JSON
cucli create-checklist-item <checklist_id> --name "My Item" --raw
```

### Update checklist

```bash
cucli update-checklist <checklist_id> --name "Updated Name"
```

Reorder checklist (position 0 = top):

```bash
cucli update-checklist <checklist_id> --position 0
```

Output in different formats:

```bash
# JSON (default)
cucli update-checklist <checklist_id> --name "Updated Name"

# Table format
cucli update-checklist <checklist_id> --name "Updated Name" --format table

# Raw JSON
cucli update-checklist <checklist_id> --name "Updated Name" --raw
```

### Update checklist item

```bash
cucli update-checklist-item <checklist_id> <checklist_item_id> --name "Updated Item"
```

Mark checklist item as resolved (completed):

```bash
cucli update-checklist-item <checklist_id> <checklist_item_id> --resolved true
```

Mark checklist item as unresolved:

```bash
cucli update-checklist-item <checklist_id> <checklist_item_id> --resolved false
```

Set assignee:

```bash
cucli update-checklist-item <checklist_id> <checklist_item_id> --assignee 123
```

Nest checklist item under another item:

```bash
cucli update-checklist-item <checklist_id> <checklist_item_id> --parent <parent_item_id>
```

Output in different formats:

```bash
# JSON (default)
cucli update-checklist-item <checklist_id> <checklist_item_id> --name "Updated Item"

# Table format
cucli update-checklist-item <checklist_id> <checklist_item_id> --name "Updated Item" --format table

# Raw JSON
cucli update-checklist-item <checklist_id> <checklist_item_id> --name "Updated Item" --raw
```

### Delete checklist

```bash
cucli delete-checklist <checklist_id>
```

Delete with confirmation prompt (default):

```bash
cucli delete-checklist <checklist_id>
# You will be prompted to confirm: "Are you sure you want to delete checklist <checklist_id>?"
```

Skip confirmation prompt:

```bash
cucli delete-checklist <checklist_id> --yes
# or
cucli delete-checklist <checklist_id> -y
```

### Delete checklist item

```bash
cucli delete-checklist-item <checklist_id> <checklist_item_id>
```

Delete with confirmation prompt (default):

```bash
cucli delete-checklist-item <checklist_id> <checklist_item_id>
# You will be prompted to confirm: "Are you sure you want to delete checklist item <checklist_item_id>?"
```

Skip confirmation prompt:

```bash
cucli delete-checklist-item <checklist_id> <checklist_item_id> --yes
# or
cucli delete-checklist-item <checklist_id> <checklist_item_id> -y
```

### Get task members

```bash
cucli task-members <task_id>
```

Get members with explicit access to a task. Note that this does not include people with access through a Team, or people with access from the List, Folder, or Space where the task exists.

Output in JSON format (default):

```json
[
  {
    "id": 272627274,
    "username": "Kao Cardoso Félix",
    "email": "me@kaofelix.dev",
    "initials": "KF"
  }
]
```

Output in table format:

```bash
cucli task-members <task_id> --format table
```

```
ID           USERNAME              EMAIL
-------------------------------------------------
272627274   Kao Cardoso Félix    me@kaofelix.dev
```

Output raw JSON:

```bash
cucli task-members <task_id> --raw
```

### Get list members

```bash
cucli list-members <list_id>
```

Get members with explicit access to a list. Note that this does not include people with access through a Team, or people with access from the Folder or Space where the list exists.

Output in JSON format (default):

```json
[
  {
    "id": 272627274,
    "username": "Kao Cardoso Félix",
    "email": "me@kaofelix.dev",
    "initials": "KF"
  }
]
```

Output in table format:

```bash
cucli list-members <list_id> --format table
```

```
ID           USERNAME              EMAIL
-------------------------------------------------
272627274   Kao Cardoso Félix    me@kaofelix.dev
```

Output raw JSON:

```bash
cucli list-members <list_id> --raw
```

### List tags in a space

```bash
cucli tags <space_id>
```

Output in JSON format (default):

```json
[
  {
    "name": "test-tag",
    "foreground_color": "#622aea",
    "background_color": "#622aea"
  }
]
```

Output in table format:

```bash
cucli tags <space_id> --format table
```

```
NAME        FG COLOR    BG COLOR
----------------------------------------
test-tag    #622aea    #622aea
```

Output raw JSON:

```bash
cucli tags <space_id> --raw
```

### Create tag

```bash
cucli create-tag <space_id> --name "Tag Name" --fg-color "#000000" --bg-color "#FFFFFF"
```

Output in different formats:

```bash
# JSON (default)
cucli create-tag <space_id> --name "New Tag" --fg-color "#000000" --bg-color "#FFFFFF"

# Table format
cucli create-tag <space_id> --name "New Tag" --fg-color "#000000" --bg-color "#FFFFFF" --format table

# Raw JSON (useful for debugging or when models don't match)
cucli create-tag <space_id> --name "New Tag" --fg-color "#000000" --bg-color "#FFFFFF" --raw
```

### Add tag to task

```bash
cucli add-tag <task_id> <tag_name>
```

Add a tag to a task.

Output in different formats:

```bash
# JSON (default)
cucli add-tag <task_id> "urgent"

# Table format
cucli add-tag <task_id> "urgent" --format table

# Raw JSON
cucli add-tag <task_id> "urgent" --raw
```

### Remove tag from task

```bash
cucli remove-tag <task_id> <tag_name>
```

Remove a tag from a task.

Output in different formats:

```bash
# JSON (default)
cucli remove-tag <task_id> "urgent"

# Table format
cucli remove-tag <task_id> "urgent" --format table

# Raw JSON
cucli remove-tag <task_id> "urgent" --raw
```

### List goals

```bash
cucli goals <team_id>
```

List goals in a workspace.

Output in JSON format (default):

```json
[
  {
    "id": "e28a27f0-9571-4f9c-9f7a-4712f21b605e",
    "name": "Test Goal",
    "due_date": "1738368000000",
    "description": "Test goal description",
    "percent_completed": 0,
    "key_result_count": 2
  }
]
```

Output in table format:

```bash
cucli goals <team_id> --format table
```

```
ID                                  NAME                          DUE DATE         PROGRESS
-------------------------------------------------------------------------------------------
e28a27f0-9571-4f9c-9f7a-4712f21b605e  Test Goal                      1738368000000     0%
```

Include completed goals:

```bash
cucli goals <team_id> --include-completed
```

Output raw JSON:

```bash
cucli goals <team_id> --raw
```

### Get goal details

```bash
cucli goal <goal_id>
```

Get detailed information about a specific goal.

Output in different formats:

```bash
# JSON (default)
cucli goal e28a27f0-9571-4f9c-9f7a-4712f21b605e

# Table format
cucli goal e28a27f0-9571-4f9c-9f7a-4712f21b605e --format table

# Raw JSON
cucli goal e28a27f0-9571-4f9c-9f7a-4712f21b605e --raw
```

### Create goal

```bash
cucli create-goal <team_id> --name "Goal Name" --due-date 1738368000000
```

Create goal with additional options:

```bash
# With start date
cucli create-goal <team_id> --name "Goal Name" --due-date 1738368000000 --start-date 1735689600000

# With description
cucli create-goal <team_id> --name "Goal Name" --due-date 1738368000000 --description "Goal description"

# With multiple owners
cucli create-goal <team_id> --name "Goal Name" --due-date 1738368000000 --multiple-owners --owner 123 --owner 456

# With custom color
cucli create-goal <team_id> --name "Goal Name" --due-date 1738368000000 --color "#ff5733"
```

Output in different formats:

```bash
# JSON (default)
cucli create-goal <team_id> --name "New Goal" --due-date 1738368000000

# Table format
cucli create-goal <team_id> --name "New Goal" --due-date 1738368000000 --format table

# Raw JSON
cucli create-goal <team_id> --name "New Goal" --due-date 1738368000000 --raw
```

### Update goal

```bash
cucli update-goal <goal_id> --name "Updated Name"
```

Update goal with various options:

```bash
# Update name and due date
cucli update-goal <goal_id> --name "New Name" --due-date 1738368000000

# Update description and color
cucli update-goal <goal_id> --description "New description" --color "#32a852"

# Add owners
cucli update-goal <goal_id> --add-owner 123 --add-owner 456

# Remove owners
cucli update-goal <goal_id> --remove-owner 789
```

Output in different formats:

```bash
# JSON (default)
cucli update-goal <goal_id> --name "New Name"

# Table format
cucli update-goal <goal_id> --name "New Name" --format table

# Raw JSON
cucli update-goal <goal_id> --name "New Name" --raw
```

### Delete goal

```bash
cucli delete-goal <goal_id>
```

Delete with confirmation prompt (default):

```bash
cucli delete-goal <goal_id>
# You will be prompted to confirm: "Are you sure you want to delete goal <goal_id>?"
```

Skip confirmation prompt:

```bash
cucli delete-goal <goal_id> --yes
# or
cucli delete-goal <goal_id> -y
```

### Create key result

```bash
cucli create-key-result <goal_id> --name "Key Result Name"
```

Create key result with additional options:

```bash
# With type (number, currency, boolean, percentage, automatic)
cucli create-key-result <goal_id> --name "Sales Target" --type currency --unit "$"

# With progress range
cucli create-key-result <goal_id> --name "Completion Rate" --type percentage --steps-start 0 --steps-end 100

# With owners
cucli create-key-result <goal_id> --name "Key Result" --owner 123 --owner 456

# Link tasks
cucli create-key-result <goal_id> --name "Key Result" --task "86c7mc19h"

# Link lists
cucli create-key-result <goal_id> --name "Key Result" --list "90159451300"
```

Output in different formats:

```bash
# JSON (default)
cucli create-key-result <goal_id> --name "New Key Result"

# Table format
cucli create-key-result <goal_id> --name "New Key Result" --format table

# Raw JSON
cucli create-key-result <goal_id> --name "New Key Result" --raw
```

### Update key result

```bash
cucli update-key-result <key_result_id> --steps-current 50
```

Update key result with note:

```bash
cucli update-key-result <key_result_id> --steps-current 75 --note "Progress made"
```

Output in different formats:

```bash
# JSON (default)
cucli update-key-result <key_result_id> --steps-current 50

# Table format
cucli update-key-result <key_result_id> --steps-current 50 --format table

# Raw JSON
cucli update-key-result <key_result_id> --steps-current 50 --raw
```

### Delete key result

```bash
cucli delete-key-result <key_result_id>
```

Delete with confirmation prompt (default):

```bash
cucli delete-key-result <key_result_id>
# You will be prompted to confirm: "Are you sure you want to delete key result <key_result_id>?"
```

Skip confirmation prompt:

```bash
cucli delete-key-result <key_result_id> --yes
# or
cucli delete-key-result <key_result_id> -y
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
