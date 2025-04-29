# Flow Control in Python

This example illustrates how to use if-else statements for flow control in Python.

## Code

```python
# Getting user input
age = int(input("How old are you? "))

# Using if-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
```

## Explanation

1. The `input()` function is used to get user input, which is then converted to an integer using `int()`.
2. An if-else statement is used to make a decision based on the user's age.
3. If the age is 18 or older, it prints "You are an adult." Otherwise, it prints "You are not an adult yet."

## Expected Output

When you run this code, it will ask for your age and then print out whether you are an adult or not based on your input.

## Points to Consider

- Flow control statements like if-else are crucial for making decisions in your code.
- The `int()` function is used to convert the user's input to an integer for comparison.
