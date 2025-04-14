from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas
opcion = None
while opcion != 4:
    try:
        print('Opciones'.center(10,'*'))
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar Catálogo de Peliculas')
        print('4. Salir')
        opcion=int (input('Ingresa tu opcion:  '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de una Pelicula:  ')
            pelicula= Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)

        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None

else:
    print('Salimos del Programa')