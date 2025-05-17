#bool contiene los valores de T y F
#tipos numericos, Falso para 0, True demas valores
valor = 0
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = 15
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

#tipo str, False para '', True demas valores
valor = ''
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

#tipo colecciones, False para coleecion vacias, True demas colecciones
#lista vacia
valor = []
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
#lista no vacia
valor = [2,3,4]
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

#tupla
#tupla vacia
valor = ()
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
#tupla no vacia
valor = (2,3,4)
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')


#diccionario
#diccionario vacio
valor = {}
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
#diccionario no vacio
valor = {'nombre':'Said', 'apellido':'Llugdar'}
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

if bool(''):
    print('Regresó Verdadero')
else:
    print('Regresó Falso')

if '':
    print('Regresó Verdadero')
else:
    print('Regresó Falso')

while 0:
    print('Ejecución ciclo while')
else:
    print('Fin Ciclo While')
