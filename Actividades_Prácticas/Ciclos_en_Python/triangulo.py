print('***Dibujar Triangulo Simetrico ***')

nro_filas = int(input('Proporciona el numero de filas: '))

#iterar sobre cada fila del triangulo

for fila in range(1, nro_filas + 1):
    espacios_blancos = ' '* (nro_filas - fila)
    asterisco = '*' * (2 * fila -1)
    print(f'{espacios_blancos}{asterisco}')