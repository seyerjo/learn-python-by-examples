# Built-in Data Types and `type()`

Inspect Python's core scalar types and built-in collection types at runtime using the `type()` function.

**Source code:** [`sample_02_primitives_data_types.py`](./sample_02_primitives_data_types.py) · **Level:** Basic

## Core Concept

Python is **dynamically typed**: variables do not require explicit type declarations because every value carries its own type at runtime. Calling `type(value)` reveals the exact class of any object—covering both scalar values (`int`, `float`, `complex`, `str`, `bool`, `NoneType`) and core container types (`list`, `tuple`, `dict`, `set`).

## Guided Walkthrough

1. **Scalar and special types** hold single values:

```python
integer_variable = 1  # int: whole numbers
float_variable = 3.14  # float: decimal numbers
complex_variable = 1 + 2j  # complex: real + imaginary parts
string_variable = "Hello, Coder!"  # str: immutable text
boolean_variable = False  # bool: True or False
none_variable = None  # NoneType: explicit absence of a value
```

2. **Built-in collection types** group multiple values with different ordering and mutability guarantees:

```python
list_variable = [1, 2, 3]  # Ordered, mutable sequence
tuple_variable = (4.0, 5.5, 6.9)  # Ordered, immutable sequence
dictionary_variable = {
    "key": "value"
}  # Key-value map (preserves insertion order since Python 3.7+)
set_variable = {7, 8, 9}  # Unordered collection of unique items
```

3. **Runtime inspection:** Passing each variable to `print(type(...))` outputs its underlying class name.

## Running the Example

```bash
python3 code/01_basic/sample_02_primitives_data_types.py
```

### Expected Output

```text
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'set'>
<class 'bool'>
<class 'NoneType'>
```

## Key Takeaways

- Every variable name points to a typed object, so `type()` is a quick diagnostic tool during debugging.
- **Mutability matters:** `list`, `dict`, and `set` can be modified in place after creation, whereas `int`, `float`, `complex`, `str`, `tuple`, `bool`, and `NoneType` are immutable.
- Unlike `set`, Python dictionaries (`dict`) preserve key insertion order as part of the language specification since Python 3.7+.
- Next: work with text values in detail in [`sample_03_strings_operations.md`](./sample_03_strings_operations.md).
