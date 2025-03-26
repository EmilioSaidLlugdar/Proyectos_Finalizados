print('+++ Sistema de máquina de Snacks +++')

#Definimos la lista de snaks inicial
snacks=[
    {'id':1, 'nombre': 'Papas', 'precio': 30},
    {'id':2, 'nombre': 'Gaseosa', 'precio': 50},
    {'id':3, 'nombre': 'Sandwich', 'precio': 120}
]

#Lista de producto (vacia). Son los snacks ya comprados

productos= []

def mostrar_snacks():
    print('---  Snacks Disponibles ---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get('nombre')} '
              f'- ${snack.get('precio')}')

 #--------------buscar un snack
def buscar_snack_id(id_snack):
    for snack in snacks:
        if snack.get('id') == id_snack:
            return snack
    #si no se encuentra el id, retorna None
    return None


def comprar_snacks():
    print('---  Comprar Snacks ---')
    id_snack = int(input('Qué snack quieres comprar (id)??: '))
    snack_encontrado = buscar_snack_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack no Encontrado: {id_snack}')


def mostrar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.get('nombre')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

#programa principal
if __name__ == '__main__':
    #creamos el menu
    while True:
        print('''\n\tMenú:
        1. Mostrar Snacks
        2. Comrpar Snacks
        3. Mostrar Ticket
        4. Salir''')

        opcion = int(input('\nIngresa una Opcion: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('\n\tRegresa Pronto!!!')
            break
        else:
            print('Opcion invalida.\nIngresa otra Opcion: ')
