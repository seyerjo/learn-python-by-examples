# Advanced `while` Loop Control with `break`

Understand how `break` scopes to the innermost loop and how the `while True` / `break` pattern models interactive loops cleanly.

**Source code:** [`sample_12_additional_while_iterations.py`](./sample_12_additional_while_iterations.py) · **Level:** Intermediate

## Core Concept

`break` exits only the **innermost** enclosing loop, leaving any outer loop running normally. Combining `break` with `while True` lets you write clear event-driven loops where the exit condition is checked in the middle of the loop body rather than duplicated before and inside the loop.

## Guided Walkthrough

1. **`break` scope in nested loops:** When `inner_count == 3`, `break` stops the inner loop early while `outer_count` still finishes all 3 iterations:

```python
while inner_count <= 5:
    print(f"  - Inner loop is at: {inner_count}")
    if inner_count == 3:
        print("  - Found 3! Breaking the inner loop.")
        # break exits only the innermost loop.
        break
    inner_count += 1
```

2. **The `while True` / `break` pattern:** `demonstrate_while_true_with_break()` reads commands continuously until `user_input.strip().lower() == "quit"`, avoiding an artificial initial dummy value for `user_input`:

```python
while True:
    user_input = input("Enter a command: ")
    if user_input.strip().lower() == "quit":
        print("  - 'quit' detected. Breaking the loop.")
        break
    print(f"  You entered: '{user_input}'. The loop continues...")
```

## Running the Example

```bash
python3 code/02_intermediate/sample_12_additional_while_iterations.py
```

### Expected Output

With sample inputs `hello`, `world`, and `quit`:

```text
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

## Key Takeaways

- `break` terminates only its immediate enclosing loop; outer loops remain unaffected.
- `while True` + `break` is the idiomatic Python pattern for input validation loops (you will pair it with `try-except` in [`sample_22_robust_input_validation.md`](../03_advanced/sample_22_robust_input_validation.md)).
- Always verify every `while True` loop has a reachable `break` or `return` exit path.
- Next: iterate directly over sequences with [`sample_13_for_iterations.md`](./sample_13_for_iterations.md).
