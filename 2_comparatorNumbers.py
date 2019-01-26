# Programa que pide tres números y dice de cada uno 
# si es el más grande, el más pequeño o el mediano
# 
# @author J. Kevin Trujillo
# Web: juankevintrujillo.com
# 
# Python version: 3.6

print("Comparador de números")

num1 = int(input("Escriba un número (1): "))
num2 = int(input("Escriba un número (2): "))
num3 = int(input("Escriba un número (3): "))

#
# Número 1
#
if num1 >= num2 and num1 >= num3:
    print(num1, "es el más grande")
else:
    if num1 > num2 and num1 < num3:
        print(num1, "está en medio")
    else:
        print(num1, "es el más pequeño")

#
# Número 2
#
if num2 >= num1 and num2 >= num1:
    print(num2, "es el más grande")
else:
    if num2 > num1 and num2 < num1:
        print(num2, "está en medio")
    else:
        print(num2, "es el más pequeño")

#
# Número 3
#
if num3 >= num1 and num3 >= num1:
    print(num3, "es el más grande")
else:
    if num3 > num1 and num3 < num1:
        print(num3, "está en medio")
    else:
        print(num3, "es el más pequeño")



