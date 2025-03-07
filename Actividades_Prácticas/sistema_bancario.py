print('*** BIENVENIDOS AL SISTEMA BANCARIO *** ')

#usamos logica inversa

salir_sistema_txt = input('Desea salir del sistema (Si / No) ?')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')