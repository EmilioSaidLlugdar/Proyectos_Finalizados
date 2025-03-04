print('*** Sistema de Autenticación ***')

usuario_valido = 'admin'
password_valido = '1234'

usuario_ingresado = input('Cual es tu usuario? ')
password_ingresado = input('Cual es tu password? ')

son_datos_correctos = (usuario_ingresado.strip() == usuario_valido and
                       password_ingresado.strip() == password_valido)

print(f'Datos son Correctos? {son_datos_correctos}')