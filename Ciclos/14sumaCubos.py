"""Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número."""


for j in range(100,1000):
    suma = 0
    i = j
    while i > 0:
        nd = i % 10
        nn = i // 10
        i = nn
        cubo = nd**3
        suma += cubo

    if suma == j:
        print (j)