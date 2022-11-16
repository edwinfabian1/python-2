"""Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576"""

n = "0000000000"
while len(n) > 9:
    n = input("Digite un nro de hasta 9 digitos: ")

nf = ""
n = int(n)
while n > 0:
    nn = n // 10
    nd = n % 10
    n = nn
    nf += str(nd)
print (nf)