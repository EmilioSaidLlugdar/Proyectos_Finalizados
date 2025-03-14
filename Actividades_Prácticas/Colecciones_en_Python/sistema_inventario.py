print('*** Sistema de Inventario ***')

inventario = []

nro_productos=int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(nro_productos):
    print(f'Proporciona los valores del Producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    #creamos el diccionar con el detalle del producto
    producto = {'id': indice, 'nombre':nombre, 'precio':precio, 'cantidad': cantidad}
    #agregamos el nuevo producto al inventario
    inventario.append(producto)

#mostramos el inventario inicial
print(f'\n Inventario inicial: {inventario}')

#buscar un producto por id
id_buscar = int(input('\nIngresa el ID a buscar: '))
prod_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        prod_encontrado=producto
        break

if prod_encontrado is not None:
    print('\n\tInformacion del Producto encontrado:')
    print(f'''Id: {prod_encontrado.get('id')}
    Nombre: {prod_encontrado.get('nombre')}
    Precio: {prod_encontrado.get('precio')}
    Cantidad: {prod_encontrado.get('cantidad')}
    ''')
else:
    print(f'Producto con id {id_buscar} No encontrado')

#Mostramos el inventario detallado
print(f'\n\t--- Inventario Detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
        Nombre: {producto.get('nombre')}
        Precio: {producto.get('precio')}
        Cantidad: {producto.get('cantidad')}
        ''')