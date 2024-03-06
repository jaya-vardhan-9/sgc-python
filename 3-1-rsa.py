import random

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n is composite

    return True  # n is probably prime

def generate_prime(bits):
    """Generate a random prime number with the specified number of bits."""
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Extended Euclidean Algorithm to find modular inverse."""
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits):
    """Generate RSA public and private key pair."""
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public key (e, n), where 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate private key (d, n), where d is the modular inverse of e modulo phi
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    """Encrypt a message using the public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt a message using the private key."""
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example usage:
bits = 1024  # Adjust the number of bits as needed for the desired security level
public_key, private_key = generate_keypair(bits)

message = input("Enter the message you want to encrypt: ")
print("Original Message:", message)

# Encryption
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
