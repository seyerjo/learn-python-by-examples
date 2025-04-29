# Binary Search Algorithm in Python

This example demonstrates the binary search algorithm in Python.

## Code

```python
# Implementing binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(arr, target)
print(f"Target {target} found at index: {index}")
```

## Explanation

1. Binary search is an efficient algorithm for finding an item from a sorted list of items.
2. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

## Expected Output

When you run this code, it will print the index of the target element if found.

## Points to Consider

- Binary search is much faster than linear search for large sorted lists.
- The list must be sorted for binary search to work correctly.
