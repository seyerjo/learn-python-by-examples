# Algorithm: Exhaustive Enumeration (Guess and Check)

This example demonstrates the **exhaustive enumeration** algorithm, a fundamental brute-force technique also known as "guess and check." We apply it to a classic problem: finding the integer square root of a number.

## Concept

Exhaustive enumeration works by trying every possible candidate for a solution until the correct one is found. For a problem to be solvable with this method, the set of possible answers must be enumerable (countable or listable).

In this specific example:

1.  **Problem**: Find the integer `x` such that `x * x = target`.
2.  **Possible Solutions**: The set of all integers starting from 0 up to the target number.
3.  **Algorithm**:
    -   Start guessing with `guess = 0`.
    -   Check if `guess * guess == target`.
    -   If not, increment the guess (`guess = 1`, `guess = 2`, etc.) and check again.
    -   Stop when `guess * guess` is equal to or greater than the target.

This method is simple to understand but can be very inefficient, especially for large numbers.

## Code

The following code implements the "guess and check" algorithm to find the integer square root of a user-provided number.

```python
# MAIN CODE

"""
Demonstrates the EXHAUSTIVE ENUMERATION algorithm, also known as GUESS AND CHECK.

This algorithm finds a solution to a problem by trying every possible answer
(enumerating all possibilities) until the correct one is found. It is a simple
brute-force approach.

This example uses it to find the integer square root of a number.
"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`, `-> int`).       #
# ############################################################################ #


def find_square_root(target: int) -> None:
    """
    Finds the integer square root of a target number using exhaustive enumeration.

    Args:
        target (int): The number to find the square root of.
    """
    guess: int = 0
    iterations: int = 0

    # We keep guessing until our guess squared is greater than or equal to the target.
    while guess**2 < target:
        guess += 1
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")

    # After the loop, we check if we found an exact square root.
    if guess**2 == target:
        print(f"The exact square root of {target} is {guess}.")
    else:
        print(f"{target} does not have an exact integer square root.")


def main() -> None:
    """
    Main function to get user input and run the algorithm.
    """
    print("--- Exhaustive Enumeration: Integer Square Root Finder ---")

    # Get a valid non-negative integer from the user.
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
    find_square_root(target_number)
    print()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **`main()` function**: This function is responsible for the user interaction. It prompts the user to enter a non-negative integer and uses a `while True` loop with `try-except` to ensure the input is valid before proceeding.
2.  **`find_square_root(target)` function**: This is where the core algorithm resides.
    -   It initializes `guess` and `iterations` to `0`.
    -   The `while guess**2 < target:` loop is the "guess and check" engine. It continues as long as the square of our guess is less than the target number.
    -   Inside the loop, it increments `guess` and `iterations` by 1.
    -   When the loop terminates, it means `guess**2` is no longer less than `target`. The final `if` statement checks if we landed exactly on the target (`guess**2 == target`) or overshot it.
3.  **Efficiency**: The `iterations` counter is included to show how many guesses the algorithm had to make. Try running the code with a large number (e.g., 1,000,000) to see how inefficient this method can be.

## Expected Output

### Scenario 1: Perfect Square

```
--- Exhaustive Enumeration: Integer Square Root Finder ---
Enter a non-negative integer: 81

Algorithm finished after 9 iterations.
The exact square root of 81 is 9.

```

### Scenario 2: Not a Perfect Square

```
--- Exhaustive Enumeration: Integer Square Root Finder ---
Enter a non-negative integer: 80

Algorithm finished after 9 iterations.
80 does not have an exact integer square root.
```
