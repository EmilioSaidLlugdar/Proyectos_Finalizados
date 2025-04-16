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
            # sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s,%s)'
            # # valores= ('Carlos', 'Lara', 'clara@mail.com') #para insertar un solo registro
            #
            # #insertar varios registros a la vez
            # valores = (
            #     ('Luz', 'Acuña', 'lacuna@mail.com'),
            #     ('Maxi', 'Fernando', 'mfernando@mail.com'),
            #     ('Romina', 'Santillan', 'rsantillan@mail.com'),
            # )

            #--------- para actualizar
            # sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona = %s'
            # # --------- para actualizar varios registros
            # valores= (
            #     ('Aiza', 'Fiad', 'afiad@mail.com', 4),
            #     ('Lourdes', 'Banegas', 'lbanegas@mail.com', 5)
            # )

            #----------- PARA ELIMINAR
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            # valores = (6,)
            #ahora lo hacemos dinamico
            entrada = input('Proporciona los id persona a eliminar:  ')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount #regresa registros modificados
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()