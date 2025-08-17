# MAIN CODE

"""
Demonstrates Python's recursion limit and how to handle the RecursionError.

Python sets a limit on the depth of recursion to prevent infinite recursions
from causing an overflow of the C stack and crashing Python. This example
shows how to check this limit and what happens when it's exceeded.
"""

# Import the sys module to access system-specific parameters and functions.
import sys


def countdown(n):
    """
    A simple recursive function that counts down from n.
    This function is designed to demonstrate hitting the recursion limit.
    """
    # This print helps visualize the recursion, but it will stop when the
    # error occurs, so you won't see it count all the way down.
    print(n)
    # The recursive step: call itself with a decremented value.
    countdown(n - 1)


def main():
    """
    Main function to check the recursion limit and then intentionally cause
    a RecursionError.
    """
    # 1. Check and display the current recursion limit.
    # This is typically 1000 by default.
    current_limit = sys.getrecursionlimit()
    print(f"The current recursion limit is: {current_limit}\n")

    # 2. We will attempt to call a recursive function with a number slightly
    #    higher than the limit to trigger the error.
    call_depth = current_limit + 5

    print(f"Attempting to call a recursive function {call_depth} times...")
    print("This will exceed the limit and raise a RecursionError.")

    try:
        # 3. We use a try...except block to safely handle the expected error
        #    without crashing the program.
        countdown(call_depth)
    except RecursionError as e:
        # 4. When the recursion limit is hit, this block will execute.
        print(f"\nSuccessfully caught the expected error: {e}")
        print("This error prevents a stack overflow, which could crash the interpreter.")


if __name__ == "__main__":
    main()
