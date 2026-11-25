# Nested `while` Loops

Combine an outer and inner `while` loop to process two-dimensional structures or generate paired combinations.

**Source code:** [`sample_11_more_while_iterations.py`](./sample_11_more_while_iterations.py) · **Level:** Intermediate

## Core Concept

A **nested loop** places one loop inside the body of another. For every single step of the outer loop, the inner loop runs through its full cycle from start to finish before the outer loop advances.

## Guided Walkthrough

1. **Outer loop setup and inner counter reset:** The critical rule of nested loops is initializing `inner_count = 1` *inside* the outer `while` block so the inner loop restarts cleanly on every outer pass:

```python
outer_count = 1
while outer_count <= 3:
    print(f"\n[Outer Loop Iteration {outer_count}]")
    # Reset inner counter on every outer iteration.
    inner_count = 1

    while inner_count <= 4:
        print(f"  - Inner loop iteration: (Outer: {outer_count}, Inner: {inner_count})")
        inner_count += 1
    outer_count += 1
```

2. **Total iterations:** With 3 outer iterations and 4 inner iterations per pass, the inner print statement executes $3 \times 4 = 12$ times.

## Running the Example

```bash
python3 code/02_intermediate/sample_11_more_while_iterations.py
```

### Expected Output

```text
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

## Key Takeaways

- Always reset the inner loop state inside the outer loop; forgetting to reset `inner_count = 1` causes the inner loop to run only on the first outer pass.
- Watch computational growth: nesting an $N$-step loop inside an $M$-step loop yields $M \times N$ inner executions.
- Next: see how `break` behaves inside nested loops and `while True` in [`sample_12_additional_while_iterations.md`](./sample_12_additional_while_iterations.md).
