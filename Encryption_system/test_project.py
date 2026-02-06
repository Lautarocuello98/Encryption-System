import pytest


from encryption import (
    caesar_encrypt,
    caesar_decrypt,
    vigenere_encrypt,
    vigenere_decrypt,
    substitution_encrypt,
    substitution_decrypt,
    base64_encrypt,
    base64_decrypt,
    custom_encrypt,
    custom_decrypt,
)


def test_caesar_encrypt_decrypt():
    text = "HelloWorld"
    key = 3
    encrypted = caesar_encrypt(text, key)
    decrypted = caesar_decrypt(encrypted, key)

    assert encrypted != text
    assert decrypted == text


def test_vigenere_encrypt_decrypt():
    text = "HELLOWORLD"
    key = "KEY"
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)

    assert encrypted != text
    assert decrypted == text


def test_substitution_encrypt_decrypt():
    text = "HELLO"
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted = substitution_encrypt(text, alphabet)
    decrypted = substitution_decrypt(encrypted, alphabet)

    assert encrypted != text
    assert decrypted == text


def test_base64_encrypt_decrypt():
    text = "Hello123"
    encrypted = base64_encrypt(text)
    decrypted = base64_decrypt(encrypted)

    assert encrypted != text
    assert decrypted == text


def test_custom_encrypt_decrypt():
    text = "hola123"
    encrypted = custom_encrypt(text)
    decrypted = custom_decrypt(encrypted)

    assert encrypted != text
    assert decrypted == text