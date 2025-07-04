""" ROBUST INPUT VALIDATION

    When writing interactive programs, it's crucial to anticipate that users
    might not always provide the input you expect. If your program expects an
    integer but receives text, it will crash with a `ValueError`.

    Robust input validation is the practice of creating a loop that repeatedly
    asks the user for input until they provide data in the correct format. This
    prevents crashes and provides a much better user experience.

    The most common pattern for this in Python is to use a `while True` loop
    combined with a `try-except` block.

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> int`, `-> None`).       #
# ############################################################################ #


def get_valid_integer(prompt: str) -> int:
    """Continuously prompts the user until a valid integer is entered.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        int: The validated integer provided by the user.
    """
    while True:  # Start an infinite loop
        try:
            # Attempt to get input and convert it to an integer
            user_input: str = input(prompt)
            return int(user_input)
        except ValueError:
            # If a ValueError occurs, the input was not a valid integer.
            # Inform the user and the loop will continue to the next iteration.
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    """Main function to demonstrate robust input validation."""
    print("Let's get your age.")

    # The vulnerable way (uncomment to see it crash with non-numeric input)
    # age = int(input("Please enter your age: "))

    # The robust way
    age: int = get_valid_integer("Please enter your age: ")
    print(f"\nThank you. You have entered {age} as your age.")


if __name__ == "__main__":
    main()
