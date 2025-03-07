#Generador de emails
print("*** Generador de Emails ***")

#Nombre Completo de Usuario
nombre_completo = ' Emilio Said Llugdar '
print(f'Nombre de usuario: {nombre_completo}')

#procesar o normalizar el nombre del usuario
#Limpiamos los espacios en blanco al inicio y al final con strip()
nombre_normalizado = nombre_completo.strip()

#Reemplazar los espacios en blanco por puntos con replace()
nombre_normalizado = nombre_normalizado.replace(' ', '.')

#Convertimos a minusculas con lower()
nombre_normalizado = nombre_normalizado.lower()

print(f'Nombre usuario Normalizado: {nombre_normalizado}')

#Datos de la Empresa
nombre_empresa = 'Said Producciones'
print(f'\nNombre de la Empresa: {nombre_empresa}')
extension_dominio = '.com.ar'
print(f'Extension del dominio: {extension_dominio}')

#Quitamos espacios en blanco y converimos a minuscula
nombre_empresa_normalizado = nombre_empresa.replace(' ','').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del Email Normalizado: {dominio_email_normalizado}')

#Creamos el email Final
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail Final generado: {email}')

