"""Tests for calculator.py — generated via /add-test skill as an example."""

import pytest

from src.calculator import add, divide, multiply, subtract


# ── add ──────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
])
def test_add_normal(a: float, b: float, expected: float) -> None:
    assert add(a, b) == expected


# ── subtract ─────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
])
def test_subtract_normal(a: float, b: float, expected: float) -> None:
    assert subtract(a, b) == expected


# ── multiply ─────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (0, 100, 0),
    (-2, 5, -10),
])
def test_multiply_normal(a: float, b: float, expected: float) -> None:
    assert multiply(a, b) == expected


# ── divide ───────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (0, 5, 0.0),
    (-6, 3, -2.0),
])
def test_divide_normal(a: float, b: float, expected: float) -> None:
    assert divide(a, b) == expected


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)
