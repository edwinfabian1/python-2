"""Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod."""

a = int(input("Digite primer nro: "))
b = int(input("Digite segundo nro: "))

if a < b:
    a,b = b,a

cont = 0
for i in range (b,a+1,b):
    if i < a:
        cont += 1
print (cont)
print (a-i)
        