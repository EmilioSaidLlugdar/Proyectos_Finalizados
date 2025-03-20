print('---- Funcion con argumentos por nombre ----')

def imprimir_persona(nombre='',apellido='', edad=0):
    print(f'\nPersona: nombre: {nombre}, apellido: {apellido}, edad: {edad}')

#primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Emilio', 'Said', 34)

#llamar a la funcion usando argumentos por nombre
imprimir_persona(nombre='peter',apellido='Sanchez', edad=25)

#llamar a la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=45,apellido='Llugdar', nombre='Jorge')

#argumentos con valo por default
imprimir_persona(nombre='lady')
imprimir_persona(nombre='lady', apellido='Ruiz')