# CLAUDE.md — Project Intelligence File

This file is automatically read by Claude Code at session start.
It gives Claude context about this project: conventions, commands, and constraints.

---

## Project Overview

**Name:** scratch-demo
**Purpose:** Demonstrate how CLAUDE.md and Claude Code skills work together.
**Stack:** Python 3.11+, pytest, ruff (linting)

---

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest src/tests/ -v

# Lint and format
ruff check src/
ruff format src/

# Run the main script
python src/main.py
```

---

## Code Conventions

- **Style:** Follow PEP 8. Max line length = 100 chars.
- **Types:** Always add type hints to function signatures.
- **Docstrings:** Use Google-style docstrings for all public functions.
- **Tests:** Every new function needs a corresponding test in `src/tests/`.
- **Commits:** Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`.

### Example — correct style

```python
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Sum of a and b.
    """
    return a + b
```

---

## Folder Structure

```
scratch/
├── CLAUDE.md               ← You are here
├── README.md
├── requirements.txt
├── .claude/
│   └── settings.json       ← Claude Code hook/permission config
├── skills/                 ← Project-level skill definitions
│   ├── add-test.md
│   ├── review.md
│   └── changelog.md
└── src/
    ├── main.py
    ├── calculator.py
    └── tests/
        └── test_calculator.py
```

---

## Constraints & Notes for Claude

- **Never** delete files without confirming with the user.
- **Never** push to `master` directly — always use a feature branch.
- When adding a new module, also update `src/main.py` to import it.
- Prefer editing existing files over creating new ones.
- The `skills/` directory contains project-specific slash commands — use them.

---

## Available Skills (Slash Commands)

| Command        | Description                                      |
|----------------|--------------------------------------------------|
| `/add-test`    | Generate a pytest test for a given function      |
| `/review`      | Review staged changes for quality issues         |
| `/changelog`   | Append a changelog entry for the current change  |

> Skills are defined in `skills/*.md`. See each file for usage details.

---

## Suggested MCP Plugins

These MCP (Model Context Protocol) servers would enhance this project:

| Plugin              | Purpose                                          | Install                          |
|---------------------|--------------------------------------------------|----------------------------------|
| `@modelcontextprotocol/server-filesystem` | Safe file read/write with boundaries | `npx @modelcontextprotocol/server-filesystem` |
| `@modelcontextprotocol/server-github`    | GitHub PR/issue integration          | `npx @modelcontextprotocol/server-github`     |
| `@modelcontextprotocol/server-sqlite`    | Query a local SQLite database        | `npx @modelcontextprotocol/server-sqlite`     |
| `mcp-server-fetch`  | Fetch external URLs / API docs        | `uvx mcp-server-fetch`           |

Configure them in `.claude/settings.json` under `mcpServers`.
