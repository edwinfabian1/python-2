spotify={}

def artista(spotify):
    artista=input('Ingrese el nombre del artista: ')
    genero=input('Ingrese el genero: ')
    cancion=input('Ingrese una cancion del artista: ')
    spotify.update({artista:{'Genero':genero,'Cancion':[cancion]}})
    return spotify

def agregar_cancion(spotify):
    artista=input('Ingrese el nombre del artista: ')
    cancion=input('Ingrese otra cancion del artista: ')
    if artista in spotify:
        spotify[artista.append(cancion)]
    return spotify
    
def buscar_artista(spotify):
    buscar=input('¿Que artista desea buscar?: ')
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('El artista',buscar,'se encuentra en spotify y su genero es:',spotify.get(artista))
        else:
            print('El artista',buscar,'no se encuentra en spotify')

while True:
    artista(spotify)
    print (spotify)
    pedir=int(input('Si desea agregar mas canciones a este artista, marque 1, de lo contrario, marque blablabla'))
    if pedir==1:
        agregar_cancion(spotify)
        pedir1=int(input('si desea agregar otra cancion, marque 1, de lo contrario para finalizar el programa, marque 0'))
        if pedir==0:
            break
            
        
print(spotify)   