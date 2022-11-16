"""Escribir un programa que visualice la siguiente figura, utilizando ciclos.
El usuario decide cuantas líneas quiere imprimir

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *"""


def programa(x):
    for i in range(x):
        print("*"*(i+1))
num = int(input("Cuantas lineas desea imprimir? "))

print(programa(num))
