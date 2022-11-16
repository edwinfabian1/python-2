"""Calcular la operación x n sin utilizar la función pow"""

x = int(input("Ingrese un nro: "))
n = int(input("Ingrese potencia: "))
p = 1

for i in range(n):
    p *= x

print(p)