import psycopg2 as bd

conexion = bd.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db')

try:
    #con with el commit se realiza automaticamente
    #sin necesidad de abrir ni cerrar
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s,%s)'
            valores = ('Jose', 'Molina', 'jmolina@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
            valores = ('Peter', 'Sanchez', 'psanchez@mail.com', 3)
            cursor.execute(sentencia,valores)

except Exception as e:
    print(f'Ocurrió un error se hizo rollback de la transaccion {e}')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit')