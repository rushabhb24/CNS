import random

# Helper function to convert a string to a continuous binary format
def string_to_continuous_binary(s):
    return ''.join(format(ord(char), '08b') for char in s)

# Function to generate a random key of specified length
def random_key(n):
    return ''.join(chr(random.randint(0, 255)) for _ in range(n))

# Simple XOR function for pseudo encryption
def xor_block(block, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(block, key))

# Split the input block into two halves
def split_block(block):
    mid = len(block) // 2
    return block[:mid], block[mid:]

# DES-like encryption function (simplified with left and right halves)
def des_like_encrypt(plain_text):
    # Pad the plaintext to be 8 bytes long
    if len(plain_text) % 8 != 0:
        plain_text += ' ' * (8 - len(plain_text) % 8)
    
    # Split plaintext into 8-byte blocks (64 bits)
    blocks = [plain_text[i:i+8] for i in range(0, len(plain_text), 8)]
    
    # Placeholder for the ciphertext
    ciphertext_blocks = []
    
    # Initial round keys (15 random 4-byte keys for rounds 1-15)
    round_keys = [random_key(4) for _ in range(15)]
    final_round_key = random_key(8)  # Different 8-byte key for the 16th round
    
    first_round_binary = None  # To store the binary output of the first round
    
    # Process each block individually
    for block in blocks:
        left, right = split_block(block)  # Split into left and right halves (32 bits each)
        
        # First round
        temp_right = right
        right = xor_block(left, round_keys[0])  # XOR left half with round key to form new right
        left = temp_right  # Swap halves
        
        first_round_ciphertext = left + right  # Save this for output
        if first_round_binary is None:  # Only for the first block
            first_round_binary = string_to_continuous_binary(first_round_ciphertext)
        
        # Rounds 2-15
        for i in range(1, 15):
            temp_right = right
            right = xor_block(left, round_keys[i])  # XOR left half with round key to form new right
            left = temp_right  # Swap halves
        
        # 16th round with a different transformation (shift operation)
        temp_right = right
        shifted_left = ''.join(chr((ord(c) << 1) & 0xFF) for c in left)  # Shift left by 1 bit for each char
        right = xor_block(shifted_left, final_round_key)  # XOR shifted left half with final round key
        left = temp_right  # Swap halves
        
        final_round_ciphertext = left + right  # Final output after 16th round
        
        # Append final round ciphertext
        ciphertext_blocks.append(final_round_ciphertext)
    
    # Combine all ciphertext blocks
    final_ciphertext = ''.join(ciphertext_blocks)
    
    return first_round_binary, final_ciphertext

# Main function to get user input and perform encryption
def main():
    # Plaintext input from the user
    plain_text = input("Enter the plaintext message: ")
    
    # Encrypt the message
    first_round_binary, final_ciphertext = des_like_encrypt(plain_text)
    
    # Display the ciphertext after the first round in binary and after the 16th round in regular string format
    print(f"Ciphertext after 1st round (binary): {first_round_binary}")
    print(f"Ciphertext after 16th (final) round: {final_ciphertext}")

if __name__ == "__main__":
    main()
