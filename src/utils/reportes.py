import pandas as pd
import matplotlib.pyplot as plt

def generar_graficos():
    df = pd.read_excel("data/pedidos.xlsx")

    # Barras
    df.groupby("Producto")["Cantidad"].sum().plot(kind="bar")
    plt.title("Cantidad de productos vendidos") 
    plt.xlabel("Producto") 
    plt.ylabel("Cantidad") 
    plt.show()

    # Pastel
    df.groupby("Producto")["Cantidad"].sum().plot(kind="pie", autopct='%1.1f%%')
    plt.title("Distribución de productos vendidos")
    plt.show()
