class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self): #generamos la cadena que tendra info de los objetos
        return (f'Id: {self.id}, Nombre: {self.nombre},'
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')
