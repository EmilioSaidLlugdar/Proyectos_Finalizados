print('*** Aplicacion Cajero Automático ***')

saldo = 1000
salir = False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')

    op = int(input('\nIngresa una Opcion: '))
    if op==1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif op == 2:
        retiro = float(input('Ingresar el monto a retirar: '))
        #validacion
        if retiro <= saldo:
            saldo -= retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'NO cuentas con el saldo suficiente. Saldo actual es: ${saldo:.2f}')
    elif op == 3:
        deposito = float(input('Ingresa el monto a depositar:\n'))
        saldo += deposito
        print(f'Tu nuevo saldo es: ${saldo:.2f}')
    elif op == 4:
        print(f'Gracias por usar nuestro sistema.')
        salir = True
    else:
        print('opcion invalida. Selecciona otra opcion')

else:
    print('Hasta pronto')