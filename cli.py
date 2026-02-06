from encryption import (
    encrypt,
    decrypt,
    validate_key,
    CAESAR,
    VIGENERE,
    SUBSTITUTION,
    BASE64,
    CUSTOM,
)


def select_method():
    print("\nAvailable methods:")
    print("1) Caesar")
    print("2) Vigenere")
    print("3) Substitution")
    print("4) Base64")
    print("5) Custom")

    options = {
        "1": CAESAR,
        "2": VIGENERE,
        "3": SUBSTITUTION,
        "4": BASE64,
        "5": CUSTOM,
    }

    return options.get(input("Choose method (1–5): ").strip())


def get_key(method):
    if method == CAESAR:
        try:
            return int(input("Numeric key (shift): "))
        except ValueError:
            return None

    if method == VIGENERE:
        return input("Keyword (letters only): ").strip()

    if method == SUBSTITUTION:
        return input("Substitution alphabet (26 letters): ").strip()

    return None


def main():
    while True:
        print("\n=== Encryption System ===")
        print("1) Encrypt")
        print("2) Decrypt")
        print("3) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("Exiting...")
            break

        if choice not in ("1", "2"):
            print("Invalid option")
            continue

        method = select_method()
        if not method:
            print("Invalid method")
            continue

        text = input("Enter the text: ")
        key = get_key(method)

        if not validate_key(method, key):
            print("Invalid key for this method")
            continue

        try:
            result = (
                encrypt(method, text, key)
                if choice == "1"
                else decrypt(method, text, key)
            )
            print("\nResult:\n", result)

        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nDo you want to perform another operation? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
