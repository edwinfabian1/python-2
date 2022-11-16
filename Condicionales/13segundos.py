"""Solicite al usuario una cantidad numérica que expresa segundos (medida de 
tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso"""

t = int(input("Escriba la cantidad de segundos: "))
s = "00"
m = "00"
h = "00"
j = "am"

if t >= 60:
    s = t % 60
    m = t // 60
    t = m
    if t >= 60:
        m = t % 60
        h = t // 60
        t = h
        if t > 12:
            h = t % 12
            j = "pm"
else: s = t
print (h,m,s,sep=":",end=' ')
print (j)