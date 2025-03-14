print('*** Diciconarios en Python ***')

#creamos un diccionario con clave y valor

persona = {
    'nombre': 'Said',
    'edad': 35,
    'ciudad': 'La Banda'
}

print(f'Diccionario de Persona: {persona}')

#accedemos a los elementos
print(f'\nNombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')

#modificar un valor
persona['edad'] = 40
print(f'\nDiccionario de Persona: {persona}')

#agregar un elemento
persona['profesion'] = 'Profesor'
print(f'\nDiccionario de Persona: {persona}')

#eliminar un elemento
del persona['ciudad']
print(f'\nDiccionario de Persona: {persona}')

#otra forma de eliminar
persona.pop('profesion')
print(f'\nDiccionario de Persona: {persona}')

#iterar los elementos de un dicc (llave,valor)
for llave,valor in persona.items(): #usamos el desempaque para asociar el diccionario a la llave y valor
    print(f'Llave: {llave} \t Valor: {valor}')

#obtener solo los valores
print(f'\nDiccionario de Persona: {persona}')
for valor in persona.values():
    print(f' - Valor: {valor}')

#obtener solo las llaves
print(f'\nDiccionario de Persona: {persona}')
for llave in persona.keys():
    print(f' - Llave: {llave}')