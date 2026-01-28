# Refactoring Candidates: Duplicated Patterns in cucli

This document lists all the duplicated patterns identified in the codebase that are candidates for refactoring.

---

## CLI FILE (cli.py) - 4000+ lines

### 1. Error Handling Pattern (40+ occurrences)
**Pattern:** Identical try/except blocks in almost every command function.

```python
try:
    with ClickUpClient() as client:
        data = client.some_method(...)
except httpx.HTTPStatusError as e:
    click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
    raise click.Abort()
except ValueError as e:
    click.echo(f"Error: {e}", err=True)
    raise click.Abort()
except Exception as e:
    click.echo(f"Unexpected error: {e}", err=True)
    raise click.Abort()
```

**Examples found in:**
- `workspaces()`, `spaces()`, `folders()`, `create_folder()`, `folder()`, `update_folder_cli()`, `delete_folder()`, `create_list()`, `lists()`, `get_list_cli()`, `update_list_cli()`, `delete_list()`, `task()`, `tasks()`, `create_task()`, `update_task()`, `delete_task()`, `task_comments()`, `add_comment()`, `list_comments()`, `add_list_comment()`, `create_checklist()`, `create_checklist_item()`, `update_checklist()`, `update_checklist_item()`, `delete_checklist()`, `delete_checklist_item()`, `task_members()`, `list_members()`, `tags()`, `create_tag()`, `add_tag()`, `remove_tag()`, `running_time_entry()`, `start_time_entry()`, `stop_time_entry()`, `time_entries()`, `create_time_entry()`, `update_time_entry()`, `delete_time_entry()`, `goals()`, `goal()`, `create_goal()`, `update_goal()`, `delete_goal()`, `create_key_result()`, `update_key_result()`, `delete_key_result()`, `add_dependency()`, `delete_dependency()`, `add_link()`, `delete_link()`, `create_attachment()`, `team_views()`, `space_views()`, `folder_views()`, `list_views()`, `view()`, `webhooks()`, `create_webhook()`, `update_webhook_cli()`, `delete_webhook()`

**Refactoring approach:**
- Create a decorator `@handle_api_errors` to wrap command functions
- Or create a context manager `with api_error_handling():`
- Extract error handling to a helper function

---

### 2. Output Format Options (30+ occurrences)
**Pattern:** Repeated `--format` and `--raw` option definitions.

```python
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
```

**Examples found in:** Most commands (workspaces, spaces, folders, create_folder, folder, update_folder_cli, create_list, lists, get_list_cli, update_list_cli, task, tasks, create_task, update_task, task_comments, add_comment, list_comments, add_list_comment, create_checklist, create_checklist_item, update_checklist, update_checklist_item, task_members, list_members, tags, create_tag, add_tag, remove_tag, running_time_entry, start_time_entry, stop_time_entry, time_entries, create_time_entry, update_time_entry, goals, goal, create_goal, update_goal, create_key_result, update_key_result, add_dependency, delete_dependency, add_link, delete_link, create_attachment, team_views, space_views, folder_views, list_views, view, webhooks, create_webhook, update_webhook_cli)

**Refactoring approach:**
- Create a custom Click option decorator or mixin
- Or create a common options file with shared decorators
- Example: `@common_output_options` decorator

---

### 3. Raw JSON Output Pattern (30+ occurrences)
**Pattern:** Early return with raw JSON dump.

```python
if raw:
    click.echo(json.dumps(data, indent=2))
    return
```

**Examples found in:** All commands that support `--raw` option.

**Refactoring approach:**
- Create helper function `handle_raw_output(data, raw)` or similar
- Could be combined with the format option refactoring

---

### 4. Table Output Patterns (20+ occurrences)
**Pattern:** Similar table formatting logic repeated.

```python
# Calculate column widths
max_id = max(len(t.id) for t in items)
max_name = max(len(t.name) for t in items)

# Print header
click.echo(f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  ...")
click.echo("-" * (max_id + max_name + ...))

# Print rows
for item in items:
    click.echo(f"{item.id.ljust(max_id)}  {item.name.ljust(max_name)}  ...")
```

**Examples found in:** workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, tags, time_entries, goals, team_views, space_views, folder_views, list_views, webhooks

**Refactoring approach:**
- Create a generic table formatter class/function
- Accept column definitions, data, and formatting functions
- Example: `format_table(columns, data, row_formatter)`

---

### 5. Context Manager Pattern (50+ occurrences)
**Pattern:** Repeated `with ClickUpClient() as client:`

