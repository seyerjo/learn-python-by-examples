# Code Reusability and the DRY Principle

Avoid duplicating input and formatting logic by extracting a parameterized helper function that returns multiple values as a tuple.

**Source code:** [`sample_08_more_fundamentals.py`](./sample_08_more_fundamentals.py) · **Level:** Basic

## Core Concept

**DRY (Don't Repeat Yourself)** means keeping each piece of logic in a single place instead of copying and pasting code blocks. When two parts of a program perform the same steps with different labels or inputs, extracting a function makes fixes and updates instant.

## Guided Walkthrough

1. **Encapsulating repeated prompts:** `get_user_data(user_title)` collects a user's name and integer age, returning both values packed into a tuple:

```python
def get_user_data(user_title):
    print(f">>> {user_title} USER <<<")
    name = input("Hi, what's your name?: ")
    print(f"Hello {name}")
    age = int(input("And how old are you?: "))
    print("Thank you very much for the information!\n")
    return name, age
```

2. **Tuple unpacking in `main()`:** Calling `get_user_data()` twice unpacks each returned `(name, age)` pair cleanly into distinct variables before comparing ages:

```python
name_first, age_first = get_user_data("FIRST")
name_second, age_second = get_user_data("SECOND")
```

## Running the Example

```bash
python3 code/01_basic/sample_08_more_fundamentals.py
```

### Expected Output

With sample inputs `Alice` (`30`) and `Bob` (`25`):

```text
>>> FIRST USER <<<
Hi, what's your name?: Alice
Hello Alice
And how old are you?: 30
Thank you very much for the information!

>>> SECOND USER <<<
Hi, what's your name?: Bob
Hello Bob
And how old are you?: 25
Thank you very much for the information!

--- Comparison Result ---
Alice, you are older than Bob.
```

## Key Takeaways

- Parameterized functions eliminate copy-paste duplication and keep `main()` focused on high-level orchestration.
- Python lets functions return multiple values effortlessly via `return a, b`, unpacked on the caller side as `x, y = ...`.
- **Note:** Passing non-numeric text for `age` raises `ValueError`; safe validation loops are covered in [`sample_18_exception_handling.md`](../02_intermediate/sample_18_exception_handling.md).
- Next: learn escape characters and raw strings in [`sample_09_escape_character_and_strings.md`](./sample_09_escape_character_and_strings.md).
