#Pedir 3 numeros e indicar cual de ellos es el valor del medio.
#Ej 11, 2 1000, el 
#valor del medio es 11. No use operadores lógicos

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b:
    if a < c: medio = a
if b > c:
    if b < a: medio = b
if c > a:
    if c < b: medio = c
if a > c:
    if a < b: medio = a
if b > a:
    if b < c: medio = b
if c > b:
    if c < a: medio = c

print ("El valor del medio es", medio)