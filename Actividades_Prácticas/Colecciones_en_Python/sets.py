print('*** Manejo de Set o Conjuntos *** ')

#creamos un conjunto

mi_set={1,2,3,4,5,4} #no tiene orden ni indices

print(f'Mi set: {mi_set}')


#agregamos elementos al set
mi_set.add(6)
mi_set.add(7)

print(f'\n Mi set modificado: {mi_set}')

#eliminar un elemento
mi_set.remove(4)

print(f'\n Mi set modificado: {mi_set}')

#iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')

#comprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set? {4 in mi_set}')
print(f'\nExiste el valor de 1 en el set? {1 in mi_set}')

#obtener la longitud del set
print(f'\n Longitud del conjunto: {len(mi_set)}')

print('-------- OPERACIONES MATEMATICAS CON SET -------------')

a = {1,2,3,4}
b = {3,4,5,6}

print(f'a = {a}')
print(f'b = {b}')
union = a|b
print(f'Union a | b : {union}')

interseccion = a & b
print(f'Intersección a & b : {interseccion}')

diferencia = a - b
print(f'Diferencia a - b: {diferencia}')