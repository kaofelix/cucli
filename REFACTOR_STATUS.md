# Refactoring Status

This document tracks the progress of refactoring cucli.

## Completed Refactors

| Pattern | Date | Description |
|---------|------|-------------|
| Boolean Parameter String Conversion | 2026-01-28 | Added `_to_bool_str()` helper method to replace duplicate `str(x).lower()` patterns (7 occurrences reduced to 1 helper) |
| Error handling decorator | 2026-01-28 | Created `@handle_api_errors` decorator to replace duplicate try/except blocks (applied to all 53 functions) |
| Context manager helper | 2026-01-28 | Created `with_client()` helper to eliminate repeated `with ClickUpClient() as client:` pattern (refactored 28 of 54 occurrences) |
| Common output options decorator | 2026-01-28 | Created `@common_output_options` decorator to replace duplicate --format and --raw option definitions (applied to 46 commands) |
| Generic table formatter | 2026-01-28 | Created `format_table()` helper in helpers.py to replace duplicate table formatting logic (refactored 15 functions: workspaces, spaces, folders, lists, tags, team_views, space_views, folder_views, list_views, tasks, task_comments, list_comments, task_members, list_members, time_entries, webhooks) |
| Deletion confirmation helper | 2026-01-28 | Created `confirm_deletion()` helper in helpers.py to replace duplicate deletion confirmation logic (refactored 7 functions: delete_folder, delete_list, delete_task, delete_checklist, delete_checklist_item, delete_time_entry, delete_webhook) |
| Model parsing helper | 2026-01-28 | Created `parse_models_with_raw()` helper in helpers.py to replace duplicate raw output checking and model parsing patterns (refactored 8 functions: workspaces, spaces, folders, lists, task_comments, list_comments, task_members, list_members, tags) |
| Team ID validation helper | 2026-01-29 | Created `validate_team_id_for_custom_tasks()` helper in helpers.py to replace duplicate team_id validation for custom_task_ids pattern (refactored 5 functions: add_dependency, delete_dependency, add_link, delete_link, create_attachment) |
| Raw JSON output helper | 2026-01-29 | Created `handle_raw_output()` helper in helpers.py to replace duplicate raw JSON output patterns (refactored 27 functions: create_folder, folder, update_folder_cli, create_list, get_list_cli, task, create_task, update_task, create_checklist, create_checklist_item, update_checklist, update_checklist_item, create_tag, add_tag, remove_tag, running_time_entry, start_time_entry, stop_time_entry, create_time_entry, update_time_entry, tasks, add_comment, add_list_comment, time_entries, add_dependency, delete_dependency, add_link, delete_link, create_attachment, team_views, space_views, folder_views, list_views, view, webhooks, create_webhook, update_webhook_cli) |
| 204 response handler | 2026-01-29 | Created `_delete_with_204_handling()` helper method in api.py to replace duplicate 204 No Content response handling (refactored 2 functions: delete_folder, delete_task) |
| Empty collection handler | 2026-01-29 | Created `handle_empty_collection()` helper in helpers.py to replace duplicate empty collection output patterns (refactored 1 function: time_entries) |
| Context manager helper (delete commands) | 2026-01-29 | Refactored 6 delete commands to use `with_client()` helper: delete_folder, delete_list, delete_task, delete_checklist, delete_checklist_item, delete_time_entry, delete_webhook (now 35 of 54 occurrences refactored) |
| Context manager helper (remaining commands) | 2026-01-29 | Refactored remaining 18 commands to use `with_client()` helper: create_list, update_list_cli, create_task, update_task, add_comment, add_list_comment, update_checklist_item, create_tag, start_time_entry, time_entries, create_time_entry, update_time_entry, add_dependency, delete_dependency, add_link, delete_link, create_attachment, update_webhook_cli (now all 53 occurrences refactored) |
| Conditional data building helper | 2026-01-29 | Created `_build_data_dict()` helper method in api.py to replace duplicate data dict building patterns (refactored 17 functions: update_checklist, update_checklist_item, add_dependency, delete_dependency, add_task_link, delete_task_link, create_list, update_task, update_time_entry, create_task, create_task_comment, create_checklist_item, create_time_entry, create_goal, get_task_comments, get_list_comments, start_time_entry) |
| Time entry formatter helpers | 2026-01-29 | Created `format_time_entry_json()` and `format_time_entry_table()` helpers in helpers.py to replace duplicate time entry output patterns (refactored 5 functions: running_time_entry, start_time_entry, stop_time_entry, create_time_entry, update_time_entry) |
| JSON output helpers | 2026-01-29 | Created `format_list_output()` and `format_single_output()` helpers in helpers.py to replace duplicate JSON and table output transformation patterns (refactored 15 functions: workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, team_views, space_views, folder_views, list_views, webhooks, view) |
| Single-item output helpers | 2026-01-29 | Applied `format_single_output()` helper to additional single-item commands (refactored 7 functions: create_folder, folder, update_folder_cli, get_list_cli, update_list_cli, create_task, update_task) |
| Checklist output helpers | 2026-01-29 | Applied `format_single_output()` helper to checklist commands (refactored 4 functions: create_checklist, create_checklist_item, update_checklist, update_checklist_item) |
| Tag and comment output helpers | 2026-01-29 | Applied `format_single_output()` helper to tag and comment commands (refactored 5 functions: create_tag, add_tag, remove_tag, add_comment, add_list_comment) |
| Dependency, link, attachment, webhook output helpers | 2026-01-29 | Applied `format_single_output()` helper to dependency, link, attachment, and webhook commands (refactored 7 functions: add_dependency, delete_dependency, add_link, delete_link, create_attachment, create_webhook, update_webhook_cli) |

