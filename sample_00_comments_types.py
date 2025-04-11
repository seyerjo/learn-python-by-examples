# MAIN CODE

# This is a single-line comment.

"""
This is a multi-line comment also
known as a docstring. It is often used
to document functions, classes, modules, etc.
"""

# Inline comment after a line of code.
number_x = 10  # This is an inline comment.

# Inline comment and a multi-line comment with single quotes inside a function.


def my_function():
    '''This function calculates
    the square of a number.'''
    number_y = 5
    # Calculates the square.
    number_z = number_y * number_y
    return number_z


# Comment before a function call.
result = my_function()
print(result)  # Inline comment after a function call.

# Code commented ignored by the interpreter.
# if True:
#    print("This code will not be executed")

# Comment explaining a complex part of the code.
# The following code block handles the ZeroDivisionError exception.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
