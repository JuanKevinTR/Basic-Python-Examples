# Programa que pregunta cuantos números introducirá el usuario,
# pide esos X numeros y escribe la cantidad de números pares
# 
# @author J. Kevin Trujillo
# Web: juankevintrujillo.com
# 
# Python version: 3.6

amount = int(input("Dígame cuantos números va a escribir: "))
pairs = 0

for i in range(amount):
    num = int(input(f"Dígame el número {i+1}: "))
    if num % 2 == 0:
        pairs = pairs + 1

print(f"Ha escrito {pairs} número(s) par(res)")


