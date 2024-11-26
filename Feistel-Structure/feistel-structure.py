def feistel_round(left, right, key): 
    '''Perform one round of the Feistel cipher. 
    :param left: Left half of the data 
    :param right: Right half of the data 
    :param key: Key for the round 
    :return: (new_left, new_right) - the updated left and right halves 
     '''
    # Simple function F to mix the right half with the key 
    def F(right, key): 
        return (right ^ key)  # Simple XOR operation for the function F 
    new_left = right 
    new_right = left ^ F(right, key)  # XOR the left half with the function F's result   
    return new_left, new_right 
 
def feistel_encrypt(plaintext, rounds, keys): 
    """ 
    Encrypt the plaintext using the Feistel network. 
    :param plaintext: Integer input representing the plaintext to encrypt 
    :param rounds: Number of Feistel rounds 
    :param keys: List of round keys 
    :return: Encrypted ciphertext 
    """ 
    # Split plaintext into left and right halves (assuming 32-bit input for simplicity) 
    left = plaintext >> 16  # Left 16 bits 
    right = plaintext & 0xFFFF  # Right 16 bits 
     
    # Perform the specified number of rounds 
    for i in range(rounds): 
        left, right = feistel_round(left, right, keys[i]) 
     
    # Combine the final left and right to form the ciphertext 
    ciphertext = (left << 16) | right 
    return ciphertext 
 
def feistel_decrypt(ciphertext, rounds, keys): 
    """ 
    Decrypt the ciphertext using the Feistel network. 
    :param ciphertext: Integer input representing the ciphertext to decrypt 
    :param rounds: Number of Feistel rounds 
    :param keys: List of round keys 
    :return: Decrypted plaintext 
    """ 
    # Split ciphertext into left and right halves (assuming 32-bit input for simplicity) 
    left = ciphertext >> 16  # Left 16 bits 
    right = ciphertext & 0xFFFF  # Right 16 bits 
     
    # Perform the rounds in reverse order for decryption 
    for i in range(rounds - 1, -1, -1): 
        left, right = feistel_round(left, right, keys[i]) 
     
    # Combine the final left and right to form the plaintext 
    plaintext = (left << 16) | right 
    return plaintext 
 
# Example usage 
if __name__ == "__main__": 
    plaintext = 0x12345678  # Example plaintext (32-bit integer) 
    rounds = 4  # Number of Feistel rounds 
    keys = [0x0F0F, 0xF0F0, 0xAAAA, 0x5555]  # Example keys for each round 
     
    print(f"Plaintext: {hex(plaintext)}") 
     
    # Encrypt the plaintext 
    ciphertext = feistel_encrypt(plaintext, rounds, keys) 
    print(f"Ciphertext: {hex(ciphertext)}") 
     
    # Decrypt the ciphertext 
    decrypted = feistel_decrypt(ciphertext, rounds, keys) 
    print(f"Decrypted: {hex(decrypted)}")
