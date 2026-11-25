"""Demonstrates while loops using counters, user input, break, and continue."""


def demonstrate_counter_loop():
    """Demonstrates a basic counter-controlled while loop."""
    print("--- Example 1: Simple Counter Loop ---")
    counter = 0
    print(f"Starting the loop. Counter is initially {counter}.")

    while counter < 5:
        print(f"  - Inside the loop. Counter is now: {counter}")
        counter += 1

    print(f"Loop finished. Final value of counter is {counter}.\n")


def demonstrate_interactive_loop():
    """Demonstrates a while loop controlled by user input."""
    print("--- Example 2: Interactive Loop ---")
    command = ""
    while command.strip().lower() != "quit":
        command = input("Enter a command (or 'quit' to exit): ")
        print(f"  You entered: {command}")

    print("Exited the interactive loop.\n")


def demonstrate_loop_control():
    """Demonstrates skipping and terminating iterations with continue and break."""
    print("--- Example 3: Loop Control with break and continue ---")
    numbers = [1, 5, -2, 8, 0, 3, -7]
    index = 0
    print(f"Processing the list: {numbers}")

    while index < len(numbers):
        num = numbers[index]
        # Increment early so 'continue' cannot trigger an infinite loop.
        index += 1

        if num < 0:
            print(f"  Skipping negative number: {num}")
            continue

        if num == 0:
            print("  Found a zero. Breaking the loop.")
            break

        print(f"  Processing number: {num}")

    print("Finished processing the list.\n")


def main():
    """Runs all while loop demonstrations."""
    demonstrate_counter_loop()
    demonstrate_interactive_loop()
    demonstrate_loop_control()


if __name__ == "__main__":
    main()
