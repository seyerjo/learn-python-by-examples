# Escape Characters and Raw Strings

Include newlines, tabs, literal backslashes, and mixed quotes in Python strings—and learn when raw strings (`r"..."`) are cleaner.

**Source code:** [`sample_09_escape_character_and_strings.py`](./sample_09_escape_character_and_strings.py) · **Level:** Basic

## Core Concept

Inside standard string literals, the backslash (`\`) starts an **escape sequence** that represents special whitespace (`\n`, `\t`) or escapes delimiters (`\"`, `\'`, `\\`). When a string needs many literal backslashes—such as Windows paths or regular expressions—prefixing it with `r"..."` creates a **raw string** that disables escape processing.

## Guided Walkthrough

1. **Whitespace and literal backslashes:** `\n` breaks to a new line, `\t` inserts a horizontal tab, and `\\` prints a single backslash:

```python
print("This string will be split across...\n...two separate lines.")
print("You can create columns:\nCol1\tCol2\tCol3")
print("Useful for Windows paths: C:\\Users\\Name")
```

2. **Raw strings (`r"..."`):** Prefixing a literal with `r` keeps every backslash intact without doubling them:

```python
windows_path = r"C:\Users\Name\Documents"
print(f"Raw string path: {windows_path}")
```

3. **Quotes inside strings:** Either escape the inner quote (`\"`) or wrap the string in the opposite quote style (`'...'` around double quotes). Notice `# fmt: skip` preserves the escaped `\"` lesson when formatting with `Ruff`.

## Running the Example

```bash
python3 code/01_basic/sample_09_escape_character_and_strings.py
```

### Expected Output

With sample inputs `John` and `Doe`:

```text
--- Newline Character (\n) ---
This string will be split across...
...two separate lines.

--- Tab Character (\t) ---
You can create columns:
Col1	Col2	Col3
A	B	C

--- Backslash Character (\\) ---
This is a single backslash: \
Useful for Windows paths: C:\Users\Name

--- Raw Strings (r"...") ---
Raw string path: C:\Users\Name\Documents

--- Escaping Quotes (\' and \") ---
She said, "It's a beautiful day!"
He replied, "Indeed it is."

--- Interactive Example ---
What's your first name?: John
What's your last name?: Doe

Your name is:
	"John Doe"
```

## Key Takeaways

- Use `r"..."` (raw strings) for regex patterns and Windows-style paths—noting one edge case: a raw string cannot end with an odd number of trailing backslashes (e.g., `r"C:\"` is invalid).
- Also use raw docstrings (`r"""..."""`) whenever a docstring mentions `\n` or `\t` to avoid Python `SyntaxWarning` on invalid escape sequences.
- Alternating outer quotes (`'He said, "Hi."'`) is usually cleaner than escaping with `\"`.
- Next: advance to loops in [`sample_10_while_iterations.md`](../02_intermediate/sample_10_while_iterations.md).
