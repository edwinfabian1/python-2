"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la desviación estandar"""

import random
tam=round(random.randint(10,25))
vec=[round(random.random()*100)for i in range(tam)]
dif=[]
media=0
print("Tam=",tam)
#for i in range(tam):
#    vec.append(round(random.random()*100))
print(vec)
for i in vec:
    media+=1
    media=media/len(vec)
print("media",media)
suma=0
for i in range(len(vec)):
    x=(vec[i]-media)**2
    dif.append(x) 
    suma+=x
print("suma",suma) 
print("desv estandar",(suma/len(vec))**0.5)