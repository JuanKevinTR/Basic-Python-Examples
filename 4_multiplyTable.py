# Programa que pide un número entero entre 1 y 10
# y escribe la tabla de múltiplicar de ese número
#
# @author J. Kevin Trujillo
# Web: juankevintrujillo.com
# 
# Python version: 3.6

print("Tabla de multiplicar")

num = int(input("Escriba un número entero entre 1 y 10: "))

while num < 1 or num > 10:
    print("\t¡No ha escrito un número entre 1 y 10")
    num = int(input("Escriba un número entero entre 1 y 10: "))

for i in range(num):
    print(num * (i+1))

