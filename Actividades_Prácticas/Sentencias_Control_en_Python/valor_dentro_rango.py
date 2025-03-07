print('*** Valor dentro de un Rango ***')

minimo = 0
maximo = 5

#solicitamos un valor
dato = int(input(f'Ingresa un dato entre {minimo} y {maximo}:\n'))

#verificamos
esta_dentro_tango = minimo <= dato <= maximo
print(f'Valor está dentro del rango? {esta_dentro_tango}')