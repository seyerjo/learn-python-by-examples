"""Demonstrates exiting nested loops and infinite loops with break."""


def demonstrate_break_in_nested_loop():
    """Shows that break exits only the innermost enclosing loop."""
    print("--- Example 1: `break` in a Nested Loop ---")
    outer_count = 1
    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")
        inner_count = 1
        while inner_count <= 5:
            print(f"  - Inner loop is at: {inner_count}")
            if inner_count == 3:
                print("  - Found 3! Breaking the inner loop.")
                # break exits only the innermost loop.
                break
            inner_count += 1
        print("[Inner loop finished]")
        outer_count += 1
    print("\nNested loop demonstration complete.\n")


def demonstrate_while_true_with_break():
    """Uses the while True / break pattern for an interactive command loop."""
    print("--- Example 2: `while True` with `break` ---")
    print("This loop will continue until you type 'quit'.")
    while True:
        user_input = input("Enter a command: ")
        if user_input.strip().lower() == "quit":
            print("  - 'quit' detected. Breaking the loop.")
            break
        print(f"  You entered: '{user_input}'. The loop continues...")

    print("Loop has been successfully terminated.")


def main():
    """Runs both break-control demonstrations."""
    demonstrate_break_in_nested_loop()
    demonstrate_while_true_with_break()


if __name__ == "__main__":
    main()
