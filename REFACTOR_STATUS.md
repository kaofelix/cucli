# Refactoring Status

This document tracks the progress of refactoring cucli.

## Completed Refactors

| Pattern | Date | Description |
|---------|------|-------------|
| Boolean Parameter String Conversion | 2026-01-28 | Added `_to_bool_str()` helper method to replace duplicate `str(x).lower()` patterns (7 occurrences reduced to 1 helper) |
| Error handling decorator | 2026-01-28 | Created `@handle_api_errors` decorator to replace duplicate try/except blocks (applied to all 53 functions) |

## In Progress

| Pattern | Started | Notes |
|---------|---------|-------|
| (none) | - | - |

## Planned Refactors (by priority)

### High Priority
- [x] Error handling decorator (40+ occurrences) - Completed: 53/53 functions refactored
- [ ] Common output options decorator (30+ occurrences)
- [ ] Generic table formatter (20+ occurrences)
- [ ] Context manager helper (50+ occurrences)
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
- Lines removed through refactoring: 336 (error handling decorator removed ~14 try/except blocks from remaining functions)
- Lines added (helpers/utilities): 39
- Net reduction: -297 (5.27%) - Reduced code duplication by creating @handle_api_errors decorator and applying to all 53 functions
