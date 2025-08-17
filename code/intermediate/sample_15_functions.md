# Functions in Python

Functions are a fundamental building block in Python. They are reusable blocks of code that perform a specific, single, well-defined task. Using functions helps make code more organized, readable, and reusable (following the DRY - Don't Repeat Yourself - principle).

This example demonstrates several key concepts of defining and using functions:

-   Defining a function with parameters.
-   Using the `return` statement to send a value back from a function.
-   Setting default values for parameters to make them optional.
-   Calling functions with both positional and keyword arguments.

## Code

The following code defines two functions, `add_numbers` and `format_full_name`, and then shows various ways to call them in the `main` function.

```python
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
```

## Explanation

### 1. Parameters and `return`

-   The `add_numbers` function is defined with two **parameters**, `a` and `b`. These act as placeholders for the values that will be passed in when the function is called.
-   The `return` keyword is used to send a result back to wherever the function was called. If a function does not have a `return` statement, it implicitly returns `None`.

### 2. Default (Optional) Arguments

-   In the `format_full_name` function, the `reverse` parameter is defined as `reverse=False`. This makes `reverse` an **optional argument** with a default value of `False`.
-   If the caller does not provide a value for `reverse`, it will automatically be `False`. This allows the function to be called in a simpler way, like `format_full_name("John", "Doe")`.

### 3. Positional vs. Keyword Arguments

-   **Positional Arguments**: When you call `add_numbers(5, 3)`, Python matches the values to the parameters based on their order: `a` becomes 5, and `b` becomes 3.
-   **Keyword Arguments**: When you call `format_full_name(last_name="Doe", first_name="John")`, you are explicitly telling Python which value belongs to which parameter, regardless of their order. This can make function calls more readable.

## Expected Output

```
--- Demonstrating `add_numbers` function ---
The result of add_numbers(5, 3) is: 8

--- Demonstrating `format_full_name` function ---
Default order: John Doe
Reversed order: Doe, John
Called with keyword arguments: John Doe
```
