# MAIN CODE

"""
Demonstrates advanced control of while loops using the `break` statement.

This example covers two common use cases for `break`:
1.  Exiting an inner loop prematurely in a nested loop structure.
2.  Creating an "infinite" loop with `while True` that is controlled by an
    internal condition.
"""


def demonstrate_break_in_nested_loop():
    """
    Shows how `break` affects only the innermost loop it is in.
    """
    print("--- Example 1: `break` in a Nested Loop ---")
    outer_count = 1
    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")
        inner_count = 1
        # This inner loop is intended to run 5 times.
        while inner_count <= 5:
            print(f"  - Inner loop is at: {inner_count}")
            # The `break` statement will exit the *inner loop* only.
            if inner_count == 3:
                print("  - Found 3! Breaking the inner loop.")
                break
            inner_count += 1
        print("[Inner loop finished]")
        outer_count += 1
    print("\nNested loop demonstration complete.\n")


def demonstrate_while_true_with_break():
    """
    Demonstrates the common pattern of using `while True` with a `break`
    for loops that don't have a simple counter-based condition.
    """
    print("--- Example 2: `while True` with `break` ---")
    print("This loop will continue until you type 'quit'.")
    while True:  # This creates a seemingly infinite loop.
        user_input = input("Enter a command: ")
        if user_input.lower() == "quit":
            print("  - 'quit' detected. Breaking the loop.")
            break  # This is the crucial exit condition.
        print(f"  You entered: '{user_input}'. The loop continues...")

    print("Loop has been successfully terminated.")


def main():
    """Main function to demonstrate `break` in while loops."""
    demonstrate_break_in_nested_loop()
    demonstrate_while_true_with_break()


if __name__ == "__main__":
    main()
