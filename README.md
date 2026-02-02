# Encryption System
#### Description:

Hello world, thank you very much for reading this. In this project, I created an encryption and decryption system with five different methods and different keys that can be chosen by the user.


### main:

In the main function, create a large while loop to keep us in the system when the user makes a mistake at some point.
The program starts by asking if you want to encrypt, decrypt, or exit, then it will give you the 5 different methods available.
In the program, request the text below and, if it concerns the type of method, also request the key.

Finally, it will deliver the finished text and the option to continue with another request or simply exit the program.

### choice methods:

The select_method() function provides us with the different options we can select and, in this way, return the method to the main function.


### the second main functions:

In the two functions of encrypt and decrypt, what happens is that it routes the rest of the program, taking the values obtained when selecting the method, the text, and the key.
This way, it takes the selected options and triggers the function that will create the result.


### methods:

In this program, we have five different methods, which are Caesar, Vigenere, Substitution, Base64, and Custom.

#### caesar:
In caesar_encrypt(text, shift), we take the text and a key (a number), adding the key to the ASCII value of each character, which transforms the text.

In caesar_decrypt(text, shift), we perform the opposite operation, subtracting the same key to recover the original text.

#### vigenere:
In vigenere_encrypt(text, key), we take the text and a key (letters), add the offset of each text letter with the corresponding key letter, and return the encrypted text.

In vigenere_decrypt(text, key), we perform the same process, but instead of adding the key offset, we subtract it to recover the original text.

#### substitution:
In this method, we take both a text and a key.
The key is a rearranged version of the alphabet, where each letter is replaced by a new one according to the custom order you provide.
This reordered alphabet defines how each character in the original text will be substituted.

#### base64:
One of the methods I wanted to include is Base64, which converts the text into bytes, encodes those bytes in Base64, and then returns the result as a text string.
In this case, no key is needed, since Base64 is an encoding method rather than a cipher.

#### custom:
n this method, no keys are needed. Each character in the text has four added to its ASCII value.
The resulting value of each character is then converted into a two-digit hexadecimal number (removing the 0x prefix).
All hexadecimal values are concatenated, and finally, the entire resulting string is reversed.
The reversed string is the encrypted output returned by the function.




### key:
get_key(method) and validate_key(method, key):

These functions prompt the user to provide the appropriate key based on the encryption method and validate whether the key is valid.

Caesar:
Prompts for a numeric key.
If the input is not a valid number, returns None.
Must be an integer.

Vigenère:
Prompts for a keyword consisting solely of letters.
Must be a string containing only letters.

Substitution:
Prompts for a substitution alphabet, which must contain exactly 26 letters.
Must be a string of exactly 26 letters

Other methods:
Returns None, as no key is required.
Always valid (no key required).













