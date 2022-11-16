"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)"""

import random

lista = [int(random.random()*100) for i in range (random.randint(10,25))]

#for i in range (random.randint(10,25)):
    #lista.insert(0,int(random.random()*100))
print (lista)
    
for i in range (len(lista)):
    for j in range (i+1,len(lista)):
        if lista[i] > lista[j]:
            lista[i],lista[j] = lista[j],lista[i]
print (lista)

for i in range (len(lista)):
    for j in range (i+1,len(lista)):
        if lista[i] < lista[j]:
            lista[i],lista[j] = lista[j],lista[i]
print (lista)