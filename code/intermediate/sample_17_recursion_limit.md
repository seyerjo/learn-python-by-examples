# Python's Recursion Limit and `RecursionError`

To protect against a stack overflow, Python sets a limit on how many times a function can call itself recursively. This example demonstrates what this limit is, why it exists, and how to handle the `RecursionError` that occurs when you exceed it.

## Concept

Every time a function is called, a "frame" is added to the call stack. This frame stores the function's local variables and its execution state. If a recursive function calls itself too many times without reaching a base case, the call stack can grow infinitely, consuming all available memory and crashing the Python interpreter.

To prevent this, Python imposes a recursion depth limit. When this limit is reached, Python stops the execution and raises a `RecursionError`.

This example will:

1.  Check and display the current recursion limit using the `sys` module.
2.  Intentionally cause a `RecursionError` by calling a recursive function more times than the limit allows.
3.  Use a `try...except` block to catch the error gracefully without crashing the program.

## Code

```python
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
```

## Explanation

1.  **`sys.getrecursionlimit()`**: This function from the `sys` module returns the current maximum depth of the Python interpreter’s recursion stack. The default value is usually 1000, but it can vary.
2.  **`countdown(n)`**: This is a simple recursive function with no base case. It will keep calling itself until the recursion limit is hit.
3.  **`try...except RecursionError`**: This is the standard way to handle this specific error. The code inside the `try` block is executed, and if a `RecursionError` occurs, the program immediately jumps to the `except` block instead of crashing. This allows you to handle the error gracefully.

## Expected Output

The exact numbers in the output may vary slightly, but the structure will be as follows. The countdown will start but will be interrupted long before it reaches zero.

```
The current recursion limit is: 1000

Attempting to call a recursive function 1005 times...
This will exceed the limit and raise a RecursionError.
1005
1004
1003
...
(many numbers will be printed here)
...
3
2
1

Successfully caught the expected error: maximum recursion depth exceeded
This error prevents a stack overflow, which could crash the interpreter.
```

## Points to Consider

-   While you can change the recursion limit with `sys.setrecursionlimit()`, it is often a sign of a design flaw in your code. It's generally better to rewrite a deeply recursive algorithm iteratively.
-   Hitting the recursion limit is a safeguard, not a bug in Python itself. It protects your system's resources.
