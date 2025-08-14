# MAIN CODE

"""
Example demonstrating various operators in Python.
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
    print(f"a is b -> {a is b}")  # False, they are different objects
    print(f"a is c -> {a is c}")  # True, they point to the same object
    # '==' checks if the values of the objects are equal
    print(f"a == b -> {a == b}")  # True, their contents are the same
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
