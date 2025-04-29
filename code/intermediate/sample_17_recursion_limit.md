# Recursion Limit in Python

This example demonstrates the recursion limit in Python and how to handle it.

## Code

```python
import sys

# Checking the recursion limit
print("Recursion limit:", sys.getrecursionlimit())

# Defining a recursive function
def recursive_function(n):
    if n == 0:
        return
    else:
        print(n)
        recursive_function(n-1)

# Calling the function
try:
    recursive_function(1000)
except RecursionError as e:
    print("Error:", e)
```

## Explanation

1. Python has a limit on the depth of recursion to prevent a stack overflow.
2. The `sys.getrecursionlimit()` function returns the current recursion limit.
3. The `recursive_function` demonstrates a recursive call that can exceed the recursion limit.
4. A `try-except` block is used to catch the `RecursionError` that occurs when the limit is exceeded.

## Expected Output

When you run this code, it will print the recursion limit and then attempt to call the recursive function. If the recursion limit is exceeded, it will print an error message.

## Points to Consider

- Be aware of the recursion limit when using recursive functions.
- Consider using iterative solutions for large problems to avoid hitting the recursion limit.
