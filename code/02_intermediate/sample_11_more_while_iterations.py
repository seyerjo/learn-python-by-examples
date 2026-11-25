"""Demonstrates nested while loops for producing paired iterations."""


def demonstrate_nested_loops():
    """Prints outer/inner counter pairs using nested while loops."""
    print("--- Nested While Loops Example ---")
    outer_count = 1
    print("Starting the outer loop.")

    while outer_count <= 3:
        print(f"\n[Outer Loop Iteration {outer_count}]")
        # Reset inner counter on every outer iteration.
        inner_count = 1

        while inner_count <= 4:
            print(
                "  - Inner loop iteration: "
                f"(Outer: {outer_count}, Inner: {inner_count})"
            )
            inner_count += 1

        print(f"[Finished Inner Loop for Outer: {outer_count}]")
        outer_count += 1

    print("\nAll loops have completed.")


def main():
    """Runs the nested while loop demonstration."""
    demonstrate_nested_loops()


if __name__ == "__main__":
    main()
