# Skill: add-test

Generate a pytest test for a given function in this project.

## Usage

```
/add-test
```

Claude will:
1. Ask which function or module to test (if not obvious from context).
2. Read the target function's source code.
3. Write a `pytest` test covering normal cases, edge cases, and expected errors.
4. Append the test to the appropriate file in `src/tests/`.

## Rules

- Follow the project's Google-style docstring convention.
- Use `pytest.mark.parametrize` for data-driven cases.
- Name tests `test_<function_name>_<scenario>`.
- Never overwrite existing tests — append only.

## Example output

```python
import pytest
from src.calculator import divide

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (0, 5, 0.0),
    (-6, 3, -2.0),
])
def test_divide_normal(a: int, b: int, expected: float) -> None:
    assert divide(a, b) == expected

def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```
