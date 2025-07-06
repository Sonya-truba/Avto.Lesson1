import math


def square(a):
    return math.ceil(a*a)


a = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата = {square(a)}")


square(a)
