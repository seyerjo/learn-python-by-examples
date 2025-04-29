# String Operations in Python

This example demonstrates various operations that can be performed on strings in Python.

## Code

```python
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# Repetition
str3 = "Hello"
result = str3 * 3
print("Repetition:", result)

# Indexing
str4 = "Python"
print("First character:", str4[0])
print("Last character:", str4[-1])

# Slicing
str5 = "Programming"
print("Slice (1:4):", str5[1:4])
```

## Explanation

1. **Concatenation**: Joining two or more strings together using the `+` operator.
2. **Repetition**: Repeating a string multiple times using the `*` operator.
3. **Indexing**: Accessing individual characters in a string using their index.
4. **Slicing**: Extracting a subset of characters from a string using a range of indices.

## Expected Output

When you run this code, you should see the following output:

```
Concatenation: Hello World
Repetition: HelloHelloHello
First character: P
Last character: n
Slice (1:4): rog
```

## Points to Consider

- Strings are versatile and can be manipulated in various ways.
- Understanding string operations is essential for text processing and manipulation.
