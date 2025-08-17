# MAIN CODE

"""
Demonstrates the fundamentals of defining and using functions in Python.

This example covers:
- Basic function definition with parameters.
- Functions that return a value.
- Functions with default parameter values (optional arguments).
- Calling functions using positional and keyword arguments.
"""


def add_numbers(a, b):
    """
    Takes two numbers as input and returns their sum.
    This is an example of a function with positional parameters and a return value.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def format_full_name(first_name, last_name, reverse=False):
    """
    Combines a first and last name into a single string.
    This demonstrates default arguments and conditional logic.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        reverse (bool, optional): If True, formats as "Last, First".
                                  Defaults to False.

    Returns:
        str: The formatted full name.
    """
    if reverse:
        return f"{last_name}, {first_name}"
    return f"{first_name} {last_name}"


def main():
    """Main function to demonstrate various ways to call functions."""
    print("--- Demonstrating `add_numbers` function ---")
    # Calling with positional arguments
    sum_result = add_numbers(5, 3)
    print(f"The result of add_numbers(5, 3) is: {sum_result}\n")

    print("--- Demonstrating `format_full_name` function ---")
    # Calling with only the required positional arguments
    regular_name = format_full_name("John", "Doe")
    print(f"Default order: {regular_name}")

    # Calling with the optional argument set to True
    reversed_name = format_full_name("John", "Doe", reverse=True)
    print(f"Reversed order: {reversed_name}")

    # Calling using keyword arguments allows changing the order
    kw_name = format_full_name(last_name="Doe", first_name="John")
    print(f"Called with keyword arguments: {kw_name}\n")


if __name__ == "__main__":
    main()
