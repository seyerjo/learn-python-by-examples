#!/usr/bin/env python3
"""Demonstrates exhaustive enumeration (guess and check) for integer square roots."""

# Uses PEP 484 type hints; see sample_23_type_hinting.py.

import sys


def find_square_root(target: int) -> None:
    """Finds the integer square root of a target number via exhaustive enumeration.

    Args:
        target: Non-negative integer whose integer square root is tested.
    """
    guess: int = 0
    iterations: int = 0

    while guess**2 < target:
        guess += 1
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")

    if guess**2 == target:
        print(f"The exact square root of {target} is {guess}.")
    else:
        print(f"{target} does not have an exact integer square root.")


def main() -> int:
    """Prompts for a non-negative integer and runs exhaustive enumeration.

    Returns:
        Exit status code (0 on completion, 130 if interrupted via Ctrl-C).
    """
    print("--- Exhaustive Enumeration: Integer Square Root Finder ---")

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
    find_square_root(target_number)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
