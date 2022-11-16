# Escribe un programa que pida tres números y que escriba si
# son los tres iguales, si hay dos iguales o si son los tres distintos
def programa(a,b,c):


    if a == b and c == b:
        return("los 3 números son iguales")
    elif a == b or c == b or c == a:
        return ("Hay dos números iguales")
    else: return("Los 3 números son distintos")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(programa(a,b,c))