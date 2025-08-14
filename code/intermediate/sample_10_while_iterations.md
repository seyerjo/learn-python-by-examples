# While Loops in Python

This example demonstrates the `while` loop in Python, showing several common use cases with increasing complexity. A `while` loop repeatedly executes a block of code as long as a specified condition remains `True`.

## Code

```python
# MAIN CODE

"""
Demonstrates various uses of the while loop in Python, from a simple
counter to more advanced control with user input, break, and continue.
"""


def demonstrate_counter_loop():
    """Demonstrates a basic while loop as a counter."""
    print("--- Example 1: Simple Counter Loop ---")
    # 1. Initialization: Start with a counter variable.
    counter = 0
    print(f"Starting the loop. Counter is initially {counter}.")

    # 2. Condition: The loop will continue as long as this is True.
    while counter < 5:
        print(f"  - Inside the loop. Counter is now: {counter}")
        # 3. Update: Increment the counter. Without this, it would be an infinite loop!
        counter += 1

    print(f"Loop finished. Final value of counter is {counter}.\n")


def demonstrate_interactive_loop():
    """Demonstrates a while loop controlled by user input."""
    print("--- Example 2: Interactive Loop ---")
    command = ""
    # The loop continues as long as the user's command is not 'quit'.
    while command.lower() != "quit":
        command = input("Enter a command (or 'quit' to exit): ")
        print(f"  You entered: {command}")

    print("Exited the interactive loop.\n")


def demonstrate_loop_control():
    """Demonstrates using 'break' and 'continue' inside a while loop."""
    print("--- Example 3: Loop Control with break and continue ---")
    numbers = [1, 5, -2, 8, 0, 3, -7]
    index = 0
    print(f"Processing the list: {numbers}")

    while index < len(numbers):
        num = numbers[index]
        index += 1  # Increment index early to avoid infinite loop on 'continue'

        if num < 0:
            print(f"  Skipping negative number: {num}")
            continue  # Skip the rest of this iteration and go to the next

        if num == 0:
            print("  Found a zero. Breaking the loop.")
            break  # Exit the loop entirely

        print(f"  Processing number: {num}")

    print("Finished processing the list.\n")


def main():
    """Main function to demonstrate all while loop examples."""
    demonstrate_counter_loop()
    demonstrate_interactive_loop()
    demonstrate_loop_control()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Simple Counter Loop**: This is the most basic form. The loop runs as long as the `counter` variable is less than 5. The counter is initialized before the loop and incremented inside the loop.

2.  **Interactive Loop**: This common pattern shows how a `while` loop can run indefinitely until a specific user input (like 'quit') is received. The condition checks the value of the `command` variable on each iteration.

3.  **Loop Control (`break` and `continue`)**:
    -   `continue`: When the code encounters a negative number, the `continue` statement immediately stops the _current iteration_ and jumps to the next evaluation of the `while` condition.
    -   `break`: When the code encounters a zero, the `break` statement immediately terminates the _entire loop_, and execution continues on the line after the loop.

## Expected Output

The output is interactive. An example session would look like this:

```
--- Example 1: Simple Counter Loop ---
Starting the loop. Counter is initially 0.
  - Inside the loop. Counter is now: 0
  - Inside the loop. Counter is now: 1
  - Inside the loop. Counter is now: 2
  - Inside the loop. Counter is now: 3
  - Inside the loop. Counter is now: 4
Loop finished. Final value of counter is 5.

--- Example 2: Interactive Loop ---
Enter a command (or 'quit' to exit): hello
  You entered: hello
Enter a command (or 'quit' to exit): world
  You entered: world
Enter a command (or 'quit' to exit): quit
  You entered: quit
Exited the interactive loop.

--- Example 3: Loop Control with break and continue ---
Processing the list: [1, 5, -2, 8, 0, 3, -7]
  Processing number: 1
  Processing number: 5
  Skipping negative number: -2
  Processing number: 8
  Found a zero. Breaking the loop.
Finished processing the list.

```

## Points to Consider

-   A `while` loop is ideal when you don't know in advance how many times you need to loop—it all depends on the condition.
-   Always ensure the condition will eventually become `False`. Forgetting to update the variable in the condition (like `counter += 1`) is a common cause of **infinite loops**.
-   `break` and `continue` give you precise control over your loop's execution beyond just the main `while` condition.
