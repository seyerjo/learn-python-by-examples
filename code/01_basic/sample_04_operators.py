"""Demonstrates Python's arithmetic, comparison, logical, and identity operators."""


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
    print(f"{a} ** {b} (Exponent) = {a**b}")
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
    """Demonstrates 'and', 'or', and 'not' operators."""
    print("--- Logical Operators ---")
    p, q = True, False
    print(f"{p} and {q} -> {p and q}")
    print(f"{p} or {q} -> {p or q}")
    print(f"not {p} -> {not p}")
    print()


def demonstrate_assignment_operators():
    """Demonstrates compound assignment operators."""
    print("--- Assignment Operators ---")
    x = 10
    print(f"Initial x = {x}")
    x += 5  # Shorthand for x = x + 5
    print(f"x += 5 -> x = {x}")
    x -= 3
    print(f"x -= 3 -> x = {x}")
    x *= 2
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
    """Demonstrates 'is' and '==' to contrast identity with value equality."""
    print("--- Identity Operators ---")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a = {a}, b = {b}, c = a")
    # 'is' compares memory identity; '==' compares values.
    print(f"a is b -> {a is b}")
    print(f"a is c -> {a is c}")
    print(f"a == b -> {a == b}")
    print()


def main():
    """Runs all operator category demonstrations."""
    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_assignment_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()


if __name__ == "__main__":
    main()
