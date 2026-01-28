# Refactoring Status

This document tracks the progress of refactoring cucli.

## Completed Refactors

| Pattern | Date | Description |
|---------|------|-------------|
| Boolean Parameter String Conversion | 2026-01-28 | Added `_to_bool_str()` helper method to replace duplicate `str(x).lower()` patterns (7 occurrences reduced to 1 helper) |

## In Progress

| Pattern | Started | Notes |
|---------|---------|-------|
| - | - | - |

## Planned Refactors (by priority)

### High Priority
- [ ] Error handling decorator (40+ occurrences)
- [ ] Common output options decorator (30+ occurrences)
- [ ] Generic table formatter (20+ occurrences)
- [ ] Context manager helper (50+ occurrences)
- [ ] Default features constant (API: 28 duplicate lines)

### Medium Priority
- [ ] Deletion confirmation decorator (10 occurrences)
- [ ] JSON output formatter (15+ occurrences)
- [ ] Model parsing helper (10+ occurrences)
- [ ] Empty collection handler (15 occurrences)
- [ ] Params builder with bool conversion (10 occurrences)

### Low Priority
- [ ] Views output formatter (5 occurrences)
- [ ] Comments output formatter (2 occurrences)
- [ ] Members output formatter (2 occurrences)
- [ ] 204 response handler (5 occurrences)
- [ ] Time entry formatter (4 occurrences)

## Metrics

- Initial lines of code: 5632 (cli.py: 4083, api.py: 1549)
- Lines removed through refactoring: 14
- Lines added (helpers/utilities): 14
- Net reduction: 0 (0%) - Reduced code duplication by replacing 7 `str().lower()` calls with helper method
