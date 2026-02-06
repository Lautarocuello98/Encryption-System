import base64

# =====================
# CONSTANTS
# =====================
CAESAR = "caesar"
VIGENERE = "vigenere"
SUBSTITUTION = "substitution"
BASE64 = "base64"
CUSTOM = "custom"


# =====================
# KEY VALIDATION
# =====================
def validate_caesar_key(key):
    return isinstance(key, int)


def validate_vigenere_key(key):
    return isinstance(key, str) and key.isalpha()


def validate_substitution_key(key):
    return (
        isinstance(key, str)
        and len(key) == 26
        and key.isalpha()
        and len(set(key.lower())) == 26
    )


VALIDATORS = {
    CAESAR: validate_caesar_key,
    VIGENERE: validate_vigenere_key,
    SUBSTITUTION: validate_substitution_key,
}


def validate_key(method, key):
    validator = VALIDATORS.get(method)
    return validator(key) if validator else True


# =====================
# DISPATCHERS
# =====================
def encrypt(method, text, key=None):
    methods = {
        CAESAR: lambda: caesar_encrypt(text, key),
        VIGENERE: lambda: vigenere_encrypt(text, key),
        SUBSTITUTION: lambda: substitution_encrypt(text, key),
        BASE64: lambda: base64_encrypt(text),
        CUSTOM: lambda: custom_encrypt(text),
    }

    if method not in methods:
        raise ValueError("Unknown encryption method")

    return methods[method]()


def decrypt(method, text, key=None):
    methods = {
        CAESAR: lambda: caesar_decrypt(text, key),
        VIGENERE: lambda: vigenere_decrypt(text, key),
        SUBSTITUTION: lambda: substitution_decrypt(text, key),
        BASE64: lambda: base64_decrypt(text),
        CUSTOM: lambda: custom_decrypt(text),
    }

    if method not in methods:
        raise ValueError("Unknown decryption method")

    return methods[method]()


# =====================
# CIPHERS
# =====================
def caesar_encrypt(text: str, shift: int) -> str:
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text: str, key: str) -> str:
    encrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key[key_index % len(key)]) - ord("A")
            encrypted += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            encrypted += char
    return encrypted


def vigenere_decrypt(text: str, key: str) -> str:
    decrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key[key_index % len(key)]) - ord("A")
            decrypted += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            decrypted += char
    return decrypted


def substitution_encrypt(text: str, alphabet: str) -> str:
    alphabet = alphabet.upper()
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""

    for char in text:
        if char.isalpha():
            index = standard.index(char.upper())
            new_char = alphabet[index]
            encrypted += new_char if char.isupper() else new_char.lower()
        else:
            encrypted += char
    return encrypted


def substitution_decrypt(text: str, alphabet: str) -> str:
    alphabet = alphabet.upper()
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.upper())
            new_char = standard[index]
            decrypted += new_char if char.isupper() else new_char.lower()
        else:
            decrypted += char
    return decrypted


def base64_encrypt(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def base64_decrypt(text: str) -> str:
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        raise ValueError("Invalid Base64 input") from e


def custom_encrypt(text: str) -> str:
    hex_output = ""
    for char in text:
        hex_output += f"{ord(char) + 4:02x}"
    return hex_output[::-1]


def custom_decrypt(text: str) -> str:
    reversed_text = text[::-1]
    output = ""

    for i in range(0, len(reversed_text), 2):
        value = int(reversed_text[i:i + 2], 16) - 4
        output += chr(value)

    return output
