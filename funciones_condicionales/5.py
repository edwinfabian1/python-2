"""Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo 
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan 
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que 
permita calcular el costo de una llamada dados los minutos de duración"""
def telefonia(n):
    if minutos <= 3:
        return minutos*200
    else:
        return minutos*250-150
minutos = float(input("Cantidad de minutos: "))  
 
print(telefonia(minutos))