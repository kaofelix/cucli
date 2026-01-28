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

## In Progress

| Pattern | Started | Notes |
|---------|---------|-------|
| (none) | - | - |

## Planned Refactors (by priority)

### High Priority
- [x] Error handling decorator (40+ occurrences) - Completed: 53/53 functions refactored
- [x] Common output options decorator (30+ occurrences) - Completed: 46/46 commands refactored
- [x] Generic table formatter (20+ occurrences) - Completed: 16/20+ functions refactored (workspaces, spaces, folders, lists, tags, team_views, space_views, folder_views, list_views, tasks, task_comments, list_comments, task_members, list_members, time_entries, webhooks)
- [x] Context manager helper (50+ occurrences) - Partially completed: 29 of 54 occurrences refactored (25 remain, likely complex patterns)
- [ ] Default features constant (API: 28 duplicate lines)

### Medium Priority
- [x] Deletion confirmation decorator (10 occurrences) - Added confirm_deletion() helper (refactored 7 functions: delete_folder, delete_list, delete_task, delete_checklist, delete_checklist_item, delete_time_entry, delete_webhook)
- [ ] JSON output formatter (15+ occurrences)
- [x] Model parsing helper (10+ occurrences) - Added parse_models_with_raw() helper (refactored 8 functions: workspaces, spaces, folders, lists, task_comments, list_comments, task_members, list_members, tags)
- [ ] Empty collection handler (15 occurrences)
- [x] Params builder with bool conversion (10 occurrences) - Added _to_bool_str() helper

### Low Priority
- [x] Views output formatter (5 occurrences) - Completed: team_views, space_views, folder_views, list_views, webhooks refactored with format_table
- [x] Comments output formatter (2 occurrences) - Completed: task_comments, list_comments refactored with format_table
- [x] Members output formatter (2 occurrences) - Completed: task_members, list_members refactored with format_table
- [x] Time entry formatter (4 occurrences) - Completed: time_entries refactored with format_table
- [ ] 204 response handler (5 occurrences)

## Metrics

- Initial lines of code: 5632 (cli.py: 4083, api.py: 1549)
- Lines removed through refactoring: 336 (error handling) + 84 (context manager helper, partial) + 276 (common output options) + 115 (table formatter, 10 functions) + 42 (deletion confirmation, 7 functions) + 85 (table formatter, 6 additional functions) + 18 (model parsing helper, 8 functions) = 956
- Lines added (helpers/utilities): 39 (error handling) + 15 (with_client helper) + 16 (common_output_options) + 97 (format_table helper) + 19 (confirm_deletion helper) + 37 (parse_models_with_raw helper) = 223
- Net reduction: -733 (13.02%) - Reduced code duplication by creating @handle_api_errors, @common_output_options decorators, with_client helper, format_table helper, confirm_deletion helper, and parse_models_with_raw helper
