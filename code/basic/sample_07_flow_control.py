# MAIN CODE

"""
Demonstrates basic flow control in Python using if-elif-else,
logical operators, and nested if statements.
"""


def demonstrate_if_elif_else():
    """Compares two integers to show basic if-elif-else structure."""
    print("--- Example 1: Basic if-elif-else ---")
    # IMPORTANT: The int() function will cause a ValueError if you enter
    # non-numeric text. A robust solution is covered in sample_18.
    num_1 = int(input("Enter the first integer: "))
    num_2 = int(input("Enter the second integer: "))

    if num_1 > num_2:
        result = f"The first number ({num_1}) is greater than the second ({num_2})."
    elif num_1 < num_2:
        result = f"The second number ({num_2}) is greater than the first ({num_1})."
    else:
        result = f"Both numbers are equal ({num_1})."
    print(f"Result: {result}\n")


def demonstrate_logical_flow():
    """Uses the 'and' operator to check if a number is within a range."""
    print("--- Example 2: Flow Control with Logical 'and' ---")
    # IMPORTANT: Vulnerable to ValueError. See sample_18 for the solution.
    age = int(input("Enter your age: "))

    if age > 0 and age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    print()


def demonstrate_nested_if():
    """Shows a nested if statement to check a sub-condition."""
    print("--- Example 3: Nested if Statements ---")
    # Using .lower() to make the comparison case-insensitive
    user_role = input("Enter user role (admin/user): ").lower()
    is_active_str = input("Is the user active? (yes/no): ").lower()

    if user_role == "admin":
        print("Admin access granted.")
        # This 'if' is nested inside the first one.
        if is_active_str == "yes":
            print("User is active and can make changes.")
        else:
            print("User is inactive and has read-only access.")
    else:
        print("General user access granted.")
    print()


def main():
    """Main function to demonstrate all flow control examples."""
    demonstrate_if_elif_else()
    demonstrate_logical_flow()
    demonstrate_nested_if()


if __name__ == "__main__":
    main()
