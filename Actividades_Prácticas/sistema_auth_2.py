print(' *** Sistema de Auenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '1234'

usuario = input('ingresa tu usuario: \n')
password = input('Ingresa tu password: \n')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema')
elif usuario == USUARIO_VALIDO:
    print('Password Incorrecto')
elif password == PASSWORD_VALIDO:
    print('Usuario Incorrecto')
else:
    print('Usuario y Passwor Incorrecto')