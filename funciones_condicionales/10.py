"""Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N."""
def multiplos():
    n = int(input("Escriba un número: "))

    for i in range(1,n+1):
        if i % 5 == 0:
            print(i)
multiplos()
