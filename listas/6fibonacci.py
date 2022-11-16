#Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el
#usuario. Mínimo debe tener 5 elementos y máximo 20.



y = 1

x = 1
n = 0
while n < 5 or n > 20:
    n = int(input("Ingrese nro de 5 a 20 "))

print (x)
for i in range(n-1):
    print(y)
    z = y
    y += x
    x = z