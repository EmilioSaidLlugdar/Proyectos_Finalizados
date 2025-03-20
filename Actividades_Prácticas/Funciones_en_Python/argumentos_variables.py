print('----- Argumentos Variables ------')

def superheroes_superpoderes(superheroe, nombre, *args):
    print(f'\nSuperheroe: {superheroe} - {nombre}')
    #iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

#llamar a la funcion
superheroes_superpoderes('Spiderman','Peter Parker', 'Instinto Arácnido', 'Telaraña')
superheroes_superpoderes('Batman', 'Bruce Wayne', 'Millonario', 'Playboy', 'Artes Marciales')