"""Determinar si un numero es o no es primo"""

n = int(input("Ingrese un nro: "))
cont = 0

for i in range(1,n+1):
    if n % i == 0:
        cont += 1
if cont > 2:
        print("El nro NO es primo")
else: print("El nro SI es primo")