"""Algoritmo para hallar el m.c.d de dos números m y n por
el algoritmo de Euclides."""

m = int(input("Digite el primer nro: "))
n = int(input("Digite el segundo nro: "))

if m < n:
    m,n = n,m

r = m % n
while r > 0:
    m = n
    n = r
    if r != 0:
        e = r
        r = m % n
        
print(e)