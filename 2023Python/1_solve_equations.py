import math

print("ax^2+bx+c=0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print("x1=", x1)
print("x2=", x2)
