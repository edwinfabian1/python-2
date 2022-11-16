"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la suma y el promedio de los números de la lista"""

import random

lista = []
suma = 0
cont = 0

for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))
print (lista)

for i in lista:
    suma += i
    cont += 1
prom = round(suma / cont,1)
print("suma = ",suma)
print("promedio =",prom)