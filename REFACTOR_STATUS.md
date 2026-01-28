# Refactoring Status

This document tracks the progress of refactoring cucli.

## Completed Refactors

| Pattern | Date | Description |
|---------|------|-------------|
| Boolean Parameter String Conversion | 2026-01-28 | Added `_to_bool_str()` helper method to replace duplicate `str(x).lower()` patterns (7 occurrences reduced to 1 helper) |
| Error handling decorator | 2026-01-28 | Created `@handle_api_errors` decorator to replace duplicate try/except blocks (applied to all 53 functions) |
| Context manager helper | 2026-01-28 | Created `with_client()` helper to eliminate repeated `with ClickUpClient() as client:` pattern (refactored 28 of 54 occurrences) |
| Common output options decorator | 2026-01-28 | Created `@common_output_options` decorator to replace duplicate --format and --raw option definitions (applied to 46 commands) |

## In Progress

| Pattern | Started | Notes |
|---------|---------|-------|
| (none) | - | - |

## Planned Refactors (by priority)

### High Priority
- [x] Error handling decorator (40+ occurrences) - Completed: 53/53 functions refactored
- [x] Common output options decorator (30+ occurrences) - Completed: 46/46 commands refactored
- [ ] Generic table formatter (20+ occurrences)
- [x] Context manager helper (50+ occurrences) - Partially completed: 28 of 54 occurrences refactored (26 remain, likely complex patterns)
- [ ] Default features constant (API: 28 duplicate lines)

### Medium Priority
- [ ] Deletion confirmation decorator (10 occurrences)
- [ ] JSON output formatter (15+ occurrences)
- [ ] Model parsing helper (10+ occurrences)
- [ ] Empty collection handler (15 occurrences)
- [x] Params builder with bool conversion (10 occurrences) - Added _to_bool_str() helper

### Low Priority
- [ ] Views output formatter (5 occurrences)
- [ ] Comments output formatter (2 occurrences)
- [ ] Members output formatter (2 occurrences)
- [ ] 204 response handler (5 occurrences)
- [ ] Time entry formatter (4 occurrences)

## Metrics

- Initial lines of code: 5632 (cli.py: 4083, api.py: 1549)
- Lines removed through refactoring: 336 (error handling) + 84 (context manager helper, partial) + 276 (common output options) = 696
- Lines added (helpers/utilities): 39 (error handling) + 15 (with_client helper) + 16 (common_output_options) = 70
- Net reduction: -626 (11.11%) - Reduced code duplication by creating @handle_api_errors, @common_output_options decorators and with_client helper
