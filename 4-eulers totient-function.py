def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def euler_totient_formula(n):
    factors = prime_factors(n)

    result = n
    for factor in set(factors):
        result *= (1.0 - (1.0 / factor))

    return int(result)

number = int(input("Enter a positive integer: "))

if number > 0:
    result = euler_totient_formula(number)
    print(f"Euler's Totient Function for {number} is: {result}")
else:
    print("Please enter a positive integer.")
   