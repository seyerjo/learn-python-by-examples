# Solution Approximation Algorithm

This example illustrates finding an approximate solution for a problem, specifically calculating the square root of a number.

## Code

```python
""" SOLUTION APPROXIMATION algorithm

    An approximation algorithm finds a solution that is "close enough" to the
    exact answer. This is useful when an exact solution is too slow or
    impossible to compute. It works by iteratively refining a guess until it
    is within a certain margin of error (epsilon).

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`).                 #
# ############################################################################ #


def main() -> None:
    """Main function demonstrating solution approximation algorithm."""
    epsilon = 0.01  # Controls accuracy of approximation
    step = epsilon**2

    # Get a valid integer from the user
    while True:
        try:
            target = int(input("Enter an integer number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print()

    # Initialize guess and perform approximation
    guess = 0.0
    while abs(guess**2 - target) >= epsilon and guess <= target:
        guess += step

    # Check if approximation was successful
    if abs(guess**2 - target) < epsilon:
        print(f"Approximate square root of {target} is {guess:.4f}")
    else:
        print(f"Could not find square root of {target} within given precision")


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Parameters**: The algorithm defines an `epsilon` (the acceptable margin of error) and a `step` (how much to increment the guess in each iteration). A smaller step leads to higher precision but takes more time.
2.  **Input Validation**: A `while` loop with `try-except` ensures the user provides a valid integer.
3.  **Approximation Loop**: The `while` loop continues as long as the absolute difference between `guess**2` and the `target` is greater than or equal to `epsilon`. It also ensures the guess does not significantly overshoot the target.
4.  **Result**: After the loop, it checks one last time if the final `guess` is within the `epsilon` margin. If so, it's considered a successful approximation.

## Expected Output

```
Enter an integer number: 26

Approximate square root of 26 is 5.0990
```

## Points to Consider

- **Trade-off**: There is a direct trade-off between precision (`epsilon`) and performance. A very small `epsilon` will be more accurate but much slower.
- **Convergence**: This simple linear approach may fail to find a solution for very large numbers if the `step` is too small, as the loop might take too long.
