"""Demonstrates PEP 8 naming, reserved keywords, dynamic typing, and len()."""

import keyword


def show_naming_conventions():
    """Prints PEP 8 naming conventions for variables, classes, and constants."""
    print("--- Naming Conventions (PEP 8) ---")
    print(
        "  - snake_case: Variables and functions (e.g., user_name, calculate_total())."
    )
    print("  - PascalCase: Classes (e.g., class MyNewClass:).")
    print("  - UPPER_SNAKE_CASE: Constants (e.g., PI = 3.14, MAX_CONNECTIONS = 5).")
    print("  - Descriptive names: Prefer customer_address over addr or c_a.")
    print("  - Leading underscore: Indicates internal use (e.g., _internal_value).")
    print()


def show_reserved_keywords():
    """Prints Python's list of reserved keywords."""
    print("--- Python Reserved Keywords ---")
    print("These words have special meaning and cannot be used as variable names:")
    print(keyword.kwlist)
    print()


def demonstrate_dynamic_typing():
    """Demonstrates rebinding a variable name to objects of different types."""
    print("--- Dynamic Typing Demonstration ---")
    my_variable = 1
    print(f"my_variable is '{my_variable}' of type {type(my_variable)}")

    my_variable = 3.75
    print(f"my_variable is now '{my_variable}' of type {type(my_variable)}")

    my_variable = "hello"
    print(f"my_variable is now '{my_variable}' of type {type(my_variable)}")
    print()


def demonstrate_string_input_and_len():
    """Reads a user's name and reports the greeting length with len()."""
    print("--- Input, F-Strings, and Length ---")
    name = input("What's your name?: ")
    greeting = f"Hi {name}, my best regards."
    print(greeting)
    print(f"Length of this greeting: {len(greeting)} characters.")
    print()


def main():
    """Runs all Python fundamentals demonstrations."""
    show_naming_conventions()
    show_reserved_keywords()
    demonstrate_dynamic_typing()
    demonstrate_string_input_and_len()


if __name__ == "__main__":
    main()
