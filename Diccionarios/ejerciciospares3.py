#pares
#prueba atletica salto largo mostrar el promedio de mas alto a mas bajo


prueba_atletica = {}

while True:
    name = input("Ingresa el nombre del competidor: ")
    if name == '':
        break

    score = int(input("Ingresa la distancia recorrida (0-60): "))
    if score not in range(0, 61):
	    break

    if name in prueba_atletica:
        prueba_atletica[name] += (score,)
    else:
        prueba_atletica[name] = (score,)

print(prueba_atletica)
for name in sorted(prueba_atletica.keys()):
    adding = 0
    counter = 0
    for score in prueba_atletica[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

for score in sorted(prueba_atletica.value):
    print(score)