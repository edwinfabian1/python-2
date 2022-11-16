"""Escribir un algoritmo que pida un valor entero que equivale a una cantidad de 
DINERO y calcule a cuantos billetes de 50.000, 20.000, 10.000, 5.000, 2.000, y 
1.000 equivalen. Si el usuario digita 282000 el programa debe responder cinco 
billetes de 50.000, un billete de veinte mil, un billete de diez mil, un billete de 
dos mil"""

x = int(input("Cunato dinero necesita? "))

if x >= 50000:
    y = x // 50000
    a = x % 50000
    print("billetes de 50.000 = ",y)
    x = a
if x >= 20000:
    y = x // 20000
    a = x % 20000
    print("billetes de 20.000 = ",y)
    x = a
if x >= 10000:
    y = x // 10000
    a = x % 10000
    print("billetes de 10.000 = ",y)
    x = a
if x >= 5000:
    y = x // 5000
    a = x % 5000
    print("billetes de 5.000 = ",y)
    x = a
if x>= 2000:
    y = x // 2000
    a = x % 2000
    print("billetes de 2.000 = ",y)
    x = a
if x >= 1000:
    y = x // 1000
    a = x % 1000
    print("billetes de 1.000 = ", y)