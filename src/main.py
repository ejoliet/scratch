"""Entry point — demonstrates using the calculator module."""

from src.calculator import add, divide, multiply, subtract


def main() -> None:
    """Run a quick demo of all calculator operations."""
    pairs = [(10, 3), (0, 5), (-4, -2)]

    for a, b in pairs:
        print(f"{a} + {b} = {add(a, b)}")
        print(f"{a} - {b} = {subtract(a, b)}")
        print(f"{a} * {b} = {multiply(a, b)}")
        try:
            print(f"{a} / {b} = {divide(a, b):.4f}")
        except ZeroDivisionError as e:
            print(f"{a} / {b} = ERROR: {e}")
        print()


if __name__ == "__main__":
    main()
