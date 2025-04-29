# MAIN CODE

"""Example demonstrating various operators in Python."""


def demonstrate_arithmetic_operators():
    """Demonstrate arithmetic operators."""
    # Arithmetic operators
    sum_result = 10 + 5  # Result: 15
    difference = 20 - 8  # Result: 12
    product = 3 * 7  # Result: 21
    quotient = 15 / 3  # Result: 5.0
    print(sum_result, difference, product, quotient)
    print()

    # Integer division operator (//)
    integer_division = 10 // 3  # Result: 3
    print(integer_division)
    print()

    # Exponent operator (**)
    power = 2 ** 3  # 2 to the power of 3 = 8
    print(power)
    print()

    # Modulo operator (%), returns division remainder
    remainder = 10 % 3  # 10 divided by 3 equals 3 with remainder 1
    print(remainder)
    print()


def demonstrate_comparison_operators():
    """Demonstrate comparison operators."""
    print(5 == 5)   # True
    print(4 != 2)   # True
    print(6 < 3)    # False
    print(5 < 10)   # True
    print(7 >= 9)   # False
    print(2 <= 10)  # True
    print()


def demonstrate_logical_operators():
    """Demonstrate logical operators."""
    # Logical operators (and, or, not)
    print(True and False)  # False
    print(True or False)   # True
    print(not True)        # False
    print()


def demonstrate_assignment_operators():
    """Demonstrate assignment operators."""
    # Assignment operators (=, +=, -=)
    initial_value = 10    # Basic assignment
    print(initial_value)
    initial_value += 5    # Equivalent to initial_value = initial_value + 5
    print(initial_value)
    initial_value -= 3    # Equivalent to initial_value = initial_value - 3
    print(initial_value)
    print()


def demonstrate_membership_operators():
    """Demonstrate membership operators."""
    # Membership operators (in, not in)
    example_list = [1, 2, 3]
    print(2 in example_list)       # True
    print(4 not in example_list)   # True
    print()


def demonstrate_identity_operators():
    """Demonstrate identity operators."""
    # Identity operators (is, is not)
    num1 = 5
    num2 = 5
    print(num1 is num2)    # True for small integers
    print()
    print(num1 is not num2)  # False


def main():
    """Main function to demonstrate example usage."""
    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_assignment_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()


if __name__ == "__main__":
    main()
