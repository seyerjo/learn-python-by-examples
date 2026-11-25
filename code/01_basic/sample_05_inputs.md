# Reading User Input and Type Conversion

Prompt the user in the terminal with `input()`, display text cleanly with f-strings, and cast numeric input with `int()`.

**Source code:** [`sample_05_inputs.py`](./sample_05_inputs.py) · **Level:** Basic

## Core Concept

Python's built-in `input()` function pauses execution until the user presses Enter and **always returns a `str`**, even if the user types digits. Whenever you need arithmetic on that input, you must explicitly convert it to a numeric type such as `int` or `float`.

## Guided Walkthrough

1. **Reading and formatting strings:** `demonstrate_string_input()` reads `name` and prints it with plain `print()`, `+` concatenation, comma-separated arguments, and f-strings (the cleanest modern option):

```python
name = input("What's your name?: ")
print(f"Your name is {name}")
```

2. **Converting strings to integers:** Passing `age_str` to `int()` turns `"30"` (`str`) into `30` (`int`) so arithmetic works as expected:

```python
age_str = input("Enter your age: ")
print(f"The type of input received is: {type(age_str)}")

age_num = int(age_str)
print(f"After converting to integer, the type is: {type(age_num)}")
print(f"In ten years, you will be {age_num + 10} years old.")
```

3. **Combined input and conversion:** You can nest `int(input(...))` on one line for compact prompts, keeping in mind that invalid text will raise `ValueError`.

## Running the Example

```bash
python3 code/01_basic/sample_05_inputs.py
```

### Expected Output

With sample inputs `Alex`, `30`, and `5`:

```text
--- String Input ---
What's your name?: Alex

--- Different ways to display the string ---
1. Simple print:
Alex

2. Concatenation with '+':
Your name is Alex

3. Multiple arguments in print():
Your name is Alex

4. Using an f-string (modern and recommended):
Your name is Alex

--- Numeric Input ---
Enter your age: 30
The type of input received is: <class 'str'>
After converting to integer, the type is: <class 'int'>
In ten years, you will be 40 years old.

--- Combined input and conversion ---
Enter a number to be multiplied by two: 5
5 * 2 = 10
```

## Key Takeaways

- `input()` always produces a `str`; trying `"30" + 10` raises a `TypeError`.
- **Unhandled `ValueError` risk:** Typing non-numeric text (e.g., `"abc"`) into `int()` crashes this basic script with a `ValueError`.
- Defensive error handling with `try-except` is introduced later in [`sample_18_exception_handling.md`](../02_intermediate/sample_18_exception_handling.md) and generalized in [`sample_22_robust_input_validation.md`](../03_advanced/sample_22_robust_input_validation.md).
- Next: review naming rules and dynamic typing in [`sample_06_fundamentals.md`](./sample_06_fundamentals.md).
