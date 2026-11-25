"""Demonstrates Python's recursion depth limit and catching RecursionError."""

import sys


def countdown(n):
    """Counts down recursively without a base case to hit the recursion limit.

    Args:
        n: Starting integer for the countdown.
    """
    # Intentionally omit a base case to demonstrate hitting the recursion limit.
    print(n)
    countdown(n - 1)


def main():
    """Inspects the active recursion limit and safely catches RecursionError."""
    current_limit = sys.getrecursionlimit()
    print(f"The current recursion limit is: {current_limit}\n")

    call_depth = current_limit + 5
    print(f"Attempting to call a recursive function {call_depth} times...")
    print("This will exceed the limit and raise a RecursionError.")

    try:
        countdown(call_depth)
    except RecursionError as err:
        print(f"\nSuccessfully caught the expected error: {err}")
        print("This safeguard prevents a C stack overflow from crashing Python.")


if __name__ == "__main__":
    main()
