print('----- Imprimir detalles de una persona, usando kwargs ------')

#funcion que acepta argumentos variables en forma de llave - valor dict

def imprimir_detalle_persona (**kwargs):
    print('\n Valores Recibidos: ')
    for llave,valor in kwargs.items():
        print(f'\t{llave}: {valor}')

imprimir_detalle_persona(nombre='Said', edad= 34, ciudad= 'La Banda')
imprimir_detalle_persona(nombre= 'Peter', edad= 25, ciudad='La Banda', Trabajo = 'Refugio' )
imprimir_detalle_persona(nombre= 'Fabio', edad= 40)