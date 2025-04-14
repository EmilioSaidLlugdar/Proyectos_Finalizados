from NumerosIdenticosException import NumeroIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumeroIdenticosException('Numeros Identicos') #raise sirve para arrojar cualquier tipo de error
    resultado = a/b #no se puede resolver, entonces queda con su asignacion original


except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error:\n {e} , {type(e)}')

except TypeError as e:
    print(f'TypeError - Ocurrió un error:\n {e} , {type(e)}')

except Exception as e:
    print(f'Exception - Ocurrió un error:\n {e} , {type(e)}')
else:
    print('----------No se arrojó ninguna excepcion')
finally:
    print('////    Ejecucion del bloque finally')
print(f'Resultado: {resultado}')
print('Continuamos...')