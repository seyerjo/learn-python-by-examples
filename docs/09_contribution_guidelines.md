# Contribution Guidelines: Learn Python by Examples

Thank you for your interest in contributing to the "Learn Python by Examples" project! Your help is essential to make this an even better resource for learning Python.

This document describes how you can participate in the project, whether by reporting bugs, suggesting improvements, or contributing code and documentation.

## Code of Conduct

To ensure a welcoming and respectful environment for all contributors, we ask you to read and follow our [Code of Conduct](../CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## How to Contribute

There are several ways to contribute to the project:

### 1. Reporting Bugs

If you find a bug in the code of an example, in the documentation, or in the repository structure, please let us know.

-   **Before reporting:** Search the [GitHub Issues](https://github.com/seyerjo/learn-python-by-examples/issues) to see if the bug has already been reported.

-   **How to report:** If you don't find an existing issue for the bug, open a new one in the GitHub repository.

-   **Useful information:** When reporting a bug, include as many details as possible:

    -   A clear and concise description of the problem.

    -   Steps to reproduce the bug.

    -   Expected behavior.

    -   Actual behavior (what actually happens).

    -   The affected file(s).

    -   Your Python version and operating system.

### 2. Suggesting Improvements

If you have ideas for new examples, improvements to existing examples, additions to the documentation, or any other suggestions to enhance the project, we'd love to hear them!

-   **Before suggesting:** Search the [GitHub Issues](https://github.com/seyerjo/learn-python-by-examples/issues) to see if the suggestion has already been discussed.

-   **How to suggest:** Open a new issue in the GitHub repository with the label "Enhancement" or "Suggestion".

-   **Useful information:** Describe your suggestion in detail and explain why you think it would be valuable for the project.

### 3. Contributing Code or Documentation

Direct contributions to the code and documentation are very welcome! Follow these steps to submit your contribution:

-   **Step 1: Fork the Repository:** If you haven't already, "fork" the `learn-python-by-examples` repository to your GitHub account.

-   **Step 2: Clone Your Fork:** Clone your fork to your local machine.

    ```bash
    git clone [https://github.com/seyerjo/learn-python-by-examples.git](https://github.com/seyerjo/learn-python-by-examples.git)
    cd learn-python-by-examples
    ```

-   **Step 3: Create a New Branch:** Create a new branch for your contribution. Use a descriptive name for the branch (e.g., `feat/new-list-example` or `fix/dictionary-example-error`).

    ```bash
    git checkout -b your-branch-name
    ```

-   **Step 4: Make Your Changes:** Implement your changes, whether adding a new example, improving an existing one, fixing a bug, or updating documentation.

    -   Make sure to follow the project's [Code Style Guide](./10_code_style_guide.md).

    -   If adding a new example, make sure to include its `.py` file and corresponding `.md` documentation, following the `sample_0x_description` naming pattern.

    -   Test your changes locally to ensure they work as expected.

-   **Step 5: Commit Your Changes:** Commit your changes with clear and descriptive messages.

    ```bash
    git add .
    git commit -m "feat: Add new example on lists"
    ```

-   **Step 6: Push Your Changes to Your Fork:** Push your new branch to your fork repository on GitHub.

    ```bash
    git push origin your-branch-name
    ```

-   **Step 7: Open a Pull Request (PR):** Go to your fork repository on GitHub and open a Pull Request from your new branch to the `main` branch of the original `learn-python-by-examples` repository.

-   **Step 8: PR Description:** Provide a clear and detailed description of your Pull Request. Explain what changes you have made, why they are necessary, and any other relevant information. Reference related issues if any.

-   **Step 9: PR Review:** The project team will review your Pull Request. They may ask questions, suggest changes, or request clarifications. Please respond to comments and make requested adjustments if necessary.

-   **Step 10: PR Merge:** Once your Pull Request is approved, it will be merged into the main branch of the project. Congratulations and thank you for your contribution!

## Code Style Guide

It is important that all code and documentation follow the defined standards to maintain project consistency. Please consult the [Code Style Guide](./10_code_style_guide.md) document before submitting your code contributions.

## Questions

If you have any questions about how to contribute, feel free to open an issue on GitHub with the label "Question".

We look forward to your contributions!
