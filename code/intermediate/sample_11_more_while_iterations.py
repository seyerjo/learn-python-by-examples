# MAIN CODE

"""
Demonstrates nested while loops in Python.

A nested loop is a loop inside another loop. The inner loop will be executed
one full time for each iteration of the outer loop. This is useful for working
with two-dimensional data structures or creating combinations of items.
"""


def demonstrate_nested_loops():
    """
    Shows how to use nested while loops to print combinations of numbers.
    """
    print("--- Nested While Loops Example ---")
    # 1. Initialization of the outer loop counter.
    outer_count = 1
    print("Starting the outer loop.")

    # 2. The outer loop will run as long as outer_count is less than or equal to 3.
    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")

        # 3. Initialization of the inner loop counter.
        # This happens *every time* the outer loop runs an iteration.
        inner_count = 1

        # 4. The inner loop will run as long as inner_count is less than or equal to 4.
        while inner_count <= 4:
            # This print statement is inside the inner loop.
            print(
                f"  - Inner loop iteration: (Outer: {outer_count}, Inner: {inner_count})")
            # 5. Increment the inner loop counter.
            inner_count += 1

        print(f"[Finished Inner Loop for Outer: {outer_count}]")
        # 6. Increment the outer loop counter.
        outer_count += 1

    print("\nAll loops have completed.")


def main():
    """Main function to demonstrate nested while loops."""
    demonstrate_nested_loops()


if __name__ == "__main__":
    main()
