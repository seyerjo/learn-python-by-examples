# Project Blueprint: Learn Python by Examples

## Vision & Objectives

### Central Vision
To be an essential and practical guide for anyone interested in learning Python, providing clear, robust, and well-structured code examples classified by difficulty level.

### Main Objectives
- **Comprehensive Collection:** Provide a collection of at least 100 Python code examples covering basic, intermediate, and advanced programming concepts.
- **Clear Classification:** Organize and categorize all code examples into well-defined difficulty levels (`basic`, `intermediate`, `advanced`).
- **Granular Documentation:** Provide dedicated, high-quality documentation for every individual code example.
- **Intuitive Architecture:** Maintain a clean, easy-to-navigate repository structure optimized for self-guided learning.
- **Educational Onboarding:** Deliver a clear and comprehensive root guide (`README.md`) explaining the project layout, navigation paths, and local execution instructions.

### Problem / Need Addressed
Beginning programmers and practitioners learning Python often struggle to find practical, standalone, and progressively challenging code examples that demonstrate best practices, error handling, and idiomatic patterns with contextual explanations.

### General Description of the Solution
A curated, modular repository of standalone and packaged Python code examples organized by difficulty tiers, accompanied by twin markdown documentation for each script, demonstrating standard library capabilities, modern syntax, and defensive programming patterns.

---

## Requirements

### Functional Requirements (FR)
- **FR-01:** The project must contain a collection of standalone and modular code examples written in modern Python (3.7+).
- **FR-02:** Code examples must be organized and classified into dedicated difficulty tiers: `basic`, `intermediate`, and `advanced`.
- **FR-03:** Each code example (`sample_XX_description.py`) must be accompanied by its corresponding twin documentation file (`sample_XX_description.md`).
- **FR-04:** Each documentation file must explain the code's pedagogical purpose, concepts illustrated, step-by-step workflow, and expected console output.
- **FR-05:** Users must be able to view and execute the source code of any example directly in a local Python environment.
- **FR-06:** Users must be able to access and read the documentation associated with each example alongside the code.
- **FR-07:** The repository architecture must support the addition of new examples and difficulty categories in an extensible manner.
- **FR-08:** The project must support continuous maintenance, refactoring, and quality improvements for existing examples and documentation.

### Non-Functional Requirements (NFR)
- **NFR-01 (Usability & Navigation):** The repository directory layout must be intuitive, predictable, and simple to browse across all operating systems.
- **NFR-02 (Pedagogical Clarity):** Documentation and in-code comments must be clear, concise, beginner-friendly, and written in English.
- **NFR-03 (Code Correctness & Robustness):** All provided code samples must be fully functional, free of syntax errors, and demonstrate proper error handling where applicable.
- **NFR-04 (Public Availability):** The project must remain hosted in a public GitHub repository with open access.
- **NFR-05 (Community Guidelines):** The project must provide clear contribution and conduct guidelines to encourage community collaboration.
- **NFR-06 (Zero-Friction Setup):** Local environment setup and script execution must require minimal steps and rely primarily on standard Python tooling.
- **NFR-07 (Consistent Difficulty Gradient):** The progression from `basic` through `intermediate` to `advanced` must follow a coherent, pedagogical complexity curve.

---

## Product Features

### FEAT-01: Modular Collection of Python Code Examples
- **Description:** A progressive library of Python code samples covering syntax fundamentals, data structures, algorithms, standard library utilities, and idiomatic patterns.
- **Associated Requirements:** FR-01, FR-02, FR-05, FR-07, NFR-03, NFR-07
- **Detailed Operation:** Users browse through categorized level folders (`/code/01_basic`, `/code/02_intermediate`, `/code/03_advanced`), choose an example, and execute it locally via CLI.
- **Edge Cases & Handling:**
  - *Invalid or Unexpected Inputs:* Examples requiring user input validate data types and gracefully intercept malformed entries.
  - *Null / Empty Values:* String and collection examples explicitly demonstrate operations on empty inputs.
  - *Boundary & Extreme Values:* Arithmetic and algorithmic samples account for zero, negative numbers, and boundary conditions.
  - *Missing External Resources:* File I/O and network examples handle missing files or connection timeouts with defensive try/except structures.
- **Validation Rules:**
  - Every script must be standalone and executable without unhandled runtime exceptions.
  - Scripts must include proper shebang (`#!/usr/bin/env python3`) and `if __name__ == "__main__":` entry guards.

### FEAT-02: Synchronized Twin Documentation
- **Description:** Comprehensive markdown documentation paired 1:1 with each script (`sample_XX_description.md`) residing in the same directory.
- **Associated Requirements:** FR-03, FR-04, FR-06, FR-08, NFR-02
- **Detailed Operation:** Readers open the markdown twin to inspect the conceptual breakdown, code explanations, and expected output before or after running the Python script.
- **Edge Cases & Validation:**
  - *Documentation Drift:* Documentation must be updated synchronously whenever code logic or parameters change.
  - *Output Discrepancies:* Sample output blocks in documentation must match exact console execution output.

### FEAT-03: Structured & Predictable Repository Architecture
- **Description:** Standardized directory hierarchy and naming convention (`sample_00_description.py` / `sample_00_description.md`) enforcing consistency across all levels.
- **Associated Requirements:** FR-02, FR-05, NFR-01
- **Detailed Operation:** Tiered folder structure isolating `01_basic/`, `02_intermediate/`, and `03_advanced/` samples, with `/docs` holding the core project documentation and `/` holding repository metadata.
- **Edge Cases & Validation:**
  - All file and directory names must strictly use lowercase letters with underscore separators.
  - Numbering must maintain sequential two-digit zero-padding (`sample_01_...`, `sample_02_...`).

### FEAT-04: Robust Error Handling & Defensive Patterns
- **Description:** Practical demonstrations of error prevention, graceful degradation, and exception handling across examples.
- **Associated Requirements:** FR-01, NFR-03
- **Detailed Operation:** Demonstrates `try-except-else-finally` blocks for common runtime exceptions (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`), showing clean error messages instead of leaking raw tracebacks to the console.
- **Validation Rules:**
  - Specific exception types must be caught (avoid bare `except:`).
  - Diagnostic error feedback must be routed cleanly to `sys.stderr` when appropriate.
