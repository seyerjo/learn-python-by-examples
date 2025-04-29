# More on Inputs, Variables, and Strings in Python

This example further demonstrates the use of user input, variables, and strings in Python.

## Code

```python
# Getting multiple inputs from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Creating a full name string
full_name = first_name + " " + last_name

# Printing the full name
print("Hello, " + full_name + "!")
```

## Explanation

1. The `input()` function is used multiple times to get different pieces of information from the user.
2. The inputs are stored in separate variables (`first_name` and `last_name`).
3. The variables are used to create a `full_name` string by concatenating them with a space in between.

## Expected Output

When you run this code, it will ask for your first name and last name, and then print out a greeting with your full name.

## Points to Consider

- You can get multiple inputs from the user and store them in different variables.
- String concatenation is useful for combining different pieces of text.
