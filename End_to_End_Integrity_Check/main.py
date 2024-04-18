import struct

def rotate_right(val, r_bits, max_bits):
    return (val >> r_bits) | (val << (max_bits - r_bits)) & 0xFFFFFFFF

def sha256(message):
    # Initialize hash values (first 32 bits of the fractional parts of the square roots of the first 8 primes)
    h = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    
    # Initialize constants
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    
    # Pre-processing
    message += b"\x80"  # append the bit '1' to the message
    while len(message) % 64 != 56:
        message += b"\x00"  # append 0 <= k < 512 bits '0', so that the resulting message length (in bytes) is congruent to 56 (mod 64)
    message += struct.pack(">Q", 8 * len(message))  # append length of message (before pre-processing), in bits, as 64-bit big-endian integer
    
    # Process the message in 512-bit chunks
    for chunk_index in range(0, len(message), 64):
        chunk = message[chunk_index:chunk_index + 64]
        words = [0] * 64
        
        # Break chunk into sixteen 32-bit big-endian words
        for i in range(16):
            start = i * 4
            words[i] = struct.unpack(">I", chunk[start:start + 4])[0]
        
        # Extend the sixteen 32-bit words into sixty-four 32-bit words
        for i in range(16, 64):
            s0 = rotate_right(words[i-15], 7, 32) ^ rotate_right(words[i-15], 18, 32) ^ (words[i-15] >> 3)
            s1 = rotate_right(words[i-2], 17, 32) ^ rotate_right(words[i-2], 19, 32) ^ (words[i-2] >> 10)
            words[i] = (words[i-16] + s0 + words[i-7] + s1) & 0xFFFFFFFF
        
        # Initialize hash value for this chunk
        a, b, c, d, e, f, g, h = h
        
        # Main loop
        for i in range(64):
            s1 = rotate_right(e, 6, 32) ^ rotate_right(e, 11, 32) ^ rotate_right(e, 25, 32)
            ch = (e & f) ^ ((~e) & g)
            temp1 = h + s1 + ch + k[i] + words[i]
            s0 = rotate_right(a, 2, 32) ^ rotate_right(a, 13, 32) ^ rotate_right(a, 22, 32)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = s0 + maj
            
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF
        
        # Add this chunk's hash to result so far
        h = (h + a) & 0xFFFFFFFF
        g = (g + b) & 0xFFFFFFFF
        f = (f + c) & 0xFFFFFFFF
        e = (e + d) & 0xFFFFFFFF
        d = (d + e) & 0xFFFFFFFF
        c = (c + f) & 0xFFFFFFFF
        b = (b + g) & 0xFFFFFFFF
        a = (a + h) & 0xFFFFFFFF
    
    # Produce the final hash value
    return "%08x%08x%08x%08x%08x%08x%08x%08x" % (h, g, f, e, d, c, b, a)

# Example usage
input_str = "Hello, World!"
key = "secret"

hashed_value = sha256(input_str.encode() + key.encode())
print("Hashed value:", hashed_value)
