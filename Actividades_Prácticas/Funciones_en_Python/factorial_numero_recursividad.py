print('+++++ Calcular el factoria de un numero\n de forma recursiva +++++')

def factorial_recursiva(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: #caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

num = 4
resultado = factorial_recursiva(num)
print(f'\n\tEl factorial de {num} es: {resultado}')
