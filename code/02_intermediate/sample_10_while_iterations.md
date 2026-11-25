# `while` Loops and Loop Control

Repeat actions dynamically with `while` loops using counters, sentinel user commands, `continue`, and `break`.

**Source code:** [`sample_10_while_iterations.py`](./sample_10_while_iterations.py) · **Level:** Intermediate

## Core Concept

A `while` loop repeats a block of code as long as its boolean condition evaluates to `True`. Unlike count-based iteration, `while` is ideal when you do not know in advance how many iterations are needed—such as waiting for a user command or scanning until a condition triggers.

## Guided Walkthrough

1. **Counter-controlled loop:** Initialize a counter before the loop, test it in the `while` header, and update it inside the body so the condition eventually becomes `False`:

```python
counter = 0
while counter < 5:
    print(f"  - Inside the loop. Counter is now: {counter}")
    counter += 1
```

2. **Sentinel-controlled interactive loop:** `demonstrate_interactive_loop()` checks `command.strip().lower() != "quit"`, normalizing whitespace and casing so `"Quit"` or `" quit "` exits cleanly.

3. **Skipping and stopping with `continue` and `break`:** Notice that `index += 1` runs *before* `continue` so negative values never stall the loop on the same element:

```python
while index < len(numbers):
    num = numbers[index]
    # Increment early so 'continue' cannot trigger an infinite loop.
    index += 1
    if num < 0:
        continue
    if num == 0:
        break
```

## Running the Example

```bash
python3 code/02_intermediate/sample_10_while_iterations.py
```

### Expected Output

With sample inputs `hello`, `world`, and `quit`:

```text
--- Example 1: Simple Counter Loop ---
Starting the loop. Counter is initially 0.
  - Inside the loop. Counter is now: 0
  - Inside the loop. Counter is now: 1
  - Inside the loop. Counter is now: 2
  - Inside the loop. Counter is now: 3
  - Inside the loop. Counter is now: 4
Loop finished. Final value of counter is 5.

--- Example 2: Interactive Loop ---
Enter a command (or 'quit' to exit): hello
  You entered: hello
Enter a command (or 'quit' to exit): world
  You entered: world
Enter a command (or 'quit' to exit): quit
  You entered: quit
Exited the interactive loop.

--- Example 3: Loop Control with break and continue ---
Processing the list: [1, 5, -2, 8, 0, 3, -7]
  Processing number: 1
  Processing number: 5
  Skipping negative number: -2
  Processing number: 8
  Found a zero. Breaking the loop.
Finished processing the list.
```

## Key Takeaways

- Always ensure at least one path inside a `while` loop moves toward termination to avoid infinite loops.
- `continue` skips only the remainder of the current iteration; `break` exits the enclosing loop immediately.
- When advancing an index manually, update it before any `continue` branch.
- Next: combine loops inside loops in [`sample_11_more_while_iterations.md`](./sample_11_more_while_iterations.md).
