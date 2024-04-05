def polybius_encrypt(plain_text):
    # Define the Polybius Square
    polybius_square = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '463',
        'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34',
        'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44',
        'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54',
        'Z': '55'
    }
    
    plain_text = plain_text.upper()  # Convert text to uppercase
    cipher_text = ""
    
    for char in plain_text:
        if char.isalpha():
            cipher_text += polybius_square[char] + " "
        elif char == ' ':
            cipher_text += ': '
    
    return cipher_text.strip()  # Remove trailing whitespace

def polybius_decrypt(cipher_text):
    # Define the Polybius Square
    polybius_square = {
        '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E',
        '21': 'F', '22': 'G', '23': 'H', '24': 'I', '463': 'J',
        '25': 'K', '31': 'L', '32': 'M', '33': 'N', '34': 'O',
        '35': 'P', '41': 'Q', '42': 'R', '43': 'S', '44': 'T',
        '45': 'U', '51': 'V', '52': 'W', '53': 'X', '54': 'Y',
        '55': 'Z'
    }
    
    cipher_text = cipher_text.split()
    plain_text = ""
    
    for pair in cipher_text:
        if pair in polybius_square:
            plain_text += polybius_square[pair]
        elif pair == ':':
            plain_text += ' '
    
    return plain_text


if __name__ == "__main__":
    # Example usage:
    plaintext = "HELLO WORLD"

    encrypted_text = polybius_encrypt(plaintext)
    print("Encrypted text:", encrypted_text)

    decrypted_text = polybius_decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)
