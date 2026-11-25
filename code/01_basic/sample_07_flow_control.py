"""Demonstrates conditional flow control with if-elif-else, 'and', and nested checks."""


def demonstrate_if_elif_else():
    """Compares two integers using an if-elif-else chain."""
    print("--- Example 1: Basic if-elif-else ---")
    # int() raises ValueError on non-numeric input; handled safely in sample_18.
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
    """Classifies an age into ranges using logical 'and'."""
    print("--- Example 2: Flow Control with Logical 'and' ---")
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    elif age >= 0 and age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    print()


def demonstrate_nested_if():
    """Uses nested conditionals to verify role and active status."""
    print("--- Example 3: Nested if Statements ---")
    # Strip whitespace and normalize casing before comparing user text.
    user_role = input("Enter user role (admin/user): ").strip().lower()
    is_active_str = input("Is the user active? (yes/no): ").strip().lower()

    if user_role == "admin":
        print("Admin access granted.")
        if is_active_str == "yes":
            print("User is active and can make changes.")
        else:
            print("User is inactive and has read-only access.")
    else:
        print("General user access granted.")
    print()


def main():
    """Runs all flow control demonstrations."""
    demonstrate_if_elif_else()
    demonstrate_logical_flow()
    demonstrate_nested_if()


if __name__ == "__main__":
    main()
