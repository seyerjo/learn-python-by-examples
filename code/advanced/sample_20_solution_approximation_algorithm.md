# Algorithm: Solution Approximation

This example demonstrates a **solution approximation** algorithm. This type of algorithm is used when finding an exact solution to a problem is too difficult or computationally expensive. Instead, we find an answer that is "close enough" to the real solution.

## Concept

The core idea is to start with a guess and iteratively improve it until it falls within an acceptable margin of error.

In this example, we find the approximate square root of a number:

1.  **Problem**: Find a number `x` such that `x * x` is very close to a `target` number.
2.  **Margin of Error (`epsilon`)**: We define a small value, `epsilon`, which is the maximum acceptable difference between `x*x` and our `target`. If the error is less than `epsilon`, we consider the solution found.
3.  **Step**: We define a `step` value. In each iteration, we increment our `guess` by this amount. A smaller step is more precise but requires more iterations.
4.  **Algorithm**:
    -   Start with `guess = 0.0`.
    -   While the error (`abs(guess**2 - target)`) is greater than or equal to `epsilon`, increment the `guess` by `step`.
    -   Stop when the error is within our acceptable margin.

This approach is more flexible than exhaustive enumeration (`sample_19`) as it can find non-integer roots, but its efficiency is highly dependent on the chosen `step` size.

## Code

The following code implements the solution approximation algorithm to find the square root of a user-provided number.

```python
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
        print(f"Failed to find the square root of {target} within the allowed error.")


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
```

## Explanation

1.  **`main()` function**: This function handles user interaction, ensuring a valid non-negative integer is entered before calling the core algorithm.
2.  **`find_root_by_approximation(target)` function**:
    -   It defines `epsilon` (the desired precision) and `step` (the increment for each guess). The `step` is made very small (`epsilon**2`) to ensure we don't accidentally "jump over" the correct answer.
    -   The `while` loop iterates as long as the solution is not "close enough". The condition `abs(guess**2 - target) >= epsilon` checks if the absolute error is still too large.
    -   The `iterations` counter is included to demonstrate the algorithm's efficiency. Compare the number of iterations here to the one in the exhaustive enumeration example (`sample_19`).
    -   After the loop, a final check confirms if a satisfactory approximation was found.

## Expected Output

```
--- Solution Approximation: Square Root Finder ---
Enter a non-negative integer: 26

Algorithm finished after 50991 iterations.
The approximate square root of 26 is 5.0990

```

## Points to Consider

-   **Precision vs. Performance**: There is a clear trade-off. A smaller `epsilon` (higher precision) requires a smaller `step`, which dramatically increases the number of iterations and slows down the algorithm.
-   **Inefficiency**: This linear "guess and check" approach is still quite inefficient. The next example, Binary Search, will show a much faster way to find a solution.
