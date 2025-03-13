print(' *** Combinacion de Listas y Tuplas *** ')

#definir unas lista que almacena tuplas de productos

productos=[
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Remera', 40.00)
]

#Imprimir la informacion de cada produto y calculamos el precio total
precio_total=0

print('Informacion de los Productos: ')
for producto in productos:
    #usamos el desempaque para mostrar la info ordenada
    id, descripcion,precio = producto
    print(f'Producto: id= {id}, Descripcion = {descripcion}, Precio = ${precio}')
    precio_total += precio #o podemos acceder al indice 2 de la tupla
print(f'Precio total de los Productos: ${precio_total}')

