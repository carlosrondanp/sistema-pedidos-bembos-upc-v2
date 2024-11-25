import pandas as pd
import os

class BaseDatosPedidos:
    def __init__(self, archivo_excel="data/pedidos.xlsx", archivo_csv="data/pedidos.csv"):
        self.archivo_excel = archivo_excel
        self.archivo_csv = archivo_csv
        self.verificar_archivos()

    def verificar_archivos(self):
        columnas = ['Codigo', 'Producto', 'Cantidad', 'Precio', 'Fecha', 'Hora', 'TiempoEntrega']
        if not os.path.isfile(self.archivo_excel):
            pd.DataFrame(columns=columnas).to_excel(self.archivo_excel, index=False)
        if not os.path.isfile(self.archivo_csv):
            pd.DataFrame(columns=columnas).to_csv(self.archivo_csv, index=False)

    def guardar_pedido(self, pedido):
        nuevo_registro = pd.DataFrame([{
            "Codigo": pedido.codigo,
            "Producto": pedido.producto,
            "Cantidad": pedido.cantidad,
            "Precio": pedido.precio,
            "Fecha": pedido.fecha,
            "Hora": pedido.hora,
            "TiempoEntrega": pedido.tiempo_entrega
        }])
        # Guardar en CSV
        nuevo_registro.to_csv(self.archivo_csv, mode='a', header=not os.path.isfile(self.archivo_csv), index=False)
        # Guardar en Excel
        df_actual = pd.read_excel(self.archivo_excel)
        df_actual = pd.concat([df_actual, nuevo_registro], ignore_index=True)
        df_actual.to_excel(self.archivo_excel, index=False)

    def cargar_pedidos(self):
        try:
            return pd.read_excel(self.archivo_excel)
        except FileNotFoundError:
            return pd.DataFrame()


    def limpiar_registro(self):
        columnas = ['Codigo', 'Producto', 'Cantidad', 'Precio', 'Fecha', 'Hora', 'TiempoEntrega']
        pd.DataFrame(columns=columnas).to_excel(self.archivo_excel, index=False)
        pd.DataFrame(columns=columnas).to_csv(self.archivo_csv, index=False)

