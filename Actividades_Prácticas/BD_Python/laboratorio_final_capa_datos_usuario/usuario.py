class Usuario:
    def __init__(self, id_usuario=None, username= None, password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'Usuario: {self._id_usuario} {self._username} {self._password}'
#--------------- USUARIO GET/SET--------------
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario = id_usuario

# --------------- USERNAME GET/SET--------------
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

# --------------- PASSWORD GET/SET--------------
    @property
    def password(self):
        return self._password

    @password.setter #Se puede agregar validaciones (numeros. letras, matusculas)
    def password(self,password):
        self._password = password

