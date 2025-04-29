# Recursive Functions in Python

This example demonstrates how to use recursive functions in Python.

## Code

```python
# Defining a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calling the function
print(factorial(5))
```

## Explanation

1. A recursive function is a function that calls itself.
2. The `factorial` function calculates the factorial of a number `n` by calling itself with `n-1` until it reaches the base case (`n == 0`).
3. The base case returns 1, and the recursive calls return the product of `n` and the factorial of `n-1`.

## Expected Output

When you run this code, it will print the factorial of 5.

## Points to Consider

- Recursive functions can be an elegant way to solve problems that have a recursive structure.
- Be cautious to avoid infinite recursion by ensuring a proper base case.
