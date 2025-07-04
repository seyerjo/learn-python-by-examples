# MAIN CODE

"""Demonstrate robust input validation using try-except blocks.

This example shows how to prevent program crashes when users provide invalid
input (e.g., non-numeric text when an integer is expected) by catching ValueError
and prompting the user to try again.
"""


def get_integer_input(prompt):
    """
    Continuously prompts the user for an integer input until a valid one is provided.

    This function uses a try-except block to gracefully handle ValueError
    if the user enters non-integer text, ensuring the program does not crash.

    Args:
        prompt (str): The message displayed to the user to solicit input.

    Returns:
        int: The valid integer entered by the user.

    Examples:
        >>> get_integer_input("Enter a number: ")
        Enter a number: abc
        Invalid input. Please enter a whole number.
        Enter a number: 123
        123
    """
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """
    Main function to demonstrate robust integer input validation using try-except.

    It collects an integer input from the user, displaying how
    invalid inputs are handled without crashing the program.
    """
    print("--- Integer Input Validation Example ---")
    age = get_integer_input("Please enter your age: ")
    print(f"Thank you. You have entered {age} as your age.\n")


if __name__ == "__main__":
    main()