```python
with ClickUpClient() as client:
    data = client.some_method(...)
```

**Examples found in:** Almost every command function.

**Refactoring approach:**
- Create a helper function that accepts a callable working with the client
- Example: `with_client(lambda client: client.some_method())`

---

### 6. Deletion Confirmation Pattern (10 occurrences)
**Pattern:** Identical confirmation logic.

```python
if not yes:
    if not click.confirm(f"Are you sure you want to delete {resource_type} {resource_id}?"):
        click.echo("Deletion cancelled.")
        return
```

**Examples found in:** delete_folder, delete_list, delete_task, delete_checklist, delete_checklist_item, delete_time_entry, delete_goal, delete_key_result, delete_webhook

**Refactoring approach:**
- Create a decorator `@require_confirmation` or helper function
- Parameterize resource type

---

### 7. Team ID Validation Pattern (5 occurrences)
**Pattern:** Same validation for custom_task_ids with team_id.

```python
if custom_task_ids and not team_id:
    click.echo(
        "Error: --team-id is required when using --custom-task-ids.",
        err=True,
    )
    raise click.Abort()
```

**Examples found in:** add_dependency, delete_dependency, add_link, delete_link, create_attachment

**Refactoring approach:**
- Create a validator function or callback
- Use Click's `callback` parameter in option

---

### 8. JSON Response Transformation Patterns (15+ occurrences)
**Pattern:** Similar transformations of API responses to JSON.

```python
if format == "json":
    output = [{"id": item.id, "name": item.name, ...} for item in items]
    click.echo(json.dumps(output, indent=2))
elif format == "table":
    ...
```

**Examples found in:** workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, tags, time_entries, goals, team_views, space_views, folder_views, list_views, webhooks

**Refactoring approach:**
- Create a generic formatter that accepts a list of field definitions
- Example: `format_json(items, field_mappings)`

---

### 9. Data Model Parsing Patterns (10+ occurrences)
**Pattern:** Parsing raw API response into Pydantic models.

```python
if raw:
    click.echo(json.dumps(data, indent=2))
    return

items = [Model(**item) for item in data["items"]]
```

**Examples found in:** workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, tags

**Refactoring approach:**
- Create a helper to handle model parsing with raw fallback
- Example: `parse_models(data, key, model_class, raw)`

---

### 10. Empty Collection Handling Pattern (15+ occurrences)
**Pattern:** Same empty result message.

```python
if not items:
    click.echo("No {items} found.")
    return
```

**Examples found in:** workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, tags, time_entries, goals, team_views, space_views, folder_views, list_views, webhooks

**Refactoring approach:**
- Create a helper function or integrate into table formatter

---

### 11. Time Entry Response Pattern (4 occurrences)
**Pattern:** Extracting time entry data from nested response.

```python
entry = data.get("data", {})
# Format entry for output...
```

**Examples found in:** running_time_entry, start_time_entry, stop_time_entry, create_time_entry

**Refactoring approach:**
- Create a time_entry formatter function

---

### 12. Views Response Pattern (5 occurrences)
**Pattern:** Identical views listing code.

```python
views_list = data.get("views", [])
# Format views for output...
```

**Examples found in:** team_views, space_views, folder_views, list_views

**Refactoring approach:**
- Create a single `format_views_output()` helper
- All 4 functions are nearly identical

---

### 13. Comments Output Pattern (2 occurrences)
**Pattern:** Nearly identical comments listing for task and list.

`task_comments()` and `list_comments()` are 95% identical.

**Refactoring approach:**
- Create a generic `format_comments_output()` function

---

### 14. Members Output Pattern (2 occurrences)
**Pattern:** Nearly identical members listing for task and list.

`task_members()` and `list_members()` are 95% identical.

**Refactoring approach:**
- Create a generic `format_members_output()` function

---

## API FILE (api.py) - 1900+ lines

### 1. Default Features Dictionary Pattern (3 occurrences)
**Pattern:** Same 14-line default features dictionary defined twice.

```python
data["features"] = {
    "due_dates": {...},
    "time_tracking": {"enabled": True},
    "tags": {"enabled": True},
    "time_estimates": {"enabled": True},
    "checklists": {"enabled": True},
    "custom_fields": {"enabled": True},
    "remap_dependencies": {"enabled": True},
    "dependency_warning": {"enabled": True},
    "portfolios": {"enabled": True},
}
```

**Examples found in:** update_space(), create_space()

**Refactoring approach:**
- Extract to a class constant `_DEFAULT_FEATURES`
- Or helper method `_get_default_features()`

