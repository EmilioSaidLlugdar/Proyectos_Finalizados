import  os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod #puede acceder a los atributos de clase
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo, 'a', encoding= 'utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de Películas'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado: {cls.ruta_archivo}')