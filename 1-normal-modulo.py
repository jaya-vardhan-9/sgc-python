# normal way of getting modulo is by showing the remainder so we cant get the negative values mod

def modulos(dividend,divisor):
    if divisor == 0:
        raise ValueError("Cannot be divided")
    qoutient = dividend // divisor

    remainder = dividend-(divisor*qoutient)  #dividend = (divisor*qoutient)+remainder

    return remainder

dividend = int(input("Enter the dividend"))
divisor = int(input("Enter the divisor"))

result = modulos(dividend, divisor)

print(result)