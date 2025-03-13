print('*** promedio_calificaciones ***')

total_calificaciones = int(input('Ingresa el numero de calificaciones a evaluar: '))
calificaciones = []

#iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'calificacion[{indice}]= '))
    calificaciones.append(calificacion)

#imprimimos las calificaciones
print(f'\n Las calificaciones proporcionadas son: {calificaciones}')

#calulamos el promedio de las calificaciones
#sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio= suma_calificaciones/total_calificaciones
print(f'\nPromedio de las Calificaciones: {promedio}')