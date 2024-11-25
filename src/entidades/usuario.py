class Usuario:
    def __init__(self, nombre, contrasena, rol):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol

    def autenticar(self, contrasena):
        return self.contrasena == contrasena