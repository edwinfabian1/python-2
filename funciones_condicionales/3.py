#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el
# número exceda los límites emita un mensaje y finalice el programa
def numero(n):

    if n < 0 or n > 9999:

        return("El número excede los limites permitidos!")

    else: return (len(str(n)))
n = int(input("Escriba un número entre 0 y 9.999: "))
print(numero(n))