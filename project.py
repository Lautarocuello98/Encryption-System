import base64



#inicio

def main():


    while True:
        print()
        print("=== Encryption System ===")
        print("1) Encript")
        print("2) Decrypt")
        print("3) Exit")



        choice = input("Choose an option: ").strip()


        if choice == "3":
            print("Exiting...")
            break

        if choice not in ["1", "2"]:
            print()
            print("Invalid option.")
            print("Try again.")
            continue



        method = select_method()

        if method is None:
            print()
            print("Invalid method.")
            print("Try again.")
            continue



        text = input("Enter the text: ")

        key = get_key(method)

        if not validate_key(method, key):
            print()
            print("Invalid key for this method.")
            print("Try again.")
            continue


        print()
        print("--------------------------------")

        print("\nResult:\n")

        # Perform action
        if choice == "1":
            print(encrypt(method, text, key))
        else:
            print(decrypt(method, text, key))
        print("--------------------------------")

        print()
        print("Thank you for using the Encryption System!")
        print("Do you want to perform another operation?")
        print()
        print("1) Yes, continue")
        print("2) exit")
        again = input("Choose an option: ").strip()
        print()
        if again == "2":
            print("Exiting...")
            break


#seleccion de metod
def select_method():
    print("\nAvailable methods:")
    print("1) Caesar")
    print("2) Vigenere")
    print("3) Substitution")
    print("4) Base64")
    print("5) Custom")

    option = input("Choose method (1–5): ").strip()

    methods = {
        "1": "caesar",
        "2": "vigenere",
        "3": "substitution",
        "4": "base64",
        "5": "custom"
    }


    return methods.get(option, None)





#validacion de clave

def get_key(method):

    if method == "caesar":
        try:
            return int(input("Numeric key (shift): "))
        except ValueError:
            return None

    elif method == "vigenere":
        return input("Keyword (letters only): ").strip()

    elif method == "substitution":
        return input("Substitution alphabet (26 letters): ").strip()


    return None


# MAIN FUNCTIONS
def encrypt(method, text, key):
    if method == "caesar":
        return caesar_encrypt(text, key)
    elif method == "vigenere":
        return vigenere_encrypt(text, key)
    elif method == "substitution":
        return substitution_encrypt(text, key)
    elif method == "base64":
        return base64_encrypt(text)
    elif method == "custom":
        return custom_encrypt(text)


def decrypt(method, text, key):
    if method == "caesar":
        return caesar_decrypt(text, key)
    elif method == "vigenere":
        return vigenere_decrypt(text, key)
    elif method == "substitution":
        return substitution_decrypt(text, key)
    elif method == "base64":
        return base64_decrypt(text)
    elif method == "custom":
        return custom_decrypt(text)

def validate_key(method, key):
    if method == "caesar":
        return isinstance(key, int)

    if method == "vigenere":
        return isinstance(key, str) and key.isalpha()

    if method == "substitution":
        return isinstance(key, str) and len(key) == 26 and key.isalpha()

    return True



# METHODS

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)





def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(text, key):
    decrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            decrypted += char
    return decrypted







def substitution_encrypt(text, alphabet):
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

def substitution_decrypt(text, alphabet):
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






def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return "Invalid Base64 input"






def custom_encrypt(text):
    hex_output = ""

    for char in text:
        value = ord(char) + 4
        hex_value = hex(value)[2:]
        if len(hex_value) == 1:
            hex_value = "0" + hex_value
        hex_output += hex_value

    return hex_output[::-1]

def custom_decrypt(text):
    reversed_text = text[::-1]

    bytes_hex = [reversed_text[i:i+2] for i in range(0, len(reversed_text), 2)]
    output = ""
    for h in bytes_hex:
        value = int(h, 16) - 4
        output += chr(value)

    return output








if __name__ == "__main__":
    main()
