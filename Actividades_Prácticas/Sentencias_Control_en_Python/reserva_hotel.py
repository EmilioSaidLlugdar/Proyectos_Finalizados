print(' *** Sistema de Reserva Hotel ***')

#variables

tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

#pedimos la info al usuario
nombre_cliente = input('Nombre del Cliente: ')
dias_estadia = int(input('Días de estadía: '))
vista_al_mar_txt = input('Con vista al mar (Si / No)? ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

#calulamos el costo total de la estancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

#msotramos los detalles de la reserva
print('\n---------  DETALLES DE LA RESERVACIÓN ---------')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de  estadia: {dias_estadia}')
print(f'Costo Total: ${costo_total:.2f}')
print(f'Habitacion con vista al mar: {'Si' if vista_al_mar else 'No'}')
print(f'**** GRACIAS *****')

