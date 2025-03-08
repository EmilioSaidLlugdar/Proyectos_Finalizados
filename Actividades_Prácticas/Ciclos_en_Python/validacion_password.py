print('*** Creacion y validacion de password ***')

password= input('''Ingresa un password
    debe tener al menos 6 caracteres: \n''')
while len(password) <6:
    print('El password no cumple con los requisitos.\n Debe tener al menos 6 caracteres')
    password=input('Ingrese nuevamente un password: ')

else:
    print('El valor del password es VALIDO!')