# Python Operators Overview

Understand Python's six foundational operator families: arithmetic, comparison, logical, assignment, membership, and identity.

**Source code:** [`sample_04_operators.py`](./sample_04_operators.py) · **Level:** Basic

## Core Concept

Operators are symbols and keywords that compute values, compare data, test membership, and combine boolean conditions. Knowing the exact difference between value equality (`==`) and object identity (`is`) prevents subtle bugs when working with mutable objects.

*(Note: Each operator family lives in its own helper function for clarity; defining functions is covered in [`sample_15_functions.md`](../02_intermediate/sample_15_functions.md).)*

## Guided Walkthrough

1. **Arithmetic operators** distinguish true division (`/`, always returns a `float`) from floor division (`//`), modulo remainder (`%`), and exponentiation (`**`):

```python
a, b = 10, 3
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} (Integer Division) = {a // b}")
print(f"{a} % {b} (Modulo) = {a % b}")
print(f"{a} ** {b} (Exponent) = {a**b}")
```

2. **Comparison and logical operators** evaluate conditions to `True` or `False` (`==`, `!=`, `<`, `>`, `<=`, `>=`, combined via `and`, `or`, `not`).

3. **Compound assignment and membership:** Operators like `+=`, `-=`, and `*=` update a variable concisely (`x += 5`), while `in` and `not in` check whether an element exists inside a sequence.

4. **Identity (`is`) vs. equality (`==`):** Two distinct lists can contain equal values (`==` is `True`) while occupying different locations in memory (`is` is `False`):

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a is b -> {a is b}")
print(f"a is c -> {a is c}")
print(f"a == b -> {a == b}")
```

## Running the Example

```bash
python3 code/01_basic/sample_04_operators.py
```

### Expected Output

```text
--- Arithmetic Operators ---
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 // 3 (Integer Division) = 3
10 % 3 (Modulo) = 1
10 ** 3 (Exponent) = 1000

--- Comparison Operators ---
5 == 10 -> False
5 != 10 -> True
5 < 10 -> True
5 > 10 -> False
5 <= 10 -> True
5 >= 10 -> False

--- Logical Operators ---
True and False -> False
True or False -> True
not True -> False

--- Assignment Operators ---
Initial x = 10
x += 5 -> x = 15
x -= 3 -> x = 12
x *= 2 -> x = 24

--- Membership Operators ---
List = [1, 2, 3, 4, 5]
3 in [1, 2, 3, 4, 5] -> True
6 in [1, 2, 3, 4, 5] -> False
3 not in [1, 2, 3, 4, 5] -> False

--- Identity Operators ---
a = [1, 2, 3], b = [1, 2, 3], c = a
a is b -> False
a is c -> True
a == b -> True
```

## Key Takeaways

- Use `==` when comparing values (numbers, strings, lists) and reserve `is` for singletons like `None` (`if value is None:`).
- Remember `/` always produces a `float` (`10 / 2 == 5.0`), whereas `//` performs floor division.
- Next: learn how programs read keyboard data in [`sample_05_inputs.md`](./sample_05_inputs.md).
