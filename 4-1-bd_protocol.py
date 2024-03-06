def findGroupKey(p, g, arr):
    n = len(arr)
    print("P", p, "g", g)
    for i in range(n):
        print("User", i+1, "key:", arr[i])
    
    if g < 1 or g > p:
        print("BD Protocol not possible")
    else:
        R = [0] * n
        for i in range(n):
            nxt = pow(g, arr[(i+1) % n], p)
            prev = pow(g, arr[(i-1+n) % n], p)
            r = pow(nxt * modularInverse(prev, p), arr[i], p)
            R[i] = r

        for i in range(n):
            temp = n
            j = i
            k = 1
            exponent = n * arr[i]
            while temp > 0:
                temp -= 1
                k *= modularExponentiation(R[j % n], temp, p) % p
                k %= p
                j += 1
            k *= modularExponentiation(modularExponentiation(g, arr[(i - 1 + n) % n], p), exponent, p) % p
            k %= p
            print("Common Group Key of user", i + 1, "is", k)

def modularInverse(a, m):
    a = ((a % m) + m) % m
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def modularExponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

# Main function
arr = [3, 4, 5]
p = 11
g = 2
findGroupKey(p, g, arr)