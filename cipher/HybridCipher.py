from cipher.VigenereCipher import vigenere_encrypt, vigenere_decrypt
from cipher.PolybiusCipher import polybius_encrypt, polybius_decrypt


def hybrid_encrypt(plain_text, key):
    cipher_text_intermediate = vigenere_encrypt(plain_text, key)
    cipher_text = polybius_encrypt(cipher_text_intermediate)
    
    return cipher_text

def hybrid_decrypt(cipher_text, key):
    plain_text_intermediate = polybius_decrypt(cipher_text)
    plain_text = vigenere_decrypt(plain_text_intermediate, key)

    return plain_text


if __name__ == "__main__":
    # Example usage:
    plaintext = "HELLO WORLD"
    key = "KEY"

    # Encrypt the plaintext
    encrypted_text = hybrid_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = hybrid_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)