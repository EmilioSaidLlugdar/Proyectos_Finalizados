print(' *** Lista de Suscriptores ***')

#definimos el set inicial
#suscriptores= {} #diccionario vacio
suscriptores = set() #definimos un set vacio

#pedimos al usuario ingresar datos de manera dinamica
numero_suscriptores = int(input('Proporciona el número de suscriptores inciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores incial: {suscriptores}')

#verificar si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Ingresa un nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'\nEl nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'\nEl nuevo suscriptor se ha agregado a la lista: {nuevo_suscriptor}')
print(f'\nLista de suscriptores actualizada: {suscriptores}')

#Eliminamos un suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'\nEl suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'\nLista de suscriptores actualizada: {suscriptores}')

#Verificamos la cantidad total de suscriptores
print(f'\n\tCantidad total de suscriptores: {len(suscriptores)}')

#Mostramos todos los suscriptores
print(f'\n\t------ lista de Suscriptores --------')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')
