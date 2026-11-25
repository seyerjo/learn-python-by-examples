#!/usr/bin/env python3
"""Demonstrates modern PEP 484 / 585 / 604 type hinting in Python."""

PI: float = 3.14159


def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns their sum.

    Args:
        a: First integer operand.
        b: Second integer operand.

    Returns:
        Sum of `a` and `b`.
    """
    return a + b


def count_words(phrases: list[str]) -> dict[str, int]:
    """Tokenizes text phrases and counts occurrences of each word.

    Args:
        phrases: Sequence of text phrases to inspect.

    Returns:
        Dictionary mapping each whitespace-delimited word to its frequency.
    """
    word_count: dict[str, int] = {}
    for phrase in phrases:
        for word in phrase.split():
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def main() -> int:
    """Demonstrates scalar and collection type annotations at runtime.

    Returns:
        Exit status code (0 on completion).
    """
    print("--- Demonstrating Basic Type Hinting ---")
    result: int = add_numbers(10, 5)
    print(f"The result of add_numbers(10, 5) is: {result}")
    print(f"The value of PI (hinted as float) is: {PI}\n")

    print("--- Demonstrating Complex Type Hinting ---")
    sentences: list[str] = ["hello world", "hello python"]
    counts: dict[str, int] = count_words(sentences)
    print(f"Counting words in: {sentences}")
    print(f"Resulting dictionary: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
