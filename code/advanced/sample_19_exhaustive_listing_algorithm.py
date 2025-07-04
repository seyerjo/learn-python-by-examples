""" EXHAUSTIVE LISTING algorithm, also called GUESS AND CHECK.

    The exhaustive enumeration algorithm is a method of finding the optimal
    solution to a given problem. It uses a brute-force search of all possible
    solutions to a problem to find the best solution. This means the algorithm
    reviews all possible options and tries to evaluate each one to find the
    best solution. The exhaustive enumeration algorithm is useful when the
    number of possible solutions is small. However, it is inefficient when the
    number of possible solutions is large, as it would have to review each
    solution to find the best one.

    This Python code is an example of the Exhaustive Listing algorithm, also
    called Guess and Check. The algorithm requests the user to enter an integer
    number, then it iterates by adding one to the response until it is obtained
    that the square of the response is equal to the number entered by the user.
    If so, then the square root of the number can be calculated and if not, then
    the number entered by the user does not have an exact square root. 

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`).                 #
# ############################################################################ #


def main() -> None:
    """Main function to demonstrate exhaustive listing algorithm."""
    # Get a valid integer from the user
    while True:
        try:
            target_number: int = int(input("Enter an integer number: "))
            if target_number < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print()  # Blank line

    # Find square root by exhaustive listing
    guess: int = 0
    while guess**2 < target_number:
        print(guess)  # Show current guess
        guess += 1    # Increment guess

    print()  # Blank line

    # Check if perfect square was found
    if guess**2 == target_number:
        print(f"The square root of {target_number} is {guess}")
    else:
        print(f"{target_number} does not have an exact square root")


if __name__ == "__main__":
    main()
