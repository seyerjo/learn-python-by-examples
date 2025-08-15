# Nested `while` Loops in Python

This example demonstrates the use of **nested `while` loops**. A nested loop is a loop that is placed inside another loop.

## Concept

In a nested loop structure, the following happens:

1.  The **outer loop** starts and executes its first iteration.
2.  The **inner loop** is then executed completely (from its beginning to its end).
3.  Once the inner loop finishes, the outer loop proceeds to its next iteration.
4.  This process repeats until the outer loop has completed all its iterations.

This structure is very useful for tasks that involve iterating over two-dimensional data (like a grid or a matrix) or for generating combinations of items from two different sets.

## Code

The following code uses a nested `while` loop to show how the iterations of the outer and inner loops interact.

```python
# MAIN CODE

"""
Demonstrates nested while loops in Python.

A nested loop is a loop inside another loop. The inner loop will be executed
one full time for each iteration of the outer loop. This is useful for working
with two-dimensional data structures or creating combinations of items.
"""


def demonstrate_nested_loops():
    """
    Shows how to use nested while loops to print combinations of numbers.
    """
    print("--- Nested While Loops Example ---")
    # 1. Initialization of the outer loop counter.
    outer_count = 1
    print("Starting the outer loop.")

    # 2. The outer loop will run as long as outer_count is less than or equal to 3.
    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")

        # 3. Initialization of the inner loop counter.
        # This happens *every time* the outer loop runs an iteration.
        inner_count = 1

        # 4. The inner loop will run as long as inner_count is less than or equal to 4.
        while inner_count <= 4:
            # This print statement is inside the inner loop.
            print(f"  - Inner loop iteration: (Outer: {outer_count}, Inner: {inner_count})")
            # 5. Increment the inner loop counter.
            inner_count += 1

        print(f"[Finished Inner Loop for Outer: {outer_count}]")
        # 6. Increment the outer loop counter.
        outer_count += 1

    print("\nAll loops have completed.")


def main():
    """Main function to demonstrate nested while loops."""
    demonstrate_nested_loops()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **`outer_count`**: This variable controls the outer loop. It starts at 1 and the loop continues as long as `outer_count` is less than or equal to 3.
2.  **`inner_count`**: This variable controls the inner loop. It is **reset to 1 at the beginning of each iteration of the outer loop**.
3.  **Execution Flow**: For each single iteration of the outer loop (e.g., when `outer_count` is 1), the inner loop runs completely (from `inner_count` = 1 to 4). This results in a printout of all combinations of the outer and inner counter values.

## Expected Output

When you run this code, the output will clearly show how the inner loop completes its full cycle for each step of the outer loop:

```
--- Nested While Loops Example ---
Starting the outer loop.

[Outer Loop Iteration 1]
  - Inner loop iteration: (Outer: 1, Inner: 1)
  - Inner loop iteration: (Outer: 1, Inner: 2)
  - Inner loop iteration: (Outer: 1, Inner: 3)
  - Inner loop iteration: (Outer: 1, Inner: 4)
[Finished Inner Loop for Outer: 1]

[Outer Loop Iteration 2]
  - Inner loop iteration: (Outer: 2, Inner: 1)
  - Inner loop iteration: (Outer: 2, Inner: 2)
  - Inner loop iteration: (Outer: 2, Inner: 3)
  - Inner loop iteration: (Outer: 2, Inner: 4)
[Finished Inner Loop for Outer: 2]

[Outer Loop Iteration 3]
  - Inner loop iteration: (Outer: 3, Inner: 1)
  - Inner loop iteration: (Outer: 3, Inner: 2)
  - Inner loop iteration: (Outer: 3, Inner: 3)
  - Inner loop iteration: (Outer: 3, Inner: 4)
[Finished Inner Loop for Outer: 3]

All loops have completed.
```

## Points to Consider

-   Be careful with the initialization of the inner loop's counter. It almost always needs to be reset inside the outer loop.
-   Nested loops can be computationally expensive. If the outer loop runs N times and the inner loop runs M times, the code inside the inner loop will be executed N \* M times.
