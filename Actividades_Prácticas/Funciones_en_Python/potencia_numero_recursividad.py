print('+++++ Potencia de un numero de forma recursiva +++++')

def potencia(base, exponente):
    if exponente == 0: #caso base
        return 1
    else: #caso recursivo
        return base * potencia(base, exponente - 1)

base= int(input('Ingrese una base: '))
exponente = int(input('Ingrese un exponente: '))

print(f'La potencia de {base} elevado a {exponente} es: {potencia(base,exponente)}')