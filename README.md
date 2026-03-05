# 🔐 Encryption System

> A Python encryption toolkit demonstrating classical ciphers, clean architecture, and test-driven development.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-green.svg)](#-running-tests)

---

## ✨ Overview

This project is a **Python encryption toolkit** that implements several classical encryption algorithms while demonstrating good software engineering practices.

The system separates encryption logic from the command-line interface, includes automated tests with **pytest**, and is designed to be easily extended with additional cipher methods.

This repository focuses on demonstrating:

- Modular Python architecture
- Algorithm implementation
- CLI application design
- Unit testing with pytest
- Clean and maintainable code structure

---

## 🚀 Features

| Feature | Description |
|-------|-------------|
| Multiple Cipher Methods | Caesar, Vigenère, Substitution, Base64, and a custom cipher |
| CLI Interface | Interactive command-line tool for encryption and decryption |
| Input Validation | Key validation specific to each cipher |
| Unit Tests | Automated testing with pytest |
| Modular Architecture | Encryption logic separated from the user interface |
| Extensible Design | New ciphers can be added with minimal changes |

---

## 🔐 Supported Encryption Methods

### Caesar Cipher

A classical substitution cipher that shifts each letter by a fixed number of positions.

**Key Format:** Integer (1–25)

Example:

    Input:  HELLO
    Key:    3
    Output: KHOOR

---

### Vigenère Cipher

A polyalphabetic substitution cipher that uses a keyword to determine shifting values.

**Key Format:** Alphabetic string (example: SECRET)

Example:

    Input:  HELLO
    Key:    KEY
    Output: RIJVS

---

### Substitution Cipher

A cipher that replaces each letter with a custom alphabet mapping.

**Key Format:** 26 unique letters representing a full alphabet permutation.

Example:

    Plain alphabet:  abcdefghijklmnopqrstuvwxyz
    Cipher alphabet: qwertyuiopasdfghjklzxcvbnm

---

### Base64 Encoding

Encodes text using the Base64 encoding scheme.

Commonly used for safe transmission of binary data as text.

Example:

    Input:  HELLO
    Output: SEVMTE8=

---

### Custom Cipher

A custom encryption method combining several transformations.

Process:

1. ASCII shift (±4)
2. Convert characters to hexadecimal
3. Reverse the resulting string

This demonstrates how multiple transformations can be chained to form a custom cipher pipeline.

---

## 📦 Installation

### Requirements

- Python 3.8 or higher
- pip

### Setup

    git clone https://github.com/Lautarocuello98/Encryption-System.git
    cd Encryption-System
    pip install -r requirements.txt

---

## 🎯 Quick Start

Run the CLI application:

    python cli.py

Example interaction:

    Select encryption method:

    1. Caesar Cipher
    2. Vigenère Cipher
    3. Substitution Cipher
    4. Base64 Encoding
    5. Custom Cipher

    Enter choice (1-5): 1
    Enter text: Hello World
    Enter shift value (1-25): 3
    Encrypt (e) or Decrypt (d)? e

    Result: Khoor Zruog

---

## 💻 Using the Project as a Python Library

Example:

    from encryption import Encryption

    enc = Encryption()

    # Caesar Cipher
    encrypted = enc.encrypt("hello", "caesar", "3")
    print(encrypted)

    # Vigenère Cipher
    encrypted = enc.encrypt("hello", "vigenere", "secret")
    print(encrypted)

    # Base64
    encrypted = enc.encrypt("hello", "base64", None)
    print(encrypted)

---

## 📁 Project Structure

    Encryption-System/
    │
    ├── encryption.py
    ├── cli.py
    ├── test_project.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    └── __init__.py

- encryption.py → Core encryption logic and cipher implementations  
- cli.py → Command-line interface  
- test_project.py → Automated tests using pytest  

---

## 🧪 Running Tests

Install dependencies:

    pip install -r requirements.txt

Run tests:

    pytest

Verbose output:

    pytest -v

Run a specific test:

    pytest test_project.py::test_caesar_cipher -v

---

## 🏗 Architecture & Design

The project follows several clean code principles.

### Separation of Concerns

Encryption logic is completely independent from the CLI interface.

### Testability

Core logic functions can be tested without user interaction.

### Extensibility

Adding a new cipher requires minimal changes.

Example:

    def rot13(self, text):
        return self.caesar(text, 13)

---

## 💡 Use Cases

- Educational projects for understanding classical cryptography
- Demonstrating Python architecture and testing practices
- Integration as a module in larger Python applications
- Portfolio project showing algorithm implementation

---

## 📊 Code Quality

This project includes:

- Clean modular architecture
- Automated tests with pytest
- Clear function structure
- Error handling and input validation
- Readable and maintainable code

---

## 🔒 Security Note

⚠️ **Educational Purpose**

This project implements **classical encryption algorithms** and is intended for learning and experimentation.

It should **not be used to protect sensitive data**.

For real-world security applications, use industry-standard libraries such as:

- cryptography
- TLS / SSL protocols
- AES / RSA encryption standards

---

## 🚀 Possible Future Improvements

- GUI interface with tkinter
- File encryption support
- Additional classical ciphers (Playfair, Transposition, etc.)
- Web API interface
- Batch encryption processing

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

## 👨‍💻 Author

**Lautaro Cuello**

GitHub: https://github.com/Lautarocuello98  
LinkedIn: lautaro-cuello-7ba4063a3  

Python developer focused on automation, scripting, and practical tools.

---

⭐ If you found this project useful, consider giving it a star.
