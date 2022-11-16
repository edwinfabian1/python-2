import random

tiemp =[]

for i in range(30):
    tiemp.append(random.randint(5,28))
print(tiemp)

a=tiemp[:15]
b=tiemp[16:]
c=tiemp[:10]
d=tiemp[10:20]
e=tiemp[20:]

list=[a,b,c,d,e]
for i in list:
    suma=0
    for j in i:
        suma+=j
        
    print(round(suma/len(i),2))