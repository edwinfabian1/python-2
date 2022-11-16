"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que
posiciones esta. Si no está agréguelo al final de la lista."""

import random

lista = []

for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))

n = int(input("Ingrese un nro "))

cont = 0
pos = ""
for i in range (len(lista)):
    if lista[i] == n:
        cont += 1
        pos += str(i)
        pos += " "

if cont == 0:
    lista.append(n)
    print (lista)
else:
    print (n,"esta",cont,"veces")
    print ("Posición(es)",pos)