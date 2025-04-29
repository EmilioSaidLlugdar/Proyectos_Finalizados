from logger_base import log
# import psycopg2 as bd
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE ='test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    # Crearemos una clase mas para un pool de conexiones
    # _conexion = None
    # _cursor = None


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool EXITOSA: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrió un ERROR al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def obtenerConexion(cls):  #obtener conexion a partir de un pool de conexiones
         conexion = cls.obtenerPool().getconn()
         log.debug(f'Conexión obtenida del pool: {conexion}')
         return conexion

    @classmethod
    def liberarConexion(cls,conexion): #liberamos el objeto luego de usar para estar disponible
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() #cerramos todos los objetos de conexion disponibles


        # @classmethod
        #     def obtenerConexion(cls):
        #       if cls._conexion is None:
        #     try:
        #         cls._conexion = bd.connect(host= cls._HOST,
        #                                    user= cls._USERNAME,
        #                                    password = cls._PASSWORD,
        #                                    port= cls._DB_PORT,
        #                                    database = cls._DATABASE)
        #         log.debug(f'Conexión EXITOSA: {cls._conexion}')
        #         return cls._conexion #devolvemos un obj conexion que se creó correctamente
        #     except Exception as e:
        #         log.debug(f'Ocurrió una excepción al obtener la conexión {e}')
        #         sys.exit()
        # else:
        #     return cls._conexion


    # @classmethod
    # def obtenerCursor(cls):
    #     #se obtiene una conexion en caso que no exista
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
    #             return cls._cursor
    #         except Exception as e:
    #             log.error(f'Ocurrió una Excepcion al obtener el cursor: {e}')
    #             sys.exit()
    #     else:
    #         return cls._cursor

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()

