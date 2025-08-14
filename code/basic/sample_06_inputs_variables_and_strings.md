# Python Fundamentals: Naming, Keywords, and Dynamic Typing

This example demonstrates several fundamental concepts in Python, structured as a mini-lesson. It covers:

-   Best practices and conventions for naming variables, functions, and classes according to PEP 8.
-   How to see Python's list of reserved keywords.
-   The concept of "dynamic typing," where a variable can hold different data types.
-   A practical example combining user input, f-strings, and the `len()` function.

## Code

```python
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
```

## Explanation

1.  **Naming Conventions (PEP 8)**: The script begins by printing a comprehensive guide to Python's standard naming conventions. Following these makes code more readable and consistent with the wider Python community. The key styles are `snake_case` for variables/functions, `PascalCase` for classes, and `ALL_CAPS` for constants.

2.  **Reserved Keywords**: It then imports the `keyword` module to print a list of all reserved words in Python (like `if`, `for`, `def`, etc.). These words have special functions and cannot be used as names for your variables.

3.  **Dynamic Typing**: This section shows one of Python's core features. A variable (`my_variable`) is first assigned an integer, then a float, and finally a string. The `type()` function confirms that the variable's type changes along with the object it points to.

4.  **Input, F-Strings, and `len()`**: The final part combines concepts. It takes user input, uses an f-string to create a personalized greeting, and then uses the `len()` function to calculate and report the length of that greeting.

## Expected Output

The output will be a sequence of informational sections, with the last part being interactive. An example session might look like this (the keyword list may vary slightly between Python versions):

```
--- Naming Conventions (PEP 8) ---
The most common and important conventions are:
  - `snake_case`: Used for variables and functions. It's the standard for most names.
    (e.g., `user_name`, `calculate_total()`).
  - `PascalCase`: Used for classes. This is a key distinction from variables.
    (e.g., `class MyNewClass:`).
  - `ALL_CAPS`: Used for constants — variables whose values are not intended to change.
    (e.g., `PI = 3.14`, `MAX_CONNECTIONS = 5`).

Other Important Considerations:
  - **Descriptiveness**: Names should be clear and descriptive, not single letters.
    (e.g., `customer_address` is better than `addr` or `c_a`).
  - **Leading Underscore**: A name starting with an underscore (e.g., `_internal_value`)
    is a convention that tells other programmers it's for internal use.

--- Python Reserved Keywords ---
These words have special meaning and cannot be used as variable names:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

--- Dynamic Typing Demonstration ---
variable_x is '1' of type <class 'int'>
variable_x is now '3.75' of type <class 'float'>
variable_x is now 'hello' of type <class 'str'>

--- Input, F-Strings, and Length ---
What's your name?: Alex
Hi Alex, my best regards.
Did you know that the length of this greeting is 25 characters?

```

## Points to Consider

-   Adhering to PEP 8 naming conventions is highly recommended as it makes your code more readable to other Python developers.
-   Python's flexibility with dynamic typing is powerful, but it also means you need to be mindful of what type of data your variables are holding at any given time.
-   To help manage the flexibility of dynamic typing and prevent errors, modern Python supports **Type Hinting**, which allows you to declare the expected type of a variable. This is an advanced topic covered in `sample_23_type_hinting.py`.
