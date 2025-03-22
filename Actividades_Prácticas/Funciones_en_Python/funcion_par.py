print('++++ FUNCION PAR +++++')

def es_par(num):
    if num % 2 == 0:
        return  True
    else:
        return False

if __name__ == '__main__':
    numero= int(input('Ingrese un numero: '))
    print(f'\n\tEl numero es PAR? {es_par(numero)}')