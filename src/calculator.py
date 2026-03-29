"""Simple calculator module — used as the sample codebase for CLAUDE.md/skills demo."""


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        Sum of a and b.
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a.

    Args:
        a: Minuend.
        b: Subtrahend.

    Returns:
        Difference of a and b.
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers.

    Args:
        a: First factor.
        b: Second factor.

    Returns:
        Product of a and b.
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide a by b.

    Args:
        a: Dividend.
        b: Divisor — must not be zero.

    Returns:
        Quotient as a float.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
