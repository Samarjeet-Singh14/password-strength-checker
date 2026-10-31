# Password Strength Checker & Batch Generator

A lightweight, zero-dependency Python utility designed to evaluate credential robustness and generate cryptographically secure, randomized passwords.

## Features
- **Heuristic Strength Scoring:** Rates passwords from *Very Weak* to *Very Strong* based on length thresholds and character complexity.
- **Pattern Detection:** Automatically flags high-frequency breached and predictable credentials (e.g., `admin`, `123456`, `qwerty`).
- **Targeted Feedback:** Provides specific recommendations for missing character sets (uppercase, lowercase, numbers, or special symbols).
- **CSPRNG Security:** Uses Python's `secrets` module for cryptographically strong, non-deterministic random generation.
- **Batch Processing:** Allows users to set a custom length (8–64) and generate up to 25 passwords at once.

## Prerequisites
- Python 3.10 or higher installed.
- No third-party packages required (built entirely using Python standard library).

## How to Run
1. Clone or download this repository.
2. Open your terminal in the project folder and run:
   ```bash
   python password_tool.py
