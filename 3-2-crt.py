def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    # Input: congruences is a list of tuples (a, m)
    # where a is the remainder and m is the modulus for each congruence

    N = 1
    for _, m in congruences:
        N *= m

    result = 0
    for a, m in congruences:
        Ni = N // m
        Mi = mod_inverse(Ni, m)
        result += a * Ni * Mi

    return result % N

# User input for the number of congruences
num_congruences = int(input("Enter the number of congruences: "))

# User input for each congruence
congruences = []
for i in range(num_congruences):
    a = int(input(f"Enter a{i+1}: "))
    m = int(input(f"Enter m{i+1}: "))
    congruences.append((a, m))

# Calculate and print the solution
result = chinese_remainder_theorem(congruences)
print("Solution:", result)


fruit = 'banana'
for letter in fruit :
    print(letter)

name = "jayavardhannarayana"
alpha = input(print("Enter the leter you want to search"))
count = 0 
for letter in name :
    if letter == alpha :
        count = count + 1
print (count)