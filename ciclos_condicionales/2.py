"""Calcular la operación x n sin utilizar la función pow"""
def calcular(q,p):
    elevado=q     
    while p >1:
        elevado*=q
        p-=1
    return elevado
x = int(input("Ingrese un nro: "))
n = int(input("Ingrese potencia: "))


print(calcular(x,n))