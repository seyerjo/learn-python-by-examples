# More For Loop Examples in Python

This example provides additional illustrations of using for loops in Python.

## Code

```python
# Using a for loop with the range() function
for i in range(5):
    print(i)

# Using a for loop with the enumerate() function
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Explanation

1. The `range()` function generates a sequence of numbers that can be used in a for loop.
2. The `enumerate()` function returns both the index and the value of each element in a sequence.

## Expected Output

When you run this code, it will print the numbers 0 through 4, followed by the elements of the `fruits` list with their indices.

## Points to Consider

- The `range()` function is useful for creating loops that run a specific number of times.
- The `enumerate()` function is useful when you need both the index and the value of each element in a sequence.
