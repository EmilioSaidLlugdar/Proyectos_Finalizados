print('*** Calculadora Simple ***')
operando1= operando2=resultado=0
salir = False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')

    op = int(input('\nIngresa una Opcion: '))
    if 1<= op <= 4:
        operando1 = float(input('Ingresa el valor 1: \n'))
        operando2 = float(input('Ingresa el valor 2: \n'))

    if op == 1: #SUMA
        resultado= operando1 + operando2
        print(f'El resultado de la SUMA es: {resultado:.2f}\n')

    elif op==2: #RESTA
        resultado = operando1 - operando2
        print(f'El resultado de la RESTA es: {resultado:.2f}\n')
    elif op == 3: #MULTIPLICACION
        resultado = operando1 * operando2
        print(f'El resultado de la MULTIPLICACION es: {resultado:.2f}\n')

    elif op == 4: #DIVISION
        resultado = operando1 / operando2
        print(f'El resultado de la DIVISION es: {resultado:.2f}\n')

    elif op == 5: #SALIR
        print('Gracias por usar mi Calculadora! :)')
        salir=True

    else:
        print('Opcion Inválida')