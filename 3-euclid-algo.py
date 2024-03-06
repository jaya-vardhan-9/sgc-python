def euclidean_algorithm(a, b):
    while b != 0: # loop goes untill b becomes zero 
        a, b = b, a % b  # it keeps on inter changing the values as a=b & b= a mod b(remainder)
    return a             # this returns the gcd

a = int(input("Enter value of a: "))
b = int(input("Enter the value of b: "))

result = euclidean_algorithm(a,b)

print(f"The gcd of a,b is{result}")