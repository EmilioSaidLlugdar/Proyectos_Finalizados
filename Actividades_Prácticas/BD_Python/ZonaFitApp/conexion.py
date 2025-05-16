try:
    import mysql.connector
    import mysql.connector.pooling as pooling
    from mysql.connector import Error
except ImportError as e:
    print(f"Error crítico al importar las librerías de MySQL: {e}")
    raise

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    #obtener el pool de conexiones
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea el obj pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                # print(f'Nombre del pool: {cls.pool.pool_name}')
                # print(f'Tamaño del pool: {cls.pool.pool_size}')
                return cls.pool #retornamos el objeto de pool

            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool #retornamos el objeto ya inicializado

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ =='__main__':
    #creacion del objeto pool
    # pool= Conexion.obtener_pool()
    # print(pool)

    #obtener un objeto conexion
    cnx1 = Conexion.obtener_conexion() #listo para conectarlo a DB
    print(cnx1)
    Conexion.liberar_conexion(cnx1) #regresa al pool de conexiones