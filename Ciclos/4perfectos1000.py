"""Determinar cuales y cuantos números perfectos hay entre 1 y 1000?"""
cont = 0
def numentre(num)

for n in range(1,1001):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    if suma == n:
        cont += 1
        print(n)
print("Total de nros perfectos: ",cont)