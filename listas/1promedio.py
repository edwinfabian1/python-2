"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
del promedio o es igual al promedio de todos los números de la lista."""

import random

lista = []
suma = 0
cont = 0

for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))
    suma += lista[i]
    cont += 1
prom = suma/cont

print("El promedio es: ",prom)
for i in lista:
    if i > prom:
        print(i,"es mayor al promedio")
    elif i < prom:
        print(i,"es menor al promedio")
    else:
        print(i,"es igual al promedio")
