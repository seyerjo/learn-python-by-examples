# Practical `for` Loops: Aggregation and `enumerate()`

Compute running totals and averages over a list, and unpack both index and value cleanly using Python's built-in `enumerate()`.

**Source code:** [`sample_14_more_for_iterations.py`](./sample_14_more_for_iterations.py) · **Level:** Intermediate

## Core Concept

Two patterns appear constantly in real Python code: **accumulation** (folding items into a running total) and **indexed traversal** (needing each element's position alongside its value). Using `enumerate()` gives you both index and item directly without manual counter arithmetic.

## Guided Walkthrough

1. **Accumulating a sum and average:** Initialize `total = 0` (explicitly avoiding the name `sum`, which would shadow Python's built-in `sum()` function) and format the average to two decimal places (`:.2f`):

```python
numbers = [10, 20, 30, 40, 50]
# Avoid naming this 'sum' to prevent shadowing the built-in sum().
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
```

2. **Tracking positions with `enumerate()`:** `enumerate(fruits)` yields `(index, fruit)` pairs that unpack directly in the `for` header:

```python
for index, fruit in enumerate(fruits):
    print(f"  - Item at index {index} is: {fruit}")
```

## Running the Example

```bash
python3 code/02_intermediate/sample_14_more_for_iterations.py
```

### Expected Output

```text
--- Example 1: Calculating Sum and Average ---
Calculating sum and average for the list: [10, 20, 30, 40, 50]
  - The sum of the numbers is: 150
  - The average of the numbers is: 30.00

--- Example 2: Using enumerate() to Get Index and Value ---
Iterating through the list with enumerate: ['apple', 'banana', 'cherry']
  - Item at index 0 is: apple
  - Item at index 1 is: banana
  - Item at index 2 is: cherry
```

## Key Takeaways

- Always prefer `for index, item in enumerate(items):` over `for i in range(len(items)):`—it is cleaner and less error-prone.
- Never shadow built-in functions (`sum`, `list`, `len`, `str`) with variable names.
- Guard divisions like `total / len(numbers)` against empty lists (`ZeroDivisionError`) in real applications.
- Next: structure reusable logic into parameterized functions in [`sample_15_functions.md`](./sample_15_functions.md).
