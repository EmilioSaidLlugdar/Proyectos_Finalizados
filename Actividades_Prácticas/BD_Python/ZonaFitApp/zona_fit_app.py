from cliente import Cliente
from cliente_dao import ClienteDAO

print('*** Clientes de Zona Fit (GyM) ***')
opcion = None
while opcion != 5:
    print('''\tMenú:
    \t 1. Lista Clientes
    \t 2. Agregar Clientes
    \t 3. Modificar Clientes
    \t 4. Eliminar Clientes
    \t 5. Salir
    ''')
    opcion = int(input('Escribe tu opcion (1 - 5): '))
    if opcion == 1: #seleccionar listado de clientes
        clientes = ClienteDAO.seleccionar()
        print('\n *** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
        print('\n')

    elif opcion ==2:  #ingresar un cliente
        nombre_var = input('Escribe el nombre del Nuevo Cliente: ')
        apellido_var = input('Escribe el apellido del Nuevo Cliente: ')
        membresia_var = int(input('Escribe la membresia del Nuevo Cliente: '))
        cliente = Cliente(nombre = nombre_var, apellido = apellido_var, membresia= membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados} \n')

    elif opcion == 3: #modficar un cliente
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = int(input('Escribe la membresia: '))
        cliente = Cliente(id_cliente_var, nombre_var,apellido_var,membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Clientes Actualizados: {clientes_actualizados} \n')

    elif opcion ==4: #eliminar un cliente
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: ' ))
        cliente= Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes Eliminados: {clientes_eliminados} \n')

else:
    print('Saliste de la Aplicación...')