import pandas as pd
import matplotlib.pyplot as plt

def generar_analisis_estadistico(archivo_excel="data/pedidos.xlsx"):
    try:
        df = pd.read_excel(archivo_excel)
        if df.empty:
            print("No hay datos disponibles para el análisis.")
            return

        total_pedidos = len(df)
        total_ingresos = df["Precio"].sum()
        producto_mas_vendido = df["Producto"].value_counts().idxmax()

        print("Análisis Estadístico:")
        print(f"- Total de Pedidos: {total_pedidos}")
        print(f"- Total de Ingresos: S/ {total_ingresos:.2f}")
        print(f"- Producto Más Vendido: {producto_mas_vendido}")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo_excel}")
    except ValueError as e:
        print(f"Error en los datos: {e}")

def generar_grafico_barras(archivo_excel="data/pedidos.xlsx"):
    try:
        df = pd.read_excel(archivo_excel)
        if df.empty:
            print("No hay datos disponibles para generar gráficos.")
            return

        df.groupby("Producto")["Cantidad"].sum().plot(kind="bar", title="Cantidad de Productos Vendidos")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad Vendida")
        plt.xticks(rotation=45)
        plt.show()

    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo_excel}")
    except ValueError as e:
        print(f"Error en los datos: {e}")
