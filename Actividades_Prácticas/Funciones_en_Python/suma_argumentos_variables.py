print('----- Sumar con Argumentos Variables ------')

def sumar(*args):
    total = 0
    for num in args:
        total +=num
    return total

resultado = sumar (1,2,3,4,5,6,7,8,9,10)
print(f'Resultado de la suma es: {resultado}')