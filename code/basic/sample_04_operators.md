# Operators in Python

This example illustrates the various operators available in Python, categorized by their function. The code is structured into separate functions for clarity, with descriptive print statements to make the output easy to understand.

## Code

```python
# MAIN CODE

"""
Example demonstrating various operators in Python.
This version includes descriptive print statements for better clarity.
"""


def demonstrate_arithmetic_operators():
    """Demonstrates basic arithmetic operators."""
    print("--- Arithmetic Operators ---")
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} (Integer Division) = {a // b}")
    print(f"{a} % {b} (Modulo) = {a % b}")
    print(f"{a} ** {b} (Exponent) = {a ** b}")
    print()


def demonstrate_comparison_operators():
    """Demonstrates operators that compare two values."""
    print("--- Comparison Operators ---")
    a, b = 5, 10
    print(f"{a} == {b} -> {a == b}")
    print(f"{a} != {b} -> {a != b}")
    print(f"{a} < {b} -> {a < b}")
    print(f"{a} > {b} -> {a > b}")
    print(f"{a} <= {b} -> {a <= b}")
    print(f"{a} >= {b} -> {a >= b}")
    print()


def demonstrate_logical_operators():
    """Demonstrates 'and', 'or', 'not' operators."""
    print("--- Logical Operators ---")
    p, q = True, False
    print(f"{p} and {q} -> {p and q}")
    print(f"{p} or {q} -> {p or q}")
    print(f"not {p} -> {not p}")
    print()


def demonstrate_assignment_operators():
    """Demonstrates operators for assigning values to variables."""
    print("--- Assignment Operators ---")
    x = 10
    print(f"Initial x = {x}")
    x += 5  # Equivalent to x = x + 5
    print(f"x += 5 -> x = {x}")
    x -= 3  # Equivalent to x = x - 3
    print(f"x -= 3 -> x = {x}")
    x *= 2  # Equivalent to x = x * 2
    print(f"x *= 2 -> x = {x}")
    print()


def demonstrate_membership_operators():
    """Demonstrates 'in' and 'not in' operators for sequences."""
    print("--- Membership Operators ---")
    example_list = [1, 2, 3, 4, 5]
    print(f"List = {example_list}")
    print(f"3 in {example_list} -> {3 in example_list}")
    print(f"6 in {example_list} -> {6 in example_list}")
    print(f"3 not in {example_list} -> {3 not in example_list}")
    print()


def demonstrate_identity_operators():
    """Demonstrates 'is' and 'is not' to check object identity."""
    print("--- Identity Operators ---")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a = {a}, b = {b}, c = a")
    # 'is' checks if two variables point to the exact same object in memory
    print(f"a is b -> {a is b}")
    print(f"a is c -> {a is c}")
    # '==' checks if the values of the objects are equal
    print(f"a == b -> {a == b}")
    print()


def main():
    """Main function to demonstrate all operator types."""
    # Add introductory note about functions, as per user feedback
    print("This script is organized into functions to demonstrate each "
          "operator type clearly.")
    print("We will cover functions in detail in a later example.\n")

    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_assignment_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Arithmetic Operators**: Used for mathematical operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
2.  **Comparison (Relational) Operators**: Used to compare two values and result in a boolean (`True` or `False`) (`==`, `!=`, `<`, `>`, `<=`, `>=`).
3.  **Logical Operators**: Used to combine conditional statements (`and`, `or`, `not`).
4.  **Assignment Operators**: Used to assign values to variables. Compound operators (`+=`, `-=`, etc.) perform an operation and an assignment in one step.
5.  **Membership Operators**: Used to test if a sequence is presented in an object (`in`, `not in`).
6.  **Identity Operators**: Used to compare the memory locations of two objects (`is`, `is not`). This is different from `==`, which compares the values.

## Expected Output

```
This script is organized into functions to demonstrate each operator type clearly.
We will cover functions in detail in a later example.

--- Arithmetic Operators ---
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 // 3 (Integer Division) = 3
10 % 3 (Modulo) = 1
10 ** 3 (Exponent) = 1000

--- Comparison Operators ---
5 == 10 -> False
5 != 10 -> True
5 < 10 -> True
5 > 10 -> False
5 <= 10 -> True
5 >= 10 -> False

--- Logical Operators ---
True and False -> False
True or False -> True
not True -> False

--- Assignment Operators ---
Initial x = 10
x += 5 -> x = 15
x -= 3 -> x = 12
x *= 2 -> x = 24

--- Membership Operators ---
List = [1, 2, 3, 4, 5]
3 in [1, 2, 3, 4, 5] -> True
6 in [1, 2, 3, 4, 5] -> False
3 not in [1, 2, 3, 4, 5] -> False

--- Identity Operators ---
a = [1, 2, 3], b = [1, 2, 3], c = a
a is b -> False
a is c -> True
a == b -> True

```

## Points to Consider

- The distinction between `is` (identity) and `==` (equality) is a key concept. `is` checks if two variables refer to the _same object_ in memory, while `==` checks if the _values_ of the objects are equivalent.
- Operators are fundamental building blocks in Python for performing virtually any computation or logic.
