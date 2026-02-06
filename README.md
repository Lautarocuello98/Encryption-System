# Encryption System 🔐

A Python-based **encryption and decryption system** implementing multiple classical and custom ciphers.  
The project is designed with a **clear separation between logic and CLI**, making it easy to test, extend, and maintain.

---

## 🚀 Features

- Encrypt and decrypt text using multiple methods
- Input validation for cipher-specific keys
- Clean command-line interface (CLI)
- Fully tested with `pytest`
- Modular and extensible design

---

## 🔐 Supported Encryption Methods

### 1. Caesar Cipher
- Shifts alphabetic characters by a fixed number.
- **Key:** Integer (shift value)

### 2. Vigenère Cipher
- Uses a keyword to encrypt text with repeated shifts.
- **Key:** Alphabetic string

### 3. Substitution Cipher
- Replaces letters using a custom alphabet.
- **Key:** 26 unique letters

### 4. Base64 Encoding
- Encodes and decodes text using Base64.
- **Key:** None

### 5. Custom Cipher
- Adds 4 to each character’s ASCII value
- Converts to hexadecimal
- Reverses the final string
- **Key:** None

---

## 📁 Project Structure

```text
encryption_system/
│
├─ encryption.py      # Core encryption logic
├─ cli.py             # Command-line interface
├─ test_project.py    # Unit tests
├─ README.md
├─ requirements.txt
└─ __init__.py
```

---

## 🧪 Running Tests

Install dependencies:

bash:
pip install -r requirements.txt

Run tests:

pytest

## ▶️ Running the Program

python cli.py

## Design Notes

- Core logic is fully decoupled from user input and output
- Errors are handled via exceptions in the logic layer
- The CLI is responsible only for user interaction
- New encryption methods can be added with minimal changes

## Author

Lautaro Cuello  
GitHub: https://github.com/Lautarocuello98
Linkedin: https://www.linkedin.com/in/lautaro-cuello-7ba4063a3
