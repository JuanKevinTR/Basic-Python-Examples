# Programa que calcula la letra del DNI a partir del número introducido.
# La letra se obtiene calculando el resto de la división del número del
# DNI por 23. A cada resultado le corresponde una letra:
# 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y; 7=F; 8=P; 9=D; 10=X; 11=B; 12=N;
# 13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L; 20=C; 21=K; 22=; 23=E;
#
# @author J. Kevin Trujillo
# Web: juankevintrujillo.com
# 
# Python version: 3.6

print("Calculadora de letra del DNI")

dni = int(input("Dígame su DNI (sin letra): "))
resto = dni % 23

# Creamos un diccionario
letras = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D',
          10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L',
          20: 'C', 21: 'K', 22: 'E'}

letra = str(letras[resto])

print(f"Su DNI (con letra) es: {dni}{letra}")
