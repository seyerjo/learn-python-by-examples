""" TYPE HINTING (PEP 484)

    Type Hinting, introduced in PEP 484, allows developers to indicate the
    expected data types for variables, function parameters, and return values.

    IMPORTANT: Python remains a dynamically-typed language. These "hints" are
    not enforced by the Python interpreter at runtime. They are primarily for:
    1.  Improving code readability and self-documentation.
    2.  Allowing static analysis tools (like mypy) to catch type-related
        errors before the code is even run.
    3.  Enhancing IDE support for autocompletion and error checking.

"""

# Variable with a type hint
PI: float = 3.14159


def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns their sum.

    This function uses type hints to declare that 'a' and 'b' are expected
    to be integers, and the function itself is expected to return an integer.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


def main() -> None:
    """Main function to demonstrate type hinting."""
    result: int = add_numbers(10, 5)  # Adding type hint for 'result'
    print(f"The result of adding two numbers is: {result}")
    print(f"The type of PI is declared as float, its value is: {PI}")


if __name__ == "__main__":
    main()
