class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.sesion_activa = False

    def autenticar(self, contrasena):
        return self.contrasena == contrasena

    def iniciar_sesion(self):
        self.sesion_activa = True

    def cerrar_sesion(self):
        self.sesion_activa = False
