# More While Loops in Python

This example further demonstrates the use of while loops in Python.

## Code

```python
# Using a while loop with a conditional break
i = 0
while True:
    if i >= 5:
        break
    print(i)
    i += 1
```

## Explanation

1. A while loop with a condition that is always true (`while True`) can be used to create an infinite loop.
2. The `break` statement is used to exit the loop when a certain condition is met.
3. In this case, the loop breaks when `i` is greater than or equal to 5.

## Expected Output

When you run this code, it will print the numbers 0 through 4.

## Points to Consider

- The `break` statement allows you to exit a loop prematurely.
- Infinite loops can be useful in certain situations, but be cautious to avoid unintended infinite loops.
