print('*** Salud y Fitness *** ')

#constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 #valor aproximado, son kilocalorias

#pedimos los valores al usuario
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

#verificar si el usuario alcanzó la meta de pasos diarios

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'
#calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

#mostramos la info
print(f'\n Usuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'meta de pasos diarios alcanzados: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')
