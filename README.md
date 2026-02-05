# Encryption System 🔐

**Description:**  
This project implements an **encryption and decryption system** with **five different methods**, allowing the user to choose between them and use custom keys when needed.  

---

## 🚀 Main Functionality
The program runs a **main loop** that allows the user to:  
1. Choose to **encrypt**, **decrypt**, or **exit**.  
2. Select one of the **five available methods**.  
3. Enter the **text** and, if applicable, the **key**.  
4. Get the **final result** and decide whether to continue or exit.  

---

## 🔧 Available Encryption Methods

### 1. Caesar
- **Encrypt:** Adds the key (number) to the ASCII value of each character.  
- **Decrypt:** Subtracts the same key to recover the original text.  
- **Key:** Integer number.  

### 2. Vigenère
- **Encrypt:** Combines the text with a **keyword** (letters only) to encrypt.  
- **Decrypt:** Subtracts the keyword offset to recover the original text.  
- **Key:** Word consisting of letters only.  

### 3. Substitution
- **Encrypt/Decrypt:** Replaces each letter according to a **custom alphabet** defined by the user.  
- **Key:** A 26-letter string representing the reordered alphabet.  

### 4. Base64
- **Encrypt:** Converts the text to bytes and encodes it in Base64.  
- **Decrypt:** Decodes Base64 back to the original text.  
- **Key:** Not required.  

### 5. Custom
- **Encrypt:**  
  1. Adds 4 to the ASCII value of each character.  
  2. Converts each value to a 2-digit hexadecimal.  
  3. Concatenates and **reverses** the final string.  
- **Decrypt:** Reverses the process to recover the original text.  
- **Key:** Not required.  

---

## 🔑 Key Management
The **get_key()** and **validate_key()** functions ensure the user enters the correct key based on the method:  

| Method       | Key Type                        | Validation                           |
|--------------|---------------------------------|--------------------------------------|
| Caesar       | Integer number                  | Must be a valid number                |
| Vigenère     | Letters only                    | Must contain letters only             |
| Substitution | 26-letter alphabet              | Exactly 26 letters                    |
| Base64       | None                            | Always valid                          |
| Custom       | None                            | Always valid                          |

---











