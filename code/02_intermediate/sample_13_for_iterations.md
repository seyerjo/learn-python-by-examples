# `for` Loops and `range()`

Iterate cleanly over lists, strings, and generated integer sequences with Python's `for` loop.

**Source code:** [`sample_13_for_iterations.py`](./sample_13_for_iterations.py) · **Level:** Intermediate

## Core Concept

In Python, `for` loops iterate directly over the items of **any iterable** (`list`, `tuple`, `str`, `dict`, `set`, or `range()`), rather than forcing you to manage manual index counters. That eliminates off-by-one indexing bugs and keeps traversal code concise.

## Guided Walkthrough

1. **Iterating over a list:** `iterate_over_list()` binds each element in `fruits` to `fruit` one by one:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  - Current fruit: {fruit}")
```

2. **Iterating over a string:** Because strings are sequences of characters, `for letter in word:` yields one character per step.

3. **Counting with `range()`:** `range(5)` lazily generates integers from `0` up to `4` without storing a list in memory:

```python
# range(5) yields 0 through 4 (stop is exclusive).
for number in range(5):
    print(f"  - Current number: {number}")
```

## Running the Example

```bash
python3 code/02_intermediate/sample_13_for_iterations.py
```

### Expected Output

```text
--- Example 1: Iterating over a list ---
Iterating through the list: ['apple', 'banana', 'cherry']
  - Current fruit: apple
  - Current fruit: banana
  - Current fruit: cherry

--- Example 2: Iterating over a string ---
Iterating through the characters of the word: 'Python'
  - Current letter: P
  - Current letter: y
  - Current letter: t
  - Current letter: h
  - Current letter: o
  - Current letter: n

--- Example 3: Iterating with range() ---
Looping from 0 to 4 using range(5):
  - Current number: 0
  - Current number: 1
  - Current number: 2
  - Current number: 3
  - Current number: 4
```

## Key Takeaways

- Prefer `for` over `while` whenever you are traversing an existing iterable or a fixed numeric range.
- `range(start, stop, step)` treats `stop` as **exclusive** (`range(5)` stops at `4`).
- Never mutate a list's length (adding/removing elements) while iterating over it directly; iterate over a copy or build a new list instead.
- Next: aggregate totals and track item indexes with `enumerate()` in [`sample_14_more_for_iterations.md`](./sample_14_more_for_iterations.md).
