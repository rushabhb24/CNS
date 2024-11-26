import hashlib

def calculate_sha1_digest(text):
    """
    Calculate the SHA-1 message digest of the given text.
    
    :param text: Input string
    :return: SHA-1 message digest in hexadecimal format
    """
    # Create a SHA-1 hash object
    sha1_hash = hashlib.sha1()
    
    # Update the hash object with the input text (encoded to bytes)
    sha1_hash.update(text.encode('utf-8'))
    
    # Return the hexadecimal digest
    return sha1_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    input_text = input("Enter the text to hash: ")
    digest = calculate_sha1_digest(input_text)
    print(f"SHA-1 Digest: {digest}")
