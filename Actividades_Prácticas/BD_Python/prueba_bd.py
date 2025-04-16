import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'

            # llaves_primarias = ((1,2,3),)
            # id_persona = input('Ingrese un id_persona:  ')
            #pedimos al usuario que ingrese info y lo tomamos como tupla

            entrada = input('Proporciona los if \'s a buscar (separado por comas):  ')
            llaves_primarias = (tuple(entrada.split(',')),) #convertimos lo ingresado a tupla y eliminamos las comas con split --> convertimos en una tupla de tuplas
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()