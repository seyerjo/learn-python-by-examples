# MAIN CODE

# This is a single-line comment.

"""
This is a multi-line comment also known as a docstring.
It is often used at the beginning of a module, function,
or class to document functions, classes, modules, etc.
"""

# Inline comment after a line of code.
INITIAL_VALUE = 10  # This is an inline comment.

# Example of a functions with a docstring.

# This function calculates the square of a number.


def calculate_square(number):
    """Calculate the square of a number."""
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