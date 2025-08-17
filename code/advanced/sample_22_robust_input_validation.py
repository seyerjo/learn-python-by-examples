# MAIN CODE

"""
Demonstrates a ROBUST AND REUSABLE INPUT VALIDATION function.

A common task in programming is getting a specific type of numerical input
from a user within a certain range. This example builds a single, flexible
function that can be reused for integers, floats, and ranges.

The core pattern remains a `while True` loop combined with `try-except`.
"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> int`, `-> None`).       #
# ############################################################################ #

from typing import Union, Type


def get_valid_number(
    prompt: str,
    num_type: Type[Union[int, float]] = int,
    min_val: Union[int, float] = None,
    max_val: Union[int, float] = None,
) -> Union[int, float]:
    """
    Continuously prompts the user until a valid number of a specific type and
    within a specific range is entered.

    Args:
        prompt (str): The message to display to the user.
        num_type (type): The required number type (e.g., `int` or `float`).
        min_val (int or float, optional): The minimum allowed value.
        max_val (int or float, optional): The maximum allowed value.

    Returns:
        A valid number of the specified type and within the specified range.
    """
    while True:
        try:
            # 1. Attempt to get and convert the input to the desired type.
            user_input = input(prompt)
            number = num_type(user_input)

            # 2. Check if the number is above the minimum value.
            if min_val is not None and number < min_val:
                print(f"Error: The value must be at least {min_val}.")
                continue  # Ask for input again.

            # 3. Check if the number is below the maximum value.
            if max_val is not None and number > max_val:
                print(f"Error: The value must be no more than {max_val}.")
                continue  # Ask for input again.

            # 4. If all checks pass, return the valid number.
            return number

        except ValueError:
            # This catches errors from the type conversion (e.g., `int("abc")`).
            print(f"Invalid input. Please enter a valid {num_type.__name__}.")


def main() -> None:
    """Main function to demonstrate robust and flexible input validation."""
    print("--- Demonstrating a general-purpose number validation function ---\n")

    # Example 1: Get any integer.
    age = get_valid_number("Please enter your age (any integer): ")
    print(f"Valid age entered: {age}\n")

    # Example 2: Get a float between 0.0 and 1.0.
    probability = get_valid_number(
        "Enter a probability (a decimal between 0.0 and 1.0): ",
        num_type=float,
        min_val=0.0,
        max_val=1.0,
    )
    print(f"Valid probability entered: {probability}\n")

    # Example 3: Get an integer within a specific range.
    rating = get_valid_number(
        "Please rate our service (an integer from 1 to 5): ",
        num_type=int,
        min_val=1,
        max_val=5,
    )
    print(f"Valid rating entered: {rating}\n")


if __name__ == "__main__":
    main()
