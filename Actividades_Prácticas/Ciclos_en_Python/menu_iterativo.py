print('*** SISTEMA DE ADMINISTRACION DE CUENTAS ***')

salir = False
while not salir:
    print(f'''MENU:
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir''')

    op= int(input('Escoje una opcion: \n'))
    if op == 1:
        print('Creando tu Cuenta...\n')
    elif op == 2:
        print('Eliminando tu Cuenta...\n')
    elif op== 3:
        print('Saliendo del Sistema. Hasta pronto...\n')
        salir = True
    else:
        print('Opción inválida. Ingrese nuevamente')
else:
    print('*** TERMINANDO SISTEMA DE ADMINISTRACION DE CUENTAS ***')