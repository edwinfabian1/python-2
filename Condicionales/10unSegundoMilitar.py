"""Solicite al usuario la hora en formato hh:mm:ss (hora militar, 24 horas). El 
programa debe responder que hora será un segundo después. Ej: ingreso 
11:59:59, el programa responde 12:00:00"""

h = int(input("Horas = "))
if h > 0 and h < 24:
    m = int(input("Minutos = "))
    if m > 0 and m < 60:
        s = int(input("Segundos = "))
        if s > 0 and s < 60:
            if s+1 == 60:
                s = "00"
                m += 1
            else: s += 1
            if m == 60:
                m = "00"
                h += 1
            if h == 24:
                h = "00"
            
            print(h,m,s,sep=":")
            exit()
print("error")