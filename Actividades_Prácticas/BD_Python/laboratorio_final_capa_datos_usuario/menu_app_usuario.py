from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('\tOPCIONES:')
    print('\t 1. Listar Usuarios')
    print('\t 2. Agregar Usuario')
    print('\t 3. Modificar Usuario')
    print('\t 4. Eliminar Usuario')
    print('\t 5. SALIR')

    opcion = int(input('\tEscribe tu opcion (1 - 5):  \n'))
    if opcion == 1 :
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var,password=password_var )
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info((f'Usuarios Insertados: {usuarios_insertados}'))
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var=input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        usuario_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'usuarios actualizados: {usuario_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario= id_usuario_var)
        usuario_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'usuarios eliminados: {usuario_eliminados}')
else:
    log.info('Salimos de la Aplicacion...')