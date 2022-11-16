"""Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta."""
def num():
    n = 1
    cont = 0

    while n >= 0:
        n = int(input("Escriba un nro: "))
        cont  += 1
    return(cont-1)
print(num())