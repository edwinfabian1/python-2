"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la moda de los números de la lista"""

import random

lista = [int(random.random()*100) for i in range (random.randint(10,25))]

#for i in range (random.randint(10,25)):
 #   lista.insert(0,int(random.random()*100))
print(lista)

moda = []
for i in range (len(lista)):
    cont = 1
    for j in range (i+1,len(lista)):
        if lista[i] == lista[j]:
            cont += 1
    moda.append(cont)

rep = 0
for i in moda:
        if i > rep:
            rep = i

if rep == 1:
    print ("Ningún nro se repite")
else:
    mod = ""
    for i in range (len(moda)):
        if moda[i] == rep:
            mod += str(lista[i])
            mod += " "
    print("La moda es:",mod)
