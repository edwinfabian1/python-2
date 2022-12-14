"""¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?"""

def primos():

    for n in range(1,1001):
        cont = 0
        primo = 0  
        for i in range(1,n+1):
            if n % i == 0:
                cont += 1
        if cont == 2:
            primo += 1
        
            print (n)

primos()