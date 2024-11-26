import random

# Function to compute the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse of a under modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate RSA keys
def rsa_generate_keys(p, q):
    # Check if p and q are prime numbers
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime numbers")

    # Calculate n = p * q
    n = p * q

    # Calculate Euler's Totient Function: φ(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)

    # Choose e (public exponent) such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate d (private exponent) such that (e * d) % φ(n) = 1
    d = mod_inverse(e, phi)

    # Public key (e, n) and private key (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Function to encrypt the message
def encrypt(message, public_key):
    e, n = public_key
    # Encrypt the message using the formula: cipher = (message ** e) % n
    encrypted_message = pow(message, e, n)
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Decrypt the message using the formula: decrypted = (cipher ** d) % n
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

# Main function to demonstrate the RSA algorithm
def main():
    # Input prime numbers p and q, and the message to encrypt
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    message = int(input("Enter the message (numeric): "))  # The message should be numeric

    # Generate public and private keys
    public_key, private_key = rsa_generate_keys(p, q)

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)

    # Output the results
    print("\nPublic Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

# Run the main function
if __name__ == "__main__":
    main()
