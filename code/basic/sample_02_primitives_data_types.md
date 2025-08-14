# Primitive Data Types in Python

This example illustrates the basic data types available in Python, including numeric types, sequences, mappings, and more.

## Code

```python
# MAIN CODE

"""Example demonstrating various primitive data types in Python."""


def main():
    """Main function to demonstrate example usage."""
    # Variables of different data types.
    integer_variable = 1
    float_variable = 3.14
    complex_variable = 1 + 2j
    string_variable = "Hello, Coder!"
    list_variable = [1, 2, 3]
    tuple_variable = (4.0, 5.5, 6.9)
    dictionary_variable = {"key": "value"}
    set_variable = {7, 8, 9}
    boolean_variable = False
    none_variable = None

    # Using the 'type' function to determine data types.
    print(type(integer_variable))       # int
    print(type(float_variable))         # float
    print(type(complex_variable))       # complex
    print(type(string_variable))        # str
    print(type(list_variable))          # list
    print(type(tuple_variable))         # tuple
    print(type(dictionary_variable))    # dictionary
    print(type(set_variable))           # set
    print(type(boolean_variable))       # bool
    print(type(none_variable))          # NoneType


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Integers (`int`)**: Whole numbers, like `1`, `10`, or `-5`.
2.  **Floats (`float`)**: Numbers with a fractional part, like `3.14` or `-0.5`.
3.  **Complex (`complex`)**: Numbers with a real and imaginary part, like `1 + 2j`.
4.  **Strings (`str`)**: Sequences of characters, like `"Hello, Coder!"`.
5.  **Lists (`list`)**: Ordered, mutable sequences of items, like `[1, 2, 3]`.
6.  **Tuples (`tuple`)**: Ordered, immutable sequences of items, like `(4.0, 5.5, 6.9)`.
7.  **Dictionaries (`dict`)**: Unordered collections of key-value pairs, like `{"key": "value"}`.
8.  **Sets (`set`)**: Unordered collections of unique items, like `{7, 8, 9}`.
9.  **Booleans (`bool`)**: Logical values that can be either `True` or `False`.
10. **NoneType (`None`)**: Represents the absence of a value.

## Expected Output

When you run this code, you should see the following output, which shows the class (type) of each variable:

```
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
<class 'bool'>
<class 'NoneType'>
```

## Points to Consider

-   Python is a dynamically-typed language, meaning you don't have to explicitly declare the data type of a variable.
-   The `type()` function is a useful built-in tool for debugging and understanding the data you are working with.
-   **Mutability**: Some types are _mutable_ (their value can change), like `list`, `dict`, and `set`. Others are _immutable_ (their value cannot change after creation), like `int`, `float`, `str`, and `tuple`.
