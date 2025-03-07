print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio Leche: '))
precio_pan = float(input('Precio Pan: '))
precio_lechuga = float(input('Preico Lechuga: '))
precio_platano = float(input('Prcio Plátano'))
desc_porcentaje = int(input('Aplicar algún descuento (%)? '))

# calcula del subtotal sin impuestos
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

#Aplicar el descuento
descuento = subtotal * (desc_porcentaje/100)

#subtotal con descuentos
subtotal_con_desc = subtotal - descuento

# calcula con impuestos (21%)
impuestos = subtotal_con_desc * 0.21

#calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_desc + impuestos
print(f'''
subtotal: ${subtotal:.2f}
Descuento Ingresado por usuario: ${descuento} ({desc_porcentaje}%)
Subtotal con Descuentos: ${subtotal_con_desc}
Impuestos: (21%): ${impuestos:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')