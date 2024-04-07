def polybius_encrypt(plain_text):
    # Define the Polybius Square
    polybius_square = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '16', 'G': '17', 'H': '18', 
        'I': '21', 'J': '22', 'K': '23', 'L': '24', 'M': '25', 'N': '26', 'O': '27', 'P': '28', 
        'Q': '31', 'R': '32', 'S': '33', 'T': '34', 'U': '35', 'V': '36', 'W': '37', 'X': '38', 
        'Y': '41', 'Z': '42', 'a': '43', 'b': '44', 'c': '45', 'd': '46', 'e': '47', 'f': '48', 
        'g': '51', 'h': '52', 'i': '53', 'j': '54', 'k': '55', 'l': '56', 'm': '57', 'n': '58', 
        'o': '61', 'p': '62', 'q': '63', 'r': '64', 's': '65', 't': '66', 'u': '67', 'v': '68', 
        'w': '71', 'x': '72', 'y': '73', 'z': '74'
    }
    
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
        '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '16': 'F', '17': 'G', '18': 'H', 
        '21': 'I', '22': 'J', '23': 'K', '24': 'L', '25': 'M', '26': 'N', '27': 'O', '28': 'P', 
        '31': 'Q', '32': 'R', '33': 'S', '34': 'T', '35': 'U', '36': 'V', '37': 'W', '38': 'X', 
        '41': 'Y', '42': 'Z', '43': 'a', '44': 'b', '45': 'c', '46': 'd', '47': 'e', '48': 'f', 
        '51': 'g', '52': 'h', '53': 'i', '54': 'j', '55': 'k', '56': 'l', '57': 'm', '58': 'n', 
        '61': 'o', '62': 'p', '63': 'q', '64': 'r', '65': 's', '66': 't', '67': 'u', '68': 'v', 
        '71': 'w', '72': 'x', '73': 'y', '74': 'z'
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
