import pandas as pd

class BaseDatosPedidos:
    def __init__(self, archivo="data/pedidos.xlsx"):
        self.archivo = archivo
        self.pedidos = self.cargar_pedidos()

    def cargar_pedidos(self):
        try:
            return pd.read_excel(self.archivo).to_dict(orient="records")
        except FileNotFoundError:
            return []

    def guardar_pedido(self, pedido):
        self.pedidos.append(pedido.__dict__)
        self._guardar_archivo()

    def obtener_pedidos(self):
        return self.pedidos

    def limpiar_registro(self):
        self.pedidos = []
        self._guardar_archivo()

    def _guardar_archivo(self):
        df = pd.DataFrame(self.pedidos)
        df.to_excel(self.archivo, index=False)

    def analizar_pedidos(self):
        df = pd.DataFrame(self.pedidos)
        if not df.empty:
            return df.groupby("producto")["cantidad"].sum()
        return None

    def generar_reporte(self):
        df = pd.DataFrame(self.pedidos)
        if not df.empty:
            df.to_csv("data/reporte_pedidos.csv", index=False)
