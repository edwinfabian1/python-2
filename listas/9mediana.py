"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la mediana de los números de la lista"""

import random

lista = []

for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))

for i in range (len(lista)):
    for j in range (i+1,len(lista)):
        if lista[i] > lista[j]:
            lista[i],lista[j] = lista[j],lista[i]
print(lista)

med = int(len(lista))
if med % 2 == 0:
    med2 = lista[med//2]
    med -= 1
    med1 = lista[med//2]
    print ("Las medianas son",med1,"y",med2)
      
else:
    med1 = lista[med//2]
    print ("La mediana es",med1)