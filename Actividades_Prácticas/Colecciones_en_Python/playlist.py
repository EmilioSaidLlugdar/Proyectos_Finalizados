print('*** Playlist de Canciones ***')

#creamos la lista vacia
lista_reproduccion = []
nro_canciones = int(input('Cuantas canciones deseas agregar: '))

#iteramos cada elemento de la lista para agregar
for i in range(nro_canciones):
    cancion= input(f'Ingresa la canción {i + 1}:')
    cancion.title()
    lista_reproduccion.append(cancion)

#ordenamos
lista_reproduccion.sort()



#mostramos iterando cada elemento
print('\n')
for cancion in lista_reproduccion:
    print(f'- {cancion}')