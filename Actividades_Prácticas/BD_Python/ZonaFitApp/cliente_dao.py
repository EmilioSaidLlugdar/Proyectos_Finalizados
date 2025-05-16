from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #mapeo entre  clase y  tabla cliente
            clientes = []
            for registro in registros:
                                  #id           nombre       apellido     membresia
                cliente = Cliente(registro[0],registro[1], registro[2],registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al INSERTAR cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia,cliente.id)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores= (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al eliminar un Cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)




if __name__ == '__main__':
    # insertar un cliente
    # cliente1 = Cliente(nombre='Debora', apellido='Coronel', membresia=123)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes INSERTADOS: {clientes_insertados}')

    #actualizacion
    # cliente_actualizar = Cliente(6,'Marina', 'Bertelli', 2000)
    # cliente_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes Actualizados: {cliente_actualizados}')

    #eliminar cliente
    # cliente_eliminar = Cliente(id=4)
    # cliente_eliminado = ClienteDAO.eliminar(cliente_eliminar)
    # print(f'Clientes Eliminados: {cliente_eliminado}')

    # seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)


