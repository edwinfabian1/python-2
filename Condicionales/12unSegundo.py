"""Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la 
hora que será dentro de 1 segundo"""

h = int(input("Horas = "))
if h >=0 and h < 12:
    m = int(input("Minutos = "))
    if m >= 0 and m < 60:
        s = int(input("Segundos = "))
        if s >= 0 and s < 60:
            if s+1 == 60:
                s = "00"
                m += 1
            else: s += 1
            if m == 60:
                m = "00"
                h += 1
            if h == 12:
                h = "00"
            
            print(h,m,s,sep=":")
            exit()
print("error")