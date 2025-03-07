print(' *** Sistema de Envíos ***')

#Definimos la tarifa de envio por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

#solicitamos los valores de destino y peso al usuario
destino = input('Ingresa el destino del paquete (nacional / internacional): \n')
peso = float(input('Ingresa el peso del paquete (en kg): \n'))

#calculamos el envio del paquete
costo_envio = None
destino = destino.strip().lower()

if destino == 'nacional':
    costo_envio= peso*TARIFA_NACIONAL
elif destino == 'internacional':
    costo_envio = peso*TARIFA_INTERNACIONAL
else:
    print('Destino NO Válido.\n Ingresa el valor de Nacional o Internacional')

#mostramos costo de envio solo si es valido

if costo_envio is not None:
    print(f'El costo de envio del paquete es: ${costo_envio:.2f}')