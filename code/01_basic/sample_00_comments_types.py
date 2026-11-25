"""Demonstrates comment styles, docstrings, and basic module structure in Python."""

# Single-line comment explaining a module-level constant.
INITIAL_VALUE = 10  # Inline comment explaining an expression or value.


def calculate_square(number):
    """Calculate the square of a number.

    Args:
        number: The numeric value to square.

    Returns:
        The squared value.
    """
    return number * number


def main():
    """Demonstrates calling a documented function and using constants."""
    calculation_result = calculate_square(5)
    print(f"5 squared = {calculation_result}")

    # Combine the module constant with the function result.
    total = INITIAL_VALUE + calculation_result
    print(f"{INITIAL_VALUE} + {calculation_result} = {total}")


if __name__ == "__main__":
    main()

# Commented-out code is ignored by the Python interpreter:
# print("This line will not run.")
