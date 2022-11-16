#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Sume los pares y saque el promedio de los impares

import random

lista = []

for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))
print (lista)

suma1 = 0
suma2 = 0
cont = 0

for i in lista:
    if i % 2 == 0:
        suma1 += i
    else:
        suma2 += i
        cont += 1
prom = round(suma2/cont,1)   
print ("Los pares suma: ",suma1)
print ("El promedio de los impares es: ",prom)