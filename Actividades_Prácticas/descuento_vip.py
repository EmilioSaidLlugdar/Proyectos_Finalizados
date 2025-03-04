print('*** Sistema de Descuentos VIP ***')

no_prod_descuento=10
cant_prod = int(input('Cuantos productos compraste hoy? '))
tiene_membresia = input(' Tienes la membresia de la Tienda (Si / No) ? ')

es_elegible_desc = (cant_prod >= no_prod_descuento
                    and tiene_membresia.strip().lower() == 'si')

print(f'Tienes acceso al descuento VIP? {es_elegible_desc}')