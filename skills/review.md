# Skill: review

Review staged or recently changed code for quality issues before committing.

## Usage

```
/review
```

## What Claude checks

1. **Correctness** — logic errors, off-by-one, wrong conditionals.
2. **Style** — PEP 8 compliance, line length, naming conventions.
3. **Type safety** — missing or incorrect type hints.
4. **Tests** — whether new code has corresponding tests.
5. **Security** — obvious injection risks, hardcoded secrets, unsafe eval/exec.
6. **CLAUDE.md compliance** — does the change follow project conventions?

## Output format

Claude will respond with:

```
## Review Summary

### Issues (must fix)
- [ ] <file>:<line> — <description>

### Suggestions (optional)
- [ ] <file>:<line> — <description>

### Looks good
- <what is done well>
```

## Notes

- Run `git diff --staged` to see what will be reviewed.
- If nothing is staged, Claude reviews the last commit (`git diff HEAD~1`).
