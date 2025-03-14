print('*** Agenda de Contactos ***')

agenda={
    'Emilio':{
        'Telefono': '123456',
        'email': 'emilio@gmail.com',
        'Direccion': 'Av. Siempre Viva'
    },
    'Said':{
        'Telefono': '789101112',
        'email': 'said@gmail.com',
        'Direccion': 'Av. chejolao'
    },
    'peter':{
        'Telefono': '13141516',
        'email': 'peter@gmail.com',
        'Direccion': 'mama antula'
    }
}

print(agenda)

#acceder a la info de un contacto
print(f'''\n\tInformacion de said
    Telefono: {agenda['Said']['Telefono']}
    email: {agenda['Said']['email']}
    Direccion: {agenda.get('Said').get('Direccion')}''')

#agregar un nuevo contacto
agenda['Fabio']={
    'Telefono': '111144444',
    'email': 'fabio@gmail.com',
    'Direccion': 'procrear'
}

print(f'\nAgenda Actualizada: {agenda}')

#eliminar un elemento
agenda.pop('Said')
print(f'\nAgenda Actualizada: {agenda}')


#mostramos contactos
for nombre, detalles in agenda.items():
    print(f''' Nombre: {nombre}
    Telefono: {detalles.get('Telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('Direccion')}
    ''')