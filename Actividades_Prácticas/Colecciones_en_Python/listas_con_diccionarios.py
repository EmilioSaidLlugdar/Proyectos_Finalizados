print('*** Listas con Diccionarios ***')

personas = [
    {
        'nombre': 'Emilio',
        'apellido': 'Llugdar',
        'edad': 35
    },
    {
        'nombre': 'Said',
        'apellido': 'Ruiz',
        'edad': 25
    }
]

print(personas)

#acceder a un diccionario desde una lista
print(f'''\n\tDetalles del Primer elemento de una Lista:
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

#recorrer elementos de una lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')