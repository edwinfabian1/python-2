
#Diseñar una lista de spotify
mi_musica = {'un artista':{'una cancion':('heavy metal',4,00),
                        'otra cancion':('trash metal',3,56),
                        "segunda cancion":("metal" ,2,00)},
                        'otro artista':{}}

#Anexar canciones (genero, duracion) 1
def nueva_cancion(cancion,artista,genero,min,seg):
    if artista not in mi_musica:
        mi_musica[artista]={}
    if cancion in mi_musica[artista]:
        print ("Esta cancion ya existe: ")
    else:
        mi_musica[artista][cancion] = (genero,min,seg)
        print('Cancion agregada correctamente')
    input('Enter para continuar')

#Anexar artista 0
def nuevo_artista(artista):
    if artista in mi_musica:
        print ("Este artista ya existe: ")
    else:
        mi_musica[artista]={}
        print ('Artista agregado correctamente')
        print ('Para agregar canciones digita "S"')
        tema = input()
        if tema == 'S' or 's':
            menu(1)

#Buscar artista 2
def buscar_artista(artista):
    if artista in mi_musica:
        for i,j in sorted(mi_musica[artista].items()):
            print(i,'// genero:',j[0],'// duracion:',j[1],':',j[2])
        input('---Enter para continuar---')
    else:
        input('---Artista no existe---')

#Buscar cancion 3
def buscar_cancion(cancion):
    for h,i in mi_musica.items():
        for j,k in i.items():
            if j == cancion:
                print(h,j,k[0],sep='//',end='//')
                print(k[1],k[2],sep=':')
            else:
                input('---La cancion no existe---')

#eliminar artista 4
def eliminar_artista(artista):
    if artista in mi_musica:
        del mi_musica[artista]
        input('---Artista eliminado correctamente---')
    else:
        input('---Artista no existe---')
    

#Ordenar alfabeticamente 5
def ordenar():
    for h,i in mi_musica.items():
        for k in sorted(i.values()):
            print(i,h,k[0],sep='//',end='//')
            print(k[1],k[2],sep=':')
    input('---Enter para continuar---')

#Cual es el artista favorito 6
def mayor():
    for i in mi_musica.values():
        mayor = max(mi_musica[i])
        print(mayor)
    

#Artista que tiene la cancion mas larga 7
def larga():
    for h,i in mi_musica.items():
        for j,k in i.items():
            print(max())
            print(k[1],k[2],sep=':')

#Artista que tiene la cancion mas corta 8
def larga():
    for h,i in mi_musica.items():
        for j,k in i.items():
            print(min())
            print(k[1],k[2],sep=':')

#Menu
def menu(a):
    match a:
        case 0:
            print ("Nombre del nuevo artista: ")
            artista = input()
            nuevo_artista(artista)
        case 1:
            print('Nombre del artista?')
            artista = input()
            print('Nombre de la nueva cancion: ')
            cancion = input()
            print('Genero?')
            genero = input()
            print('Cuantos minutos dura?')
            min = int(input())
            print('Cuantos segundos dura?')
            seg = input()
            nueva_cancion(cancion,artista,genero,min,seg)
        case 2:
            print ('Nombre del artista que buscas')
            artista = input()
            buscar_artista(artista)
        case 3:
            print('Nombre de la cancion que buscas')
            cancion = input()
            buscar_cancion(cancion)
        case 4:
            print('Nombre del artista que deseas eliminar')
            artista = input()
            eliminar_artista(artista)
        case 5:
            ordenar()
        case 6:
            mayor()
        case 7:
            larga()
        case 8:
            corta()
        case 9:
            print("hasta la proxima")
while True:
    print('-----------------------------------','     Bienvenido','   ¿Que deseas hacer hoy?',sep='\n')
    print('0 = Agregar nuevo artista','1 = Agregar nueva cancion','2 = Buscar artista','3 = Buscar cancion','4 = Eliminar un artista','5 = Ver tu lista de reproducción ordenada','6 = ¿Cual es mi artista favorito?','7 = ¿Cual es mi cancion mas larga?','8 = ¿Cual es mi cancion mas corta?','9 = SALIR',sep="\n")
    a = int(input())
    menu(a)
    if a == 9:
        break

print(mi_musica)

