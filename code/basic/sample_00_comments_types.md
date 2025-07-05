# Types of Comments in Python

This example illustrates the different ways to use comments in Python to document and explain the code.

## Code

```python
# MAIN CODE

#  This is a single-line comment.

"""
This is a multi-line comment also known as a docstring.
It is often used at the beginning of a module, function,
or class to document functions, classes, modules, etc.
"""

# Inline comment after a line of code.
INITIAL_VALUE = 10  # This is an inline comment.

# Example of a function with a docstring.


def calculate_square(number):
    """Calculate the square of a number.

    Args:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    square_value = number * number
    return square_value


# Example of calling a function and printing the result.


def main():
    """Main function to demonstrate example usage."""
    # Call the function and print the result.
    calculation_result = calculate_square(5)
    # The print() function is used to output text to the console.
    print(calculation_result)  # Inline comment after a function call.


if __name__ == "__main__":
    main()


# Code commented out, ignored by the interpreter.
# if True:
#     print("This code will not be executed")

# Comment explaining a part of the code.
# The following code block handles the ZeroDivisionError exception.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Explanation

1.  **Single-Line Comments**: Start with the `#` symbol. Python ignores everything from the `#` to the end of the line. They are useful for brief explanations.

2.  **Inline Comments**: These are single-line comments placed on the same line as a statement. They should be used sparingly and are useful for explaining specific parts of a line of code.

3.  **Multi-Line Comments (Docstrings)**: Enclosed in triple quotes (`"""..."""` or `'''...'''`). While the interpreter does not ignore them like `#` comments (they become string literals), they are the standard convention for writing documentation for modules, classes, and functions. This documentation can be accessed at runtime using `help()`.

4.  **Function Docstrings**: As shown in the `calculate_square` function, docstrings are crucial for explaining what a function does, its arguments (`Args`), and what it returns (`Returns`). This is a key practice for writing maintainable code.

5.  **Commenting Out Code**: You can use `#` at the beginning of one or more lines to temporarily disable code without deleting it. This is useful for debugging.

6.  **Main Execution Block**: The `if __name__ == "__main__":` block is standard Python practice. It ensures that the code inside the `main()` function only runs when the script is executed directly, and not when it's imported as a module into another script.

7.  **Descriptive Comments**: Comments can also be used to explain the purpose of a subsequent block of code, as seen before the `try...except` block.

## Expected Output

When you run this code, you should see the following output:

```
25
Cannot divide by zero!
```

## Points to Consider

- **Why use comments?** Comments make code more readable and easier to maintain, both for other developers and for your future self.
- **Good vs. Bad Comments**: Good comments explain _why_ the code is doing something, not _what_ it is doing. The `what` should be clear from the code itself (e.g., using good variable names).
- **Docstrings are for Documentation**: Always use docstrings for any public function, class, or module. Tools can automatically generate documentation from them.
