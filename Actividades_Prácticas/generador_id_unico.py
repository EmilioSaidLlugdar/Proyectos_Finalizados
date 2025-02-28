from random import randint

print('*** Sistema Generador de ID único ***')

nombre = input('Cual es tu nombre?: ')
apellido = input('Cual es tu apellido? ')
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY) ?')

#normalizamos los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:]

#Generamos valor aleatorio

aleatorio = randint(1000,9999)

#Generado de ID único
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
    Tu nuevo número de identificación ID generado por el sistema es:
    {id_unico}
    FELCIDADES!!''')
