import pandas as pd

def obtener_estadisticas():
    df = pd.read_excel("data/pedidos.xlsx")
    estadisticas = df.groupby("Producto")["Cantidad"].sum()
    return estadisticas
