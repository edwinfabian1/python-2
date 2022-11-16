#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Muestre cuales y cuantos son primos
import random
lista = [int(random.random()*100) for i in range (random.randint(10,25))]
suma = 0


#for i in range (random.randint(10,25)):
    #lista.insert(0,int(random.random()*100))



print(lista)
for i in lista:
    cont = 0
    for j in range (1,i+1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        print(i,"es primo")
        suma += 1
    else:
        print(i,"no es primo")
print("Cantidad de primos ",suma)