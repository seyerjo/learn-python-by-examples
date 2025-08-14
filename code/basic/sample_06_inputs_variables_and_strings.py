# MAIN CODE

"""
Demonstrates Python fundamentals: variable naming, reserved keywords,
dynamic typing, and combining inputs with string operations.
"""

import keyword


def show_naming_conventions():
    """Prints best practices for naming in Python, as per PEP 8."""
    print("--- Naming Conventions (PEP 8) ---")
    print("The most common and important conventions are:")
    print("  - `snake_case`: Used for variables and functions. It's the standard for most names.")
    print("    (e.g., `user_name`, `calculate_total()`).")
    print("  - `PascalCase`: Used for classes. This is a key distinction from variables.")
    print("    (e.g., `class MyNewClass:`).")
    print("  - `ALL_CAPS`: Used for constants — variables whose values are not intended to change.")
    print("    (e.g., `PI = 3.14`, `MAX_CONNECTIONS = 5`).")

    print("\nOther Important Considerations:")
    print("  - **Descriptiveness**: Names should be clear and descriptive, not single letters.")
    print("    (e.g., `customer_address` is better than `addr` or `c_a`).")
    print("  - **Leading Underscore**: A name starting with an underscore (e.g., `_internal_value`)")
    print("    is a convention that tells other programmers it's for internal use.")
    print()


def show_reserved_keywords():
    """Prints the list of Python's reserved keywords."""
    print("--- Python Reserved Keywords ---")
    print("These words have special meaning and cannot be used as variable names:")
    # The 'keyword' module provides facilities for checking if a string is a keyword.
    print(keyword.kwlist)
    print()


def demonstrate_dynamic_typing():
    """
    Demonstrates that a variable in Python can refer to different types
    of objects at different times.
    """
    print("--- Dynamic Typing Demonstration ---")
    # A variable is just a name for an object.
    # You can reassign the name to a different object, even of a different type.
    my_variable = 1  # Initially an integer
    print(f"variable_x is '{my_variable}' of type {type(my_variable)}")

    my_variable = 3.75  # Now it's a float
    print(f"variable_x is now '{my_variable}' of type {type(my_variable)}")

    my_variable = "hello"  # And now it's a string
    print(f"variable_x is now '{my_variable}' of type {type(my_variable)}")
    print()


def demonstrate_string_input_and_len():
    """Gets user input and demonstrates string formatting and length."""
    print("--- Input, F-Strings, and Length ---")
    name = input("What's your name?: ")
    greeting = f"Hi {name}, my best regards."
    print(greeting)

    # The len() function returns the number of characters in a string.
    message = f"Did you know that the length of this greeting is {len(greeting)} characters?"
    print(message)
    print()


def main():
    """Main function to demonstrate all concepts."""
    show_naming_conventions()
    show_reserved_keywords()
    demonstrate_dynamic_typing()
    demonstrate_string_input_and_len()


if __name__ == "__main__":
    main()
