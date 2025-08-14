# String Operations in Python

This example demonstrates various common operations that can be performed on strings in Python. The code is structured into separate functions to clearly illustrate each concept, introducing basic formatting first and then the more modern f-string method.

## Code

```python
# MAIN CODE

"""
Example demonstrating various string operations in Python.

A note on functions:

- This code is organized into 'functions' (e.g., `def demonstrate_slicing():`).
- A function is a reusable block of code that performs a specific task.
- Using functions helps keep our code clean, organized, and easy to read.
- We will cover functions in much more detail in a later example (sample_15_functions.py).
"""


def demonstrate_concatenation_and_repetition():
    """Demonstrates string concatenation and repetition."""
    print("--- Concatenation and Repetition ---")
    first_string = "123"
    second_string = "456"
    hip_string = "Hip"
    hurra_string = "Hurra"

    # Simple concatenation using the '+' operator
    concatenated = first_string + second_string
    print("'", first_string, "' + '", second_string, "' = '", concatenated,
        "'", sep="")

    # Repetition using the '*' operator
    triplicate = first_string * 3
    print("'", first_string, "' * 3 = '", triplicate, "'", sep="")

    # Combined repetition and concatenation
    cheer = ((hip_string + " ") * 2) + hurra_string
    print("Cheer example:", cheer)
    print()


def demonstrate_length_and_indexing():
    """Demonstrates calculating length and accessing characters by index."""
    print("--- Length and Indexing ---")
    large_string = """This is a large string
    that spans multiple lines
    and contains various characters."""
    world_string = "World"

    # Get the total number of characters in a string
    print("Length of the large string is:", len(large_string))

    # Access individual characters using zero-based indexing
    print("First character of 'World':", world_string[0])
    print("Third character of 'World':", world_string[2])
    print("Last character of 'World':", world_string[-1])
    print()


def demonstrate_slicing():
    """Demonstrates extracting substrings using slicing."""
    print("--- String Slicing ---")
    world_string = "World"

    # Slice from index 2 to the end
    print("Slice [2:]:", world_string[2:])

    # Slice from the beginning to index 3 (exclusive)
    print("Slice [:3]:", world_string[:3])

    # Slice from the beginning to the second-to-last character
    print("Slice [:-1]:", world_string[:-1])

    # Slice with a step (every second character)
    print("Slice [::2]:", world_string[::2])
    print()


def demonstrate_f_strings():
    """Demonstrates the use of f-strings for modern formatting."""
    print("--- F-String Formatting (Modern Method) ---")
    world_string = "World"

    # Embedding variables directly into a string
    sentence = f"I am a citizen of the {world_string}"
    print("f-string sentence:", sentence)

    # Repetition with f-strings
    repeated = f"I am a citizen of the {world_string}, " * 2
    print("f-string repeated:", repeated)
    print()


def main():
    """Main function to demonstrate all string operations."""
    demonstrate_concatenation_and_repetition()
    demonstrate_length_and_indexing()
    demonstrate_slicing()
    demonstrate_f_strings()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Concatenation**: Joining two or more strings together using the `+` operator.
2.  **Repetition**: Repeating a string multiple times using the `*` operator.
3.  **Length (`len()`)**: Calculating the total number of characters in a string.
4.  **Indexing**: Accessing individual characters in a string using their numerical index (starting from 0).
5.  **Slicing**: Extracting a portion of a string using a `[start:stop:step]` syntax.
6.  **F-Strings**: A modern and readable way to embed expressions and variables inside string literals. This is often the preferred method for string formatting.

## Expected Output

```
--- Concatenation and Repetition ---
'123' + '456' = '123456'
'123' * 3 = '123123123'
Cheer example: Hip Hip Hurra

--- Length and Indexing ---
Length of the large string is: 67
First character of 'World': W
Third character of 'World': r
Last character of 'World': d

--- String Slicing ---
Slice [2:]: rld
Slice [:3]: Wor
Slice [:-1]: Worl
Slice [::2]: Wrd

--- F-String Formatting (Modern Method) ---
f-string sentence: I am a citizen of the World
f-string repeated: I am a citizen of the World, I am a citizen of the World,

```

## Points to Consider

-   **Modularity**: Structuring code into smaller, single-purpose functions makes it easier to read, test, and maintain.
-   **Immutability**: Strings in Python are immutable. Operations like concatenation or slicing don't change the original string; they create and return a new one.
-   **Formatting**: While older methods like using commas in `print` work, f-strings are generally preferred in modern Python for their clarity and power.
