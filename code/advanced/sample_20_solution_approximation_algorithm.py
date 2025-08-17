# MAIN CODE

"""
Demonstrates the SOLUTION APPROXIMATION algorithm.

This type of algorithm is used to find a solution that is "close enough" when
an exact solution is either impossible or too computationally expensive to find.
It works by starting with a guess and iteratively improving it until the guess
is within a specified margin of error (epsilon).

This example uses it to find an approximate square root of a number.
"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`, `-> int`).       #
# ############################################################################ #


def find_root_by_approximation(target: int) -> None:
    """
    Finds an approximate square root of a target number.

    Args:
        target (int): The number to find the square root of.
    """
    # Epsilon is the margin of error we are willing to accept.
    epsilon: float = 0.01
    # The step is how much we increment our guess in each iteration.
    step: float = epsilon**2
    guess: float = 0.0
    iterations: int = 0

    # The loop continues as long as our guess is not "close enough"
    # (i.e., the error is greater than epsilon).
    # We also check `guess <= target` to prevent infinite loops for negative numbers,
    # although our main function already validates for non-negative input.
    while abs(guess**2 - target) >= epsilon and guess <= target:
        guess += step
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")

    # After the loop, we check if the final guess is within the margin of error.
    if abs(guess**2 - target) < epsilon:
        print(f"The approximate square root of {target} is {guess:.4f}")
    else:
        print(
            f"Failed to find the square root of {target} within the allowed error.")


def main() -> None:
    """
    Main function to get user input and run the algorithm.
    """
    print("--- Solution Approximation: Square Root Finder ---")

    # Get a valid integer from the user.
    # Note: This algorithm works for negative numbers, but the concept of a
    # real square root for them is undefined. We will stick to non-negatives.
    while True:
        try:
            target_number: int = int(input("Enter a non-negative integer: "))
            if target_number < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print()  # Add a blank line for readability.
    find_root_by_approximation(target_number)
    print()


if __name__ == "__main__":
    main()
