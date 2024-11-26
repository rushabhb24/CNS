import random

# Function to calculate (base^exponent) % modulus (modular exponentiation)
def power_mod(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Function to simulate the Diffie-Hellman key exchange with a Man-in-the-Middle (MitM) attack step-by-step
def diffie_hellman_mitm(p, g):
    # Step 1: Alice chooses a private key 'a'
    a = random.randint(1, p - 1)
    A = power_mod(g, a, p)  # Alice's public key

    # Step 2: Eve intercepts Alice's message and generates her own private key 'e'
    e = random.randint(1, p - 1)
    E = power_mod(g, e, p)  # Eve's public key
    print(f"Alice sends A = {A} to Eve")

    # Step 3: Eve sends her public key 'E' to Bob instead of Alice's A
    print(f"Eve sends E = {E} to Bob instead of A")

    # Step 4: Bob chooses a private key 'b'
    b = random.randint(1, p - 1)
    B = power_mod(g, b, p)  # Bob's public key
    print(f"Bob sends B = {B} to Eve")

    # Step 5: Eve intercepts Bob's message and sends her own public key 'E' to Alice instead of B
    print(f"Eve sends E = {E} to Alice instead of B")

    # Step 6: Eve computes the shared secret with Alice using E and Alice's private key a
    key_eve_alice = power_mod(E, a, p)
    print(f"Eve computes the shared secret with Alice: {key_eve_alice}")

    # Step 7: Eve computes the shared secret with Bob using E and Bob's private key b
    key_eve_bob = power_mod(E, b, p)
    print(f"Eve computes the shared secret with Bob: {key_eve_bob}")

    # Step 8: Final keys that Alice and Bob think they share
    print("\n--- Final Keys ---")
    print(f"Alice thinks she shares the key {key_eve_alice} with Bob, but actually with Eve")
    print(f"Bob thinks he shares the key {key_eve_bob} with Alice, but actually with Eve")

# Main function to run the Diffie-Hellman exchange with MitM
def main():
    # Input: Prime number p and base g
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a base number g: "))

    # Perform Diffie-Hellman key exchange with a Man-in-the-Middle attack step-by-step
    diffie_hellman_mitm(p, g)

# Run the program
if __name__ == "__main__":
    main()
