import random

def mod_exp(base, exp, mod):
    # Efficient modular exponentiation using the square-and-multiply method
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base ** 2) % mod

    return result

def generate_key(p, g):
    # Step 1: Choose private key randomly
    private_key = random.randint(2, p - 2)
    
    # Step 2: Compute public key using modular exponentiation
    public_key = mod_exp(g, private_key, p)
    
    # Return private and public keys
    return private_key, public_key

def compute_shared_secret(public_key, private_key, p):
    # Step 3: Compute shared secret using modular exponentiation
    return mod_exp(public_key, private_key, p)

def main():
    # Input prime number and primitive root
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root (g): "))

    # Generate keys for Alice and Bob
    alice_private_key, alice_public_key = generate_key(p, g)
    bob_private_key, bob_public_key = generate_key(p, g)

    # Exchange public keys
    shared_secret_alice = compute_shared_secret(bob_public_key, alice_private_key, p)
    shared_secret_bob = compute_shared_secret(alice_public_key, bob_private_key, p)

    # Print the shared secrets
    print("Prime Number (p):", p)
    print("Primitive Root (g):", g)
    print("Private Key (Alice):", alice_private_key)
    print("Public Key (Alice):", alice_public_key)
    print("Private Key (Bob):", bob_private_key)
    print("Public Key (Bob):", bob_public_key)
    print("Shared Secret (Alice):", shared_secret_alice)
    print("Shared Secret (Bob):", shared_secret_bob)

if __name__ == "__main__":
    main()
