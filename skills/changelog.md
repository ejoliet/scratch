# Skill: changelog

Append a formatted changelog entry based on recent commits or staged changes.

## Usage

```
/changelog
```

## Behavior

1. Claude reads `git log --oneline` since the last tag (or last 10 commits).
2. Groups changes into: **Added**, **Changed**, **Fixed**, **Removed**.
3. Appends an entry to `CHANGELOG.md` using [Keep a Changelog](https://keepachangelog.com) format.
4. Uses today's date and the next semantic version (patch bump by default).

## Example output appended to CHANGELOG.md

```markdown
## [0.2.0] - 2026-03-29

### Added
- `divide` function in `calculator.py` with zero-division guard.
- pytest parametrize tests for all calculator operations.

### Fixed
- Off-by-one error in `multiply` when operand is negative.
```

## Notes

- Does NOT commit the changelog — you review and commit manually.
- Pass a version hint with `/changelog v1.0.0` to override the auto-bumped version.
