#Generador de emails

print("*** Generador de Emails ***")
print('------ MEJORADO ---------')

#Nombre Completo de Usuario
nombre = input('Ingresar Nombre: ')
apellido = input('Ingresar Apellido:')
empresa = input('Ingresa nombre de tu empresa: ')
extension_dominio = input('Extension de Dominio de tu Empresa: ')

#Normalizamos Valores
nombre = nombre.strip().lower().replace(' ','.')
apellido = apellido.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','')
extension_dominio =extension_dominio.strip().lower().replace(' ','')

#Generamos el email

email = f'{nombre}.{apellido}@{empresa}{extension_dominio}'

print(f'''\n
Tu nuevo email Generado por el Sistema es:
        {email}
\nFELICIDADES!!!''')