---

### 2. Conditional Data Building Pattern (40+ occurrences)
**Pattern:** Building request dict with optional fields.

```python
data: dict[str, Any] = {}

if field1 is not None:
    data["field1"] = field1
if field2 is not None:
    data["field2"] = field2
# ... many more if statements

if data:
    response = self._client.put(url, json=data)
    response.raise_for_status()
    return response.json()

return {}
```

**Examples found in:** update_space, create_space, update_folder, update_list, update_task, update_checklist, update_checklist_item, update_time_entry, update_goal, update_key_result, update_webhook

**Refactoring approach:**
- Create a helper that accepts field mappings and values
- Use dictionary comprehension to exclude None values

---

### 3. Boolean Parameter String Conversion Pattern (10+ occurrences)
**Pattern:** Converting boolean to lowercase string for API.

```python
params: dict[str, Any] = {}
if archived is not None:
    params["archived"] = str(archived).lower()
if include_closed is not None:
    params["include_closed"] = str(include_closed).lower()
```

**Examples found in:** get_spaces, get_folders, get_lists, get_team_tasks, get_goals

**Refactoring approach:**
- Create a helper function `_build_params()` that auto-converts bools

---

### 4. Response Status 204 Handling Pattern (5 occurrences)
**Pattern:** Special handling for 204 No Content responses.

```python
response = self._client.delete(url)
if response.status_code == 204:
    return None
response.raise_for_status()
return response.json()
```

**Examples found in:** delete_space, delete_folder, delete_list, delete_task, delete_webhook

**Refactoring approach:**
- Create a helper method `_delete(url)` that handles 204 automatically

---

### 5. List Parameter Building Pattern (1 occurrence)
**Pattern:** Building list parameters with [] suffix.

```python
if space_ids:
    params["space_ids[]"] = space_ids
if list_ids:
    params["list_ids[]"] = list_ids
```

**Examples found in:** get_team_tasks

**Refactoring approach:**
- Could use a helper for list parameters

---

## CROSS-FILE PATTERNS

### 1. Validation Logic Duplication
**Pattern:** Same validation logic exists in both CLI and API layers.

**Examples:**
- Team ID validation when using custom_task_ids
- Required parameter checks

**Refactoring approach:**
- Move validation to API layer with clear error messages
- Let CLI handle user-friendly output, API handle validation

---

## SUMMARY BY PRIORITY

### High Priority (Most Duplicated, High Impact)
1. **Error handling decorator** - 40+ occurrences, critical for maintainability
2. **Common output options decorator** - 30+ occurrences, reduces code significantly
3. **Generic table formatter** - 20+ occurrences, centralizes table formatting
4. **Context manager helper** - 50+ occurrences, simplifies client usage
5. **Default features constant** - Eliminates 28 duplicate lines in API

### Medium Priority (Moderate Impact)
6. **Deletion confirmation decorator** - 10 occurrences, improves consistency
7. **JSON output formatter** - 15+ occurrences, simplifies data transformation
8. **Model parsing helper** - 10+ occurrences, standardizes data handling
9. **Empty collection handler** - 15 occurrences, improves UX consistency
10. **Params builder with bool conversion** - 10+ occurrences in API

### Low Priority (Minor Impact)
11. **Views output formatter** - 5 occurrences
12. **Comments output formatter** - 2 occurrences (95% identical)
13. **Members output formatter** - 2 occurrences (95% identical)
14. **204 response handler** - 5 occurrences
15. **Time entry formatter** - 4 occurrences

---

## POTENTIAL REFACTORING APPROACHES

### 1. Decorator-Based
```python
@handle_api_errors
@common_output_options
@click.command(...)
def my_command():
    ...
```

### 2. Helper Functions
```python
def format_table(columns, data, format, raw):
    ...

def handle_output(data, format, raw, formatter=None):
    ...
```

### 3. Mixin/Composition
```python
class ClickUpCommandMixin:
    def format_table(self, ...):
        ...
    def handle_output(self, ...):
        ...
```

### 4. Command Builder Pattern
```python
@command_builder(output_options=True, error_handling=True)
def my_command():
    ...
```

---

## ESTIMATED IMPACT

- **Lines of code reduction**: ~800-1200 lines (20-30% of cli.py)
- **Improved maintainability**: Changes to error handling or formatting in one place
- **Better consistency**: All commands behave the same way
- **Easier testing**: Decorators and helpers can be unit tested independently
- **Type safety**: Helper functions can be properly typed
