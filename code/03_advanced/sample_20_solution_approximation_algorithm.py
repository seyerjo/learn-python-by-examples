#!/usr/bin/env python3
"""Demonstrates solution approximation within an error tolerance (epsilon)."""

# Uses PEP 484 type hints; see sample_23_type_hinting.py.

import sys


def find_root_by_approximation(target: int) -> None:
    """Approximates the square root of a target integer within epsilon.

    Args:
        target: Non-negative integer whose square root is approximated.
    """
    epsilon: float = 0.01
    # Keep step smaller than epsilon so the search does not overshoot the root.
    step: float = epsilon**2
    guess: float = 0.0
    iterations: int = 0

    while abs(guess**2 - target) >= epsilon and guess <= target:
        guess += step
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")

    if abs(guess**2 - target) < epsilon:
        print(f"The approximate square root of {target} is {guess:.4f}")
    else:
        print(f"Failed to find the square root of {target} within the allowed error.")


def main() -> int:
    """Prompts for a non-negative integer and runs step approximation.

    Returns:
        Exit status code (0 on completion, 130 if interrupted via Ctrl-C).
    """
    print("--- Solution Approximation: Square Root Finder ---")

    try:
        while True:
            try:
                target_number: int = int(input("Enter a non-negative integer: "))
                if target_number < 0:
                    print(
                        "Error: Please enter a non-negative integer.",
                        file=sys.stderr,
                    )
                    continue
                break
            except ValueError:
                print(
                    "Invalid input. Please enter a valid integer.",
                    file=sys.stderr,
                )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        return 130

    print()
    find_root_by_approximation(target_number)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
