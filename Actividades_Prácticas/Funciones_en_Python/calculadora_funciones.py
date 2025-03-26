print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''\n\tMenú:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    return int(input('Ingresa una Opcion: '))

def pedir_valores():
    operando1 = float(input('Ingresa el valor 1: '))
    operando2 = float(input('Ingresa el valor 2: '))
    return operando1,operando2

def ejectutar_operacion(opcion,salir):
    #solicitar valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores() #se usa el unpaquing
    resultado = 0
    if opcion == 1:
        resultado = operando1 + operando2
        print(f'\nEl Resultado de la suma es: {resultado}')

    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'\nEl Resultado de la resta es: {resultado}')

    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'\nEl Resultado de la multiplicacion es: {resultado}')

    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'\nEl Resultado de la division es: {resultado}')

    elif opcion == 5:
        print('Saliendo del Programa Calculadora...')
        salir = True
    else:
        print('Opcion invalida.... Ingrese otra opcion')
    return salir



#programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejectutar_operacion(opcion, salir)