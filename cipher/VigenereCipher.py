def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        shift = ord(key[i % key_length]) - ord('A')  # Convert letter to shift value
        if plain_text[i].isalpha():
            if plain_text[i].islower():
                cipher_text += chr((ord(plain_text[i]) - ord('a') + shift) % 26 + ord('a'))
            else:
                cipher_text += chr((ord(plain_text[i]) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_text += plain_text[i]
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    key_length = len(key)
    for i in range(len(cipher_text)):
        shift = ord(key[i % key_length]) - ord('A')  # Convert letter to shift value
        if cipher_text[i].isalpha():
            if cipher_text[i].islower():
                plain_text += chr((ord(cipher_text[i]) - ord('a') - shift) % 26 + ord('a'))
            else:
                plain_text += chr((ord(cipher_text[i]) - ord('A') - shift) % 26 + ord('A'))
        else:
            plain_text += cipher_text[i]
    return plain_text


if __name__ == "__main__":
    # Example usage:
    plaintext = "HELLO WORLD"
    key = "KEY"

    # Encrypt the plaintext
    encrypted_text = vigenere_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)
