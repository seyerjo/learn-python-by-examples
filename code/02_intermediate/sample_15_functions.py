"""Demonstrates function parameters, return values, defaults, and keyword calls."""

# Type hints are intentionally deferred here; see sample_23_type_hinting.py.


def add_numbers(a, b):
    """Returns the sum of two numbers.

    Args:
        a: First numeric operand.
        b: Second numeric operand.

    Returns:
        Sum of a and b.
    """
    return a + b


def format_full_name(first_name, last_name, reverse=False):
    """Formats a first and last name with an optional reversed order.

    Args:
        first_name: Person's given name.
        last_name: Person's family name.
        reverse: When True, returns "Last, First". Defaults to False.

    Returns:
        Formatted full name string.
    """
    if reverse:
        return f"{last_name}, {first_name}"
    return f"{first_name} {last_name}"


def main():
    """Demonstrates positional, default, and keyword function calls."""
    print("--- Demonstrating `add_numbers` function ---")
    sum_result = add_numbers(5, 3)
    print(f"The result of add_numbers(5, 3) is: {sum_result}\n")

    print("--- Demonstrating `format_full_name` function ---")
    regular_name = format_full_name("John", "Doe")
    print(f"Default order: {regular_name}")

    reversed_name = format_full_name("John", "Doe", reverse=True)
    print(f"Reversed order: {reversed_name}")

    kw_name = format_full_name(last_name="Doe", first_name="John")
    print(f"Called with keyword arguments: {kw_name}\n")


if __name__ == "__main__":
    main()
