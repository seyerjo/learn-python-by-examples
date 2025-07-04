# Hello World in Python

This example demonstrates how to print "Hello, World!" to the console in Python and introduces the standard structure for a runnable script.

## Code

```python
# MAIN CODE

"""Example of printing 'Hello, World!' to the console."""


def main():
    """Prints 'Hello, World!' to the console."""
    print("Hello, World!")  # Using double quotes
    print('Hello, World!')  # Using single quotes


# The `if __name__ == "__main__":` block is a standard best practice in Python.
# It ensures that the `main()` function is called only when the script is
# executed directly (not when it is imported as a module into another script).
# This makes your code more reusable and organized.
if __name__ == "__main__":
    main()
```

## Explanation

1.  **`print()` function**: This is the basic function used to output text to the console.
2.  **`main()` function**: It's a convention to place the main logic of your script inside a function, typically named `main`. This helps organize the code.
3.  **`if __name__ == "__main__":`**: This is a crucial construct in Python.
    - `__name__` is a special variable that Python automatically sets.
    - When you run your script directly, Python sets `__name__` to the string `"__main__"`.
    - If your script is imported by another script, `__name__` is set to the script's filename.
    - Therefore, this `if` statement checks "Am I being run directly?". If `True`, it calls the `main()` function. This prevents the `main()` function from running automatically when the file is just imported.

## Expected Output

When you run this code, you should see the following output:

```
Hello, World!
Hello, World!
```

## Points to Consider

- Using a `main` function and the `if __name__ == "__main__":` guard is a standard best practice that makes your code more modular, reusable, and easier to read, even for simple scripts.
