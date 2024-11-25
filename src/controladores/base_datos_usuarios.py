import pandas as pd
from src.entidades.usuario import Usuario

class BaseDatosUsuarios:
    def __init__(self, archivo="data/usuarios.csv"):
        self.archivo = archivo
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            df = pd.read_csv(self.archivo)
            return [Usuario(row["nombre"], row["contrasena"], row["rol"]) for _, row in df.iterrows()]
        except FileNotFoundError:
            return []

    def validar_usuario(self, nombre, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.autenticar(contrasena):
                return usuario
        return None
