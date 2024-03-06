def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {a} modulo {m}")
    else:
        return (x % m + m) % m

modulus = int(input("Emter the wrt mod value : "))
number = int(input("Enter the num to be calculated: "))

try:
    inverse = mod_inverse(number, modulus)
    print(f"The modular multiplicative inverse of {number} modulo {modulus} is: {inverse}")
except ValueError as e:
    print(e)
