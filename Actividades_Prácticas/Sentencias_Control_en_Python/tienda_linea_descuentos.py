print('*** Sistema Tienda en Línea con Descuentos ***')

#Condiciones
monto_compra_desc = 1000

monto_compra = float(input('Cuál fué el monto de tu compra? '))
es_miembro = input(' Eres miembro de la Tienda (Si / No) ? ')

descuento = 0
#verificamos cada caso, con los datos proporcionados
if monto_compra >= monto_compra_desc and es_miembro.strip().lower() == 'si':
    descuento = 0.1 #10%
elif es_miembro.strip().lower() == 'si':
    descuento = .05 #5%
elif monto_compra >=monto_compra_desc:
    descuento = .03 # 3%
else:
    descuento = 0

#hacemos los calculos para obtener monto final

if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\n FELICIDADES, has obtenido un descuento del {descuento *100:.0f}%')
    print(f'Monto de la Compra: ${monto_compra:.2f}')
    print(f'Monto del Descuento: ${monto_descuento:.2f}')
    print(f'Monto Final de la compra con descuento: ${monto_final:.2f}')

else:
    print('\nNO obtubiste ningún descuento')
    print('\nTe invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: ${monto_compra:.2f}')

