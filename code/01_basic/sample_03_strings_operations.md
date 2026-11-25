# String Operations: Joining, Indexing, Slicing, and F-Strings

Manipulate text in Python using `+` concatenation, `*` repetition, `len()`, indexing, slicing, and modern f-strings.

**Source code:** [`sample_03_strings_operations.py`](./sample_03_strings_operations.py) · **Level:** Basic

## Core Concept

In Python, a string (`str`) is an **immutable sequence** of characters. Because it is a sequence, you can measure its length with `len()` and read individual characters or substrings by position—without ever modifying the original string in place.

*(Note: The script groups each topic into separate helper functions such as `demonstrate_slicing()` to stay clean; functions are covered in depth later in [`sample_15_functions.md`](../02_intermediate/sample_15_functions.md).)*

## Guided Walkthrough

1. **Concatenation and repetition:** Use `+` to join strings and `*` to repeat them. Passing `sep=""` to `print()` prevents spaces between comma-separated arguments:

```python
concatenated = first_string + second_string
print("'", first_string, "' + '", second_string, "' = '", concatenated, "'", sep="")
cheer = ((hip_string + " ") * 2) + hurra_string
```

2. **Length and indexing:** `len()` counts every character (including spaces and newlines inside `"""..."""`). Indexes start at `0` from the left and `-1` from the right:

```python
print("Length of the large string is:", len(large_string))
print("First character of 'World':", world_string[0])
print("Last character of 'World':", world_string[-1])
```

3. **Slicing (`[start:stop:step]`):** Extracts a substring where `start` is inclusive and `stop` is exclusive; `step` controls the stride:

```python
print("Slice [2:]:", world_string[2:])  # 'rld'
print("Slice [:3]:", world_string[:3])  # 'Wor' (indices 0, 1, 2)
print("Slice [:-1]:", world_string[:-1])  # 'Worl'
print("Slice [::2]:", world_string[::2])  # 'Wrd'
```

4. **F-strings (`f"..."`):** Embed variables directly inside `{...}` for clean, readable formatting:

```python
sentence = f"I am a citizen of the {world_string}"
```

## Running the Example

```bash
python3 code/01_basic/sample_03_strings_operations.py
```

### Expected Output

```text
--- Concatenation and Repetition ---
'123' + '456' = '123456'
'123' * 3 = '123123123'
Cheer example: Hip Hip Hurra

--- Length and Indexing ---
Length of the large string is: 89
First character of 'World': W
Third character of 'World': r
Last character of 'World': d

--- String Slicing ---
Slice [2:]: rld
Slice [:3]: Wor
Slice [:-1]: Worl
Slice [::2]: Wrd

--- F-String Formatting (Modern Method) ---
f-string sentence: I am a citizen of the World
f-string repeated: I am a citizen of the World, I am a citizen of the World, 
```

## Key Takeaways

- Strings are **immutable**: every operation returns a brand-new string.
- Remember that `stop` in `text[start:stop]` is **exclusive** (`"World"[:3]` gives `"Wor"`, not `"Worl"`).
- Prefer f-strings (`f"..."`) over manual `+` concatenation when mixing text and variables.
- Next: explore Python operators in [`sample_04_operators.md`](./sample_04_operators.md).
