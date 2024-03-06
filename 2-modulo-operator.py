def modulos(dividend,divisor):
    if divisor == 0:
        raise ValueError("Cannot be divided")
    remainder = dividend % divisor

    

    return remainder

dividend = int(input("Enter the dividend"))
divisor = int(input("Enter the divisor"))

result = modulos(dividend, divisor)

print(result)