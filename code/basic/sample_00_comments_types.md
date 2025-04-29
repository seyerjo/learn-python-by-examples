# Comments and Data Types in Python

This example illustrates how to use comments and basic data types in Python.

## Code

```python
# This is a single-line comment. Anything written after the "#" symbol on the same line is ignored by Python.

"""
This is a multi-line comment or docstring. It can span multiple lines and is often used to provide a description of a function, class, or module.
"""

# Basic data types in Python include integers, floats, strings, and booleans.

# Integer: a whole number, either positive, negative, or zero.
integer = 10  # int
print("Integer:", integer)

# Float: a number with a fractional part.
float_num = 3.14  # float
print("Float:", float_num)

# String: a sequence of characters, such as letters, numbers, or symbols, enclosed in quotes.
string = "Hello, world!"  # str
print("String:", string)

# Boolean: a logical value that can be either True or False.
boolean = True  # bool
print("Boolean:", boolean)
```

## Explanation

1. **Comments**: Comments are used to explain what the code is doing. They are ignored by the Python interpreter, so they don't affect how the code runs. There are two main types of comments:

   - **Single-line comments**: Start with the `#` symbol and continue until the end of the line.
   - **Multi-line comments or docstrings**: Enclosed between triple double quotes `""" """`. These are often used at the beginning of functions, classes, or modules to describe what they do.

2. **Basic Data Types**: Python has several basic data types that are used to store different kinds of data.

   - **Integers (`int`)**: Whole numbers, like 1, 2, 3, etc. They can be positive, negative, or zero.
   - **Floats (`float`)**: Numbers with a fractional part, like 3.14 or -0.5.
   - **Strings (`str`)**: Sequences of characters, like "hello" or 'hello'. Strings are enclosed in quotes (either single, double, or triple quotes).
   - **Booleans (`bool`)**: Logical values that can be either `True` or `False`.

3. **Printing Values**: The `print()` function is used to output the values of variables to the screen. This is a simple way to see what your code is doing.

## Expected Output

When you run this code, you should see the following output:

```
Integer: 10
Float: 3.14
String: Hello, world!
Boolean: True
```

## Points to Consider

- **Readability**: Using clear and descriptive variable names and adding comments can make your code much easier to understand.
- **Data Types**: Understanding the different data types available in Python and when to use them is crucial for writing effective code.
- **Practice**: Try changing the values of the variables and see how it affects the output. Experimenting with different data types and operations can help solidify your understanding.
