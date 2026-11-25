# Python's Recursion Limit and `RecursionError`

Inspect Python's maximum call-stack depth with `sys.getrecursionlimit()` and handle runaway recursion safely via `RecursionError`.

**Source code:** [`sample_17_recursion_limit.py`](./sample_17_recursion_limit.py) · **Level:** Intermediate

## Core Concept

Every active function call pushes a frame onto Python's call stack. Without a safeguard, an infinite or overly deep recursion would exhaust process memory and crash the interpreter. Python therefore enforces a recursion depth limit (typically `1000`) and raises `RecursionError` cleanly if it is exceeded.

## Guided Walkthrough

1. **Intentional unbounded recursion:** `countdown(n)` omits a base case on purpose so each step prints `n` and recurses with `n - 1` until the stack limit triggers:

```python
def countdown(n):
    # Intentionally omit a base case to demonstrate hitting the recursion limit.
    print(n)
    countdown(n - 1)
```

2. **Inspecting the limit and catching `RecursionError`:** `main()` queries `sys.getrecursionlimit()`, invokes `countdown(current_limit + 5)` inside `try`, and catches `RecursionError` cleanly:

```python
current_limit = sys.getrecursionlimit()
call_depth = current_limit + 5
try:
    countdown(call_depth)
except RecursionError as err:
    print(f"\nSuccessfully caught the expected error: {err}")
```

Notice that because `<module>` and `main()` already occupy stack frames before `countdown()` starts, the countdown stops a few frames above `0` (at `8` under Python 3.12's default limit of `1000`).

## Running the Example

```bash
python3 code/02_intermediate/sample_17_recursion_limit.py
```

### Expected Output

Truncated view of a real run (with default limit `1000`):

```text
The current recursion limit is: 1000

Attempting to call a recursive function 1005 times...
This will exceed the limit and raise a RecursionError.
1005
1004
1003
1002
...
12
11
10
9
8

Successfully caught the expected error: maximum recursion depth exceeded
This safeguard prevents a C stack overflow from crashing Python.
```

## Key Takeaways

- `RecursionError` is a protective boundary, not a Python bug—it prevents memory exhaustion and C-stack crashes.
- Avoid raising `sys.setrecursionlimit()` as a quick fix; deep linear loops are usually cleaner and safer when rewritten iteratively (`while` or `for`).
- Next: master full structured exception handling in [`sample_18_exception_handling.md`](./sample_18_exception_handling.md).
