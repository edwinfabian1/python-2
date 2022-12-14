"""Determinar los divisores de un número introducido por teclado"""
def divisores():
    n = int(input("Ingrese un nro. "))

    for i in range(1,n+1):
        if n % i == 0:
            return i
print(divisores())