## In Progress

| Pattern | Started | Notes |
|---------|---------|-------|
| (none) | - | - |

## Planned Refactors (by priority)

### High Priority
- [x] Error handling decorator (40+ occurrences) - Completed: 53/53 functions refactored
- [x] Common output options decorator (30+ occurrences) - Completed: 46/46 commands refactored
- [x] Generic table formatter (20+ occurrences) - Completed: 16/20+ functions refactored (workspaces, spaces, folders, lists, tags, team_views, space_views, folder_views, list_views, tasks, task_comments, list_comments, task_members, list_members, time_entries, webhooks)
- [x] Context manager helper (50+ occurrences) - Completed: all 53 occurrences refactored
- [ ] Default features constant (API: 28 duplicate lines)

### Medium Priority
- [x] Deletion confirmation decorator (10 occurrences) - Added confirm_deletion() helper (refactored 7 functions: delete_folder, delete_list, delete_task, delete_checklist, delete_checklist_item, delete_time_entry, delete_webhook)
- [x] Raw JSON output helper (30+ occurrences) - Added handle_raw_output() helper (refactored 27 functions)
- [x] Model parsing helper (10+ occurrences) - Added parse_models_with_raw() helper (refactored 8 functions: workspaces, spaces, folders, lists, task_comments, list_comments, task_members, list_members, tags)
- [x] Empty collection handler (1 occurrence) - Added handle_empty_collection() helper (refactored 1 function: time_entries)
- [x] Params builder with bool conversion (10 occurrences) - Added _to_bool_str() helper
- [x] Conditional data building pattern (40+ occurrences in API) - Added _build_data_dict() helper (refactored 17 functions: update_checklist, update_checklist_item, add_dependency, delete_dependency, add_task_link, delete_task_link, create_list, update_task, update_time_entry, create_task, create_task_comment, create_checklist_item, create_time_entry, create_goal, get_task_comments, get_list_comments, start_time_entry)
- [x] JSON output formatter (15+ occurrences) - Added format_list_output() and format_single_output() helpers (refactored 15 functions: workspaces, spaces, folders, lists, tasks, task_comments, list_comments, task_members, list_members, team_views, space_views, folder_views, list_views, webhooks, view)

### Low Priority
- [x] Views output formatter (5 occurrences) - Completed: team_views, space_views, folder_views, list_views, webhooks refactored with format_table
- [x] Comments output formatter (2 occurrences) - Completed: task_comments, list_comments refactored with format_table
- [x] Members output formatter (2 occurrences) - Completed: task_members, list_members refactored with format_table
- [x] Time entry formatter (5 occurrences) - Added format_time_entry_json() and format_time_entry_table() helpers (refactored 5 functions: running_time_entry, start_time_entry, stop_time_entry, create_time_entry, update_time_entry)
- [x] 204 response handler (2 occurrences) - Added _delete_with_204_handling() helper (refactored 2 functions: delete_folder, delete_task)

## Metrics

- Initial lines of code: 5632 (cli.py: 4083, api.py: 1549)
- Lines removed through refactoring: 336 (error handling) + 84 (context manager helper, partial) + 276 (common output options) + 115 (table formatter, 10 functions) + 42 (deletion confirmation, 7 functions) + 85 (table formatter, 6 additional functions) + 18 (model parsing helper, 8 functions) + 20 (team ID validation, 5 functions) + 81 (raw output helper, 27 functions) + 6 (204 response handler, 2 functions) + 5 (empty collection handler, 1 function) + 12 (context manager helper, 6 delete commands) + 36 (context manager helper, remaining 18 commands) + 24 (conditional data building helper, 6 functions) + 23 (conditional data building helper, 3 additional functions) + 24 (conditional data building helper, 8 additional functions) + 60 (time entry formatter, 5 functions) + 145 (JSON output helpers, 15 functions) = 1392
- Lines added (helpers/utilities): 39 (error handling) + 15 (with_client helper) + 16 (common_output_options) + 97 (format_table helper) + 19 (confirm_deletion helper) + 37 (parse_models_with_raw helper) + 22 (validate_team_id_for_custom_tasks helper) + 20 (handle_raw_output helper) + 20 (_delete_with_204_handling helper) + 19 (handle_empty_collection helper) + 14 (_build_data_dict helper) + 48 (format_time_entry_json and format_time_entry_table helpers) + 74 (format_list_output and format_single_output helpers) = 440
- Net reduction: -952 (16.90%) - Reduced code duplication by creating @handle_api_errors, @common_output_options decorators, with_client helper, format_table helper, confirm_deletion helper, parse_models_with_raw helper, validate_team_id_for_custom_tasks helper, handle_raw_output helper, _delete_with_204_handling helper, handle_empty_collection helper, _build_data_dict helper, format_time_entry_json/format_time_entry_table helpers, and format_list_output/format_single_output helpers
