print('*** Bienvenidos a la casa de los Espejos ***')

edad = int(input('Cuál es tu edad? '))
tiene_miedo_oscuridad = input('Tienes miedo a la oscuridad (Si / No)')
tiene_miedo_oscuridad = tiene_miedo_oscuridad.strip().lower() == 'si'

if not tiene_miedo_oscuridad and edad>= 10:
    print('Puedes entrar a la Casa de los Espejos')
else:
    print(' Lo siento, la casa de los espejos puede darte miedo')