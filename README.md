# 🚀 Learn Python by Examples
> A comprehensive, practical Python learning repository featuring self-contained code examples, synchronized twin documentation, and defensive programming patterns.

![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Version](https://img.shields.io/badge/Version-v1.2.0-blue.svg)
![Stage](https://img.shields.io/badge/Stage-Production-blue.svg)
![Stack](https://img.shields.io/badge/Stack-Python_3.7+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

---

## 🎯 Project Overview
* 👁️ **Vision:** To serve as an essential and practical guide for anyone learning Python, offering clean, structured, and progressively challenging code examples classified by difficulty.
* 📌 **Core Objectives:**
  * 🎯 Deliver a growing collection of 100+ Python code examples covering basic syntax, data structures, control flow, algorithms, and design patterns.
  * 🎯 Categorize all scripts into clearly defined tiers: **Basic** (`code/basic`), **Intermediate** (`code/intermediate`), and **Advanced** (`code/advanced`).
  * 🎯 Provide dedicated, companion markdown documentation for every single script (`sample_XX_description.md`).
  * 🎯 Maintain high engineering standards including PEP 8 style, Google-style docstrings, and PEP 484 type hinting.

---

## ⚡ Main Product Features
* 💎 **Modular Code Examples (FEAT-01):** Standalone, executable Python scripts illustrating specific programming concepts without heavyweight external dependencies (maps to `FR-01`, `FR-02`, `NFR-03`).
* 💎 **Synchronized Twin Documentation (FEAT-02):** Companion markdown guides paired 1:1 with each script, explaining syntax mechanics, line-by-line breakdown, and expected terminal output (maps to `FR-03`, `FR-04`, `NFR-02`).
* 💎 **Tiered Repository Architecture (FEAT-03):** Predictable directory layout and standardized two-digit sequential naming (`sample_00` to `sample_23+`) for zero-friction navigation (maps to `FR-05`, `NFR-01`).
* 💎 **Defensive Error Handling (FEAT-04):** Real-world demonstration of input sanitization, exception interception (`try-except-else-finally`), and graceful error recovery (maps to `NFR-03`).

---

## 🗺️ Application Workflow & Architecture

```mermaid
graph TD
    A[Learner / Developer] --> B(Clone Repository)
    B --> C{Local Workspace}
    C --> D[README.md]
    C --> E[code/basic]
    C --> F[code/intermediate]
    C --> G[code/advanced]
    E --> H[sample_XX_description.py]
    E --> I[sample_XX_description.md]
    F --> J[sample_YY_description.py]
    F --> K[sample_YY_description.md]
    G --> L[sample_ZZ_description.py]
    G --> M[sample_ZZ_description.md]
    D --> A
    I --> A
    K --> A
    M --> A
    H --> N(Run Code via CLI)
    J --> N
    L --> N
    N --> O[Console Output & Telemetry]
    O --> A
```

---

## 📚 Project Documentation
Access the core project documentation inside `/docs`:
* 📘 **[Project Blueprint](./docs/01_project_blueprint.md):** Vision, functional/non-functional requirements (FR/NFR), and product feature specifications.
* 🛠️ **[Engineering Guidelines](./docs/02_engineering_guidelines.md):** Technical architecture, Mermaid topologies, tech stack justifications, environment setup, and PEP 8 / Google-style coding standards.
* 📋 **[Project Log](./docs/03_project_log.md):** Active prioritized task backlog (`To-Do List`) and historical development milestone records.
* 📜 **[Changelog](./CHANGELOG.md):** Chronological version history following the *Keep a Changelog* standard.

---

## 🛠️ Getting Started & Installation

### 📋 Prerequisites
* **Python 3.7+** installed on your system (`python3 --version` or `python --version`).
* **Git** installed on your system (`git --version`).

### ⚙️ Quick Installation & Execution
```bash
# 1. Clone the repository
git clone https://github.com/seyerjo/learn-python-by-examples.git

# 2. Navigate to the project directory
cd learn-python-by-examples

# 3. Choose a difficulty level and navigate into it
cd code/basic

# 4. Execute any sample script
python3 sample_01_hello_world.py
```

---

## 📝 Code Examples Directory

### 📗 Basic Level (`code/basic`)
| Script | Documentation | Description |
| :--- | :--- | :--- |
| [`sample_00_comments_types.py`](./code/basic/sample_00_comments_types.py) | [`sample_00_comments_types.md`](./code/basic/sample_00_comments_types.md) | Single-line, multi-line, and inline comment conventions. |
| [`sample_01_hello_world.py`](./code/basic/sample_01_hello_world.py) | [`sample_01_hello_world.md`](./code/basic/sample_01_hello_world.md) | Standard entry point and `if __name__ == "__main__":` guard. |
| [`sample_02_primitives_data_types.py`](./code/basic/sample_02_primitives_data_types.py) | [`sample_02_primitives_data_types.md`](./code/basic/sample_02_primitives_data_types.md) | Primitive types (`int`, `float`, `str`, `bool`) and `type()`. |
| [`sample_03_strings_operations.py`](./code/basic/sample_03_strings_operations.py) | [`sample_03_strings_operations.md`](./code/basic/sample_03_strings_operations.md) | String concatenation, repetition, indexing, and slicing. |
| [`sample_04_operators.py`](./code/basic/sample_04_operators.py) | [`sample_04_operators.md`](./code/basic/sample_04_operators.md) | Arithmetic, comparison, and logical operators. |
| [`sample_05_inputs.py`](./code/basic/sample_05_inputs.py) | [`sample_05_inputs.md`](./code/basic/sample_05_inputs.md) | Reading console input using `input()` and type casting. |
| [`sample_06_fundamentals.py`](./code/basic/sample_06_fundamentals.py) | [`sample_06_fundamentals.md`](./code/basic/sample_06_fundamentals.md) | Variable naming rules, reserved keywords, and dynamic typing. |
| [`sample_07_flow_control.py`](./code/basic/sample_07_flow_control.py) | [`sample_07_flow_control.md`](./code/basic/sample_07_flow_control.md) | Conditional branching with `if`, `elif`, and `else`. |
| [`sample_08_more_fundamentals.py`](./code/basic/sample_08_more_fundamentals.py) | [`sample_08_more_fundamentals.md`](./code/basic/sample_08_more_fundamentals.md) | Code reusability, function encapsulation, and DRY principle. |
| [`sample_09_escape_character_and_strings.py`](./code/basic/sample_09_escape_character_and_strings.py) | [`sample_09_escape_character_and_strings.md`](./code/basic/sample_09_escape_character_and_strings.md) | Escape sequences (`\n`, `\t`, `\\`) and raw string literals (`r"..."`). |

### 📙 Intermediate Level (`code/intermediate`)
| Script | Documentation | Description |
| :--- | :--- | :--- |
| [`sample_10_while_iterations.py`](./code/intermediate/sample_10_while_iterations.py) | [`sample_10_while_iterations.md`](./code/intermediate/sample_10_while_iterations.md) | While loops, condition checks, and counter increments. |
| [`sample_11_more_while_iterations.py`](./code/intermediate/sample_11_more_while_iterations.py) | [`sample_11_more_while_iterations.md`](./code/intermediate/sample_11_more_while_iterations.md) | Nested `while` loops and multi-variable state tracking. |
| [`sample_12_additional_while_iterations.py`](./code/intermediate/sample_12_additional_while_iterations.py) | [`sample_12_additional_while_iterations.md`](./code/intermediate/sample_12_additional_while_iterations.md) | Loop control flow with `break` and conditional termination. |
| [`sample_13_for_iterations.py`](./code/intermediate/sample_13_for_iterations.py) | [`sample_13_for_iterations.md`](./code/intermediate/sample_13_for_iterations.md) | Sequence traversal with `for` loops and `range()`. |
| [`sample_14_more_for_iterations.py`](./code/intermediate/sample_14_more_for_iterations.py) | [`sample_14_more_for_iterations.md`](./code/intermediate/sample_14_more_for_iterations.md) | Iterating over strings, collections, and step ranges. |
| [`sample_15_functions.py`](./code/intermediate/sample_15_functions.py) | [`sample_15_functions.md`](./code/intermediate/sample_15_functions.md) | Defining modular functions, parameters, and return values. |
| [`sample_16_recursive_functions.py`](./code/intermediate/sample_16_recursive_functions.py) | [`sample_16_recursive_functions.md`](./code/intermediate/sample_16_recursive_functions.md) | Base cases and recursive calls for factorials. |
| [`sample_17_recursion_limit.py`](./code/intermediate/sample_17_recursion_limit.py) | [`sample_17_recursion_limit.md`](./code/intermediate/sample_17_recursion_limit.md) | Stack overflow protection and `sys.getrecursionlimit()`. |
| [`sample_18_exception_handling.py`](./code/intermediate/sample_18_exception_handling.py) | [`sample_18_exception_handling.md`](./code/intermediate/sample_18_exception_handling.md) | Defensive `try-except-else-finally` blocks and `ValueError` interception. |

### 📕 Advanced Level (`code/advanced`)
| Script | Documentation | Description |
| :--- | :--- | :--- |
| [`sample_19_exhaustive_listing_algorithm.py`](./code/advanced/sample_19_exhaustive_listing_algorithm.py) | [`sample_19_exhaustive_listing_algorithm.md`](./code/advanced/sample_19_exhaustive_listing_algorithm.md) | Brute-force exhaustive enumeration (guess-and-check). |
| [`sample_20_solution_approximation_algorithm.py`](./code/advanced/sample_20_solution_approximation_algorithm.py) | [`sample_20_solution_approximation_algorithm.md`](./code/advanced/sample_20_solution_approximation_algorithm.md) | Numerical root approximation using incremental step tolerances. |
| [`sample_21_binary_search_algorithm.py`](./code/advanced/sample_21_binary_search_algorithm.py) | [`sample_21_binary_search_algorithm.md`](./code/advanced/sample_21_binary_search_algorithm.md) | Logarithmic binary search for root finding with iteration counters. |
| [`sample_22_robust_input_validation.py`](./code/advanced/sample_22_robust_input_validation.py) | [`sample_22_robust_input_validation.md`](./code/advanced/sample_22_robust_input_validation.md) | Reusable numeric validation loop with bounds checking. |
| [`sample_23_type_hinting.py`](./code/advanced/sample_23_type_hinting.py) | [`sample_23_type_hinting.md`](./code/advanced/sample_23_type_hinting.md) | PEP 484 type annotations, function signatures, and static type safety. |

---

## 📜 Version History & Changelog
* **Current Version:** `1.2.0` (Tracked via [`CHANGELOG.md`](./CHANGELOG.md)).
* Refer to [`CHANGELOG.md`](./CHANGELOG.md) to inspect recent milestone implementations under `## [Unreleased]` and `## [1.2.0]`.

---

## 🤝 Contributing & Code of Conduct
Contributions are welcome! Please ensure you review our governing documents before submitting Pull Requests:
* 🚀 **[Contribution Guidelines](./CONTRIBUTION_GUIDELINES.md):** Bug reporting, feature suggestions, branching strategy, and PR submission workflow.
* 🤝 **[Code of Conduct](./CODE_OF_CONDUCT.md):** Community standards, inclusive participation pledges, and reporting contacts.

---

## 📄 License
This project is licensed under the terms of the [MIT License](./LICENSE).
