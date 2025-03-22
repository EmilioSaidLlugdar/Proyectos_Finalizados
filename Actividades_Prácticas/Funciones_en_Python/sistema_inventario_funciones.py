print('------ Sistema de Inventarios con Funciones -----')

#inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 35.99,'cantidad': 64},
    {'id': 2, 'nombre': 'Pantalon', 'precio': 5.99,'cantidad': 6},
    {'id': 3, 'nombre': 'Short', 'precio': 3.99,'cantidad': 8}
]

#funcion para mostrar el inventario
def mostrar_inventario():
    print('---- Inventario del Almacen ----')
    for producto in inventario:
        print(f'\n\tId:{producto.get('id')},\n\tNombre: {producto.get('nombre')},'
              f'\n\tPrecio: {producto.get('precio')},\n\tCantidad: {producto.get('cantidad')}')

def agregar_producto():
    #pass #operacion nula
    print('\n\t**** Agregar Nuevo Producto ****')
    id= int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id':id, 'nombre':nombre, 'precio': precio, 'cantidad': cantidad}

    inventario.append(nuevo_producto) #agregamos un nuevo producto al diccionario ya existente
    print('\t\t Producto agregado al inventario con Éxito!')

def buscar_producto_id():
    #pass #operacion nula
    print('//// Buscar producto por Id /////')
    id_buscar = int(input('Ingrese un Id: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformación del producto encontrado:')
            print(f'\n\tId: {producto.get('id')},\n\tNombre: {producto.get('nombre')}, '
                  f'\n\tPrecio: {producto.get('precio')},'
                  f'\n\tCantidad: {producto.get('cantidad')}')
            return
    print('\n Producto no Econtrado')




#main
if __name__ == '__main__':
    while True:
        print(f'''\n\t Menú
        1. Mostrar Inventario
        2. Agregar nuevo Producto
        3. Buscar producto por Id
        4. Salir''')

        opcion = int(input('Ingrese una opcion (1 - 4): '))

        #revisamos las opciones del menú
        if opcion == 1: #mostrar inventario
            mostrar_inventario()
        elif opcion == 2: #agregar nuevo prod
            agregar_producto()
        elif opcion == 3: #buscar un prod por id
            buscar_producto_id()
        elif opcion == 4: # salir
            print('Hasta luego')
            break
        else:
            print('opcion invalida...Ingrese otra opcion: ')
