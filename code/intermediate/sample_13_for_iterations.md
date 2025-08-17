# `for` Loops in Python

The `for` loop in Python is a fundamental control flow tool used to iterate over a sequence of items. A "sequence" can be a list, a tuple, a dictionary, a set, or even a string.

This example demonstrates the versatility of the `for` loop by showing how to iterate over different types of sequences.

## Code

The following code is divided into three functions, each demonstrating a common use case for the `for` loop.

```python
# MAIN CODE

"""
Demonstrates the versatility of the `for` loop in Python.

A `for` loop is used for iterating over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string). This is less like the `for`
keyword in other programming languages, and works more like an iterator
method as found in other object-orientated programming languages.
"""


def iterate_over_list():
    """Shows how to iterate over each item in a list."""
    print("--- Example 1: Iterating over a list ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Iterating through the list: {fruits}")
    for fruit in fruits:
        print(f"  - Current fruit: {fruit}")
    print()


def iterate_over_string():
    """Shows that a string is a sequence of characters and can be iterated."""
    print("--- Example 2: Iterating over a string ---")
    word = "Python"
    print(f"Iterating through the characters of the word: '{word}'")
    for letter in word:
        print(f"  - Current letter: {letter}")
    print()


def iterate_with_range():
    """
    Shows how to use the range() function to generate a sequence of numbers
    to loop through, which is useful when you need to perform an action a
    specific number of times.
    """
    print("--- Example 3: Iterating with range() ---")
    # range(5) generates numbers from 0 up to (but not including) 5.
    print("Looping from 0 to 4 using range(5):")
    for number in range(5):
        print(f"  - Current number: {number}")
    print()


def main():
    """Main function to demonstrate all `for` loop examples."""
    iterate_over_list()
    iterate_over_string()
    iterate_with_range()


if __name__ == "__main__":
    main()
```

## Explanation

### 1. Iterating over a List

-   **Concept**: This is the most common use of a `for` loop. The loop assigns each item from the `fruits` list to the `fruit` variable, one by one, and executes the indented code block for each item.
-   **Expected Output**:
    ```
    --- Example 1: Iterating over a list ---
    Iterating through the list: ['apple', 'banana', 'cherry']
      - Current fruit: apple
      - Current fruit: banana
      - Current fruit: cherry
    ```

### 2. Iterating over a String

-   **Concept**: A string is a sequence of characters. A `for` loop can iterate through each character of a string in the same way it iterates through the items of a list.
-   **Expected Output**:
    ```
    --- Example 2: Iterating over a string ---
    Iterating through the characters of the word: 'Python'
      - Current letter: P
      - Current letter: y
      - Current letter: t
      - Current letter: h
      - Current letter: o
      - Current letter: n
    ```

### 3. Iterating with `range()`

-   **Concept**: The `range()` function generates a sequence of numbers. It's incredibly useful when you need to execute a block of code a specific number of times. `range(n)` generates numbers from `0` up to, but not including, `n`.
-   **Expected Output**:
    ```
    --- Example 3: Iterating with range() ---
    Looping from 0 to 4 using range(5):
      - Current number: 0
      - Current number: 1
      - Current number: 2
      - Current number: 3
      - Current number: 4
    ```

## Points to Consider

-   The `for` loop is generally more readable and less error-prone than a `while` loop when you need to iterate over a known sequence of items.
-   You can iterate over many other types of objects in Python, such as tuples, dictionaries, and sets.
