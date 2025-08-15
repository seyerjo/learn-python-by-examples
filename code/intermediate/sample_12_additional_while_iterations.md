# Advanced `while` Loop Control with `break`

This example demonstrates more advanced ways to control `while` loops using the `break` statement. The `break` statement immediately terminates the innermost loop it is in, allowing for more flexible control over loop execution.

We will explore two key patterns:

1.  Using `break` to exit an inner loop in a nested loop structure.
2.  Using the `while True` and `break` pattern for event-driven loops.

## Code

The following code contains two distinct examples demonstrating these concepts.

```python
# MAIN CODE

"""
Demonstrates advanced control of while loops using the `break` statement.

This example covers two common use cases for `break`:
1.  Exiting an inner loop prematurely in a nested loop structure.
2.  Creating an "infinite" loop with `while True` that is controlled by an
    internal condition.
"""


def demonstrate_break_in_nested_loop():
    """
    Shows how `break` affects only the innermost loop it is in.
    """
    print("--- Example 1: `break` in a Nested Loop ---")
    outer_count = 1
    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")
        inner_count = 1
        # This inner loop is intended to run 5 times.
        while inner_count <= 5:
            print(f"  - Inner loop is at: {inner_count}")
            # The `break` statement will exit the *inner loop* only.
            if inner_count == 3:
                print("  - Found 3! Breaking the inner loop.")
                break
            inner_count += 1
        print("[Inner loop finished]")
        outer_count += 1
    print("\nNested loop demonstration complete.\n")


def demonstrate_while_true_with_break():
    """
    Demonstrates the common pattern of using `while True` with a `break`
    for loops that don't have a simple counter-based condition.
    """
    print("--- Example 2: `while True` with `break` ---")
    print("This loop will continue until you type 'quit'.")
    while True:  # This creates a seemingly infinite loop.
        user_input = input("Enter a command: ")
        if user_input.lower() == "quit":
            print("  - 'quit' detected. Breaking the loop.")
            break  # This is the crucial exit condition.
        print(f"  You entered: '{user_input}'. The loop continues...")

    print("Loop has been successfully terminated.")


def main():
    """Main function to demonstrate `break` in while loops."""
    demonstrate_break_in_nested_loop()
    demonstrate_while_true_with_break()


if __name__ == "__main__":
    main()
```

## Explanation

### Example 1: `break` in a Nested Loop

-   **Concept**: When `break` is used inside a nested loop, it only terminates the **innermost loop** where it is located. The outer loop is unaffected and continues its normal execution.
-   **In the code**: The inner loop is designed to count from 1 to 5. However, the `if inner_count == 3:` condition causes a `break`, so the inner loop never counts past 3. The outer loop, however, continues to run its full 3 iterations.

### Example 2: The `while True / break` Pattern

-   **Concept**: This is a very common and powerful pattern in Python. You create a loop that runs indefinitely (`while True`) and then use one or more `if` conditions inside the loop to determine the point at which to `break` out of it. This is ideal for situations where the exit condition is complex or depends on events happening inside the loop (like user input).
-   **In the code**: The loop continues to ask for user input. The only way to stop it is by typing "quit", which triggers the `break` statement.

## Expected Output

```
--- Example 1: `break` in a Nested Loop ---

[Outer Loop Iteration 1]
  - Inner loop is at: 1
  - Inner loop is at: 2
  - Inner loop is at: 3
  - Found 3! Breaking the inner loop.
[Inner loop finished]

[Outer Loop Iteration 2]
  - Inner loop is at: 1
  - Inner loop is at: 2
  - Inner loop is at: 3
  - Found 3! Breaking the inner loop.
[Inner loop finished]

[Outer Loop Iteration 3]
  - Inner loop is at: 1
  - Inner loop is at: 2
  - Inner loop is at: 3
  - Found 3! Breaking the inner loop.
[Inner loop finished]

Nested loop demonstration complete.

--- Example 2: `while True` with `break` ---
This loop will continue until you type 'quit'.
Enter a command: hello
  You entered: 'hello'. The loop continues...
Enter a command: world
  You entered: 'world'. The loop continues...
Enter a command: quit
  - 'quit' detected. Breaking the loop.
Loop has been successfully terminated.
```

## Points to Consider

-   The `break` statement provides a clean way to exit a loop based on a specific condition, making your code more readable than using complex flag variables.
-   Always ensure that a `while True` loop has a reliable `break` condition to avoid creating an actual infinite loop that freezes your program.
