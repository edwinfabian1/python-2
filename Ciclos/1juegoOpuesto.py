"""pedir numeros, imprimirlo con el opuesto 
(ejemplo 5 opuesto -5, -10 opuesto 10), 
finaliza con cero y diga cuantos ingreso"""

i = 1
cont = 0

while i != 0:
	i = int(input("Escriba un nro "))
	if i != 0:
	    print(i,"opueso",-(i))
	    cont += 1
print(cont)