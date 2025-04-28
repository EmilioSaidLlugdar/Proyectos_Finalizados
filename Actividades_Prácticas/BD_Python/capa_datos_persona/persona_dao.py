from conexion import Conexion
from persona import Persona
from logger_base import log
class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:#para obtener una conexion, por eso llamamos obtenerCursor directamente
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall() #para recuperar todos los registros
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3]) #id,nombre,apellido,email
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug((f'Persona Actualizada: {persona}'))
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Objeto Eliminado: {persona}')
                return cursor.rowcount


if __name__ == '__main__':
    # #Insertar un registro
    # persona1 = Persona(nombre='Renata', apellido='Llugdar', email='rllugdar@mail.com')
    # personas_insertadas= PersonaDAO.insertar(persona1)
    # log.debug(f'Personas Insertadas: {personas_insertadas}')

    #actualizar un registro
    # persona1= Persona(3,'emilio','llugdar', 'ellugdar@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas Actualizadas: {personas_actualizadas}')

    #eliminar un registro
    persona1 = Persona(id_persona=20)
    persona_eliminada = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas Eliminadas: {persona_eliminada}')


    #seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)