# Exhaustive Listing Algorithm in Python

This example demonstrates an exhaustive listing algorithm in Python.

## Code

```python
# Implementing an exhaustive listing algorithm
def exhaustive_listing(items):
    for item in items:
        print(item)

# Example usage
items = [1, 2, 3, 4, 5]
exhaustive_listing(items)
```

## Explanation

1. An exhaustive listing algorithm involves listing all possible solutions or elements.
2. The `exhaustive_listing` function takes a list of items and prints each one.

## Expected Output

When you run this code, it will print the elements of the `items` list.

## Points to Consider

- Exhaustive listing can be useful for small datasets but may be impractical for large ones.
- It's a straightforward approach to ensure all elements are considered.
