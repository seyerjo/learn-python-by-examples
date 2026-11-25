# Modern Type Hinting (PEP 484 / 585 / 604)

Annotate variables, parameters, and return types using modern Python `3.11+` syntax, and verify them statically with `mypy --strict`.

**Source code:** [`sample_23_type_hinting.py`](./sample_23_type_hinting.py) · **Level:** Advanced

## Core Concept

Python remains dynamically typed at runtime—the interpreter does not block mismatched types during execution. **Type hints** serve as machine-checkable contracts for static analyzers (`mypy`, `pyright`) and IDE language servers (`Pylance`), catching type bugs *before* code runs without adding runtime overhead.

## Guided Walkthrough

1. **Scalar annotations:** `PI: float = 3.14159` and `add_numbers(a: int, b: int) -> int` declare expected scalar types directly in code; per Google docstring conventions, those types are not repeated in `Args:`/`Returns:`:

```python
PI: float = 3.14159


def add_numbers(a: int, b: int) -> int:
    return a + b
```

2. **Built-in generic collections (PEP 585) and unions (PEP 604):** In modern Python (`3.11+`), parameterize `list[str]` and `dict[str, int]` directly without importing legacy `typing.List` or `typing.Dict` (and use `int | float` for unions as seen in [`sample_22_robust_input_validation.py`](./sample_22_robust_input_validation.py)):

```python
def count_words(phrases: list[str]) -> dict[str, int]:
    word_count: dict[str, int] = {}
    for phrase in phrases:
        for word in phrase.split():
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
```

3. **Catching bugs statically:** If `main()` called `add_numbers("hello", "world")`, Python would concatenate `"helloworld"` at runtime instead of failing loudly—whereas a static checker flags both arguments immediately before execution:

```text
error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"
error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"
```

## Running the Example

```bash
python3 code/03_advanced/sample_23_type_hinting.py
```

To verify static type safety across the advanced directory:

```bash
uvx mypy --strict code/03_advanced
```

### Expected Output

```text
--- Demonstrating Basic Type Hinting ---
The result of add_numbers(10, 5) is: 15
The value of PI (hinted as float) is: 3.14159

--- Demonstrating Complex Type Hinting ---
Counting words in: ['hello world', 'hello python']
Resulting dictionary: {'hello': 2, 'world': 1, 'python': 1}
```

## Key Takeaways

- Type hints are **not** enforced at runtime; pair them with `mypy --strict` or `pyright`/`Pylance` to catch mismatches early.
- Use modern native generics (`list[...]`, `dict[...]`) and pipe unions (`int | None`) instead of legacy `typing.List`, `Dict`, `Optional`, and `Union`.
- When signatures carry PEP 484 type annotations, omit redundant types from Google-style `Args:`/`Returns:` docstrings so docs never drift from signatures.
- This completes the 24-sample baseline (`sample_00`–`sample_23`); upcoming expansions (`sample_24`+) build directly on these patterns.
