# Programa que pide un número de días, horas, minutos y segundos
# y calcula cuántos segundos son en total
# 
# @author J. Kevin Trujillo
# Web: juankevintrujillo.com
# 
# Python version: 3.6

print("Convertidor a segundos")

days = int(input("Dígame un número de días: "))
hours = int(input("Dígame un número de horas: "))
minutes = int(input("Dígame un número de minutos: "))
seconds = int(input("Dígame un número de segundos: "))

total = (days*86400) + (hours*3600) + (minutes*60) + seconds;

print(f"{days} días, {hours} horas, {minutes} minutos y {seconds} segundos son {total} segundos")

