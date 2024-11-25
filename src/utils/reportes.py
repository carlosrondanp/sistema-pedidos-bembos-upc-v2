import pandas as pd

def generar_reporte(archivo_excel="data/pedidos.xlsx", archivo_reporte="data/reporte_pedidos.csv"):
    try:
        df = pd.read_excel(archivo_excel)
        if df.empty:
            print("No hay datos disponibles para generar el reporte.")
            return
        
        try:
            df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M:%S").dt.hour
        except Exception as e:
            print("Error al procesar la columna 'Hora': Asegúrate de que esté en formato 'HH:MM:SS'.")
            print(f"Detalles del error: {e}")
            return

        total_pedidos = len(df)
        total_ingresos = df["Precio"].sum()
        producto_mas_vendido = df["Producto"].value_counts().idxmax()
        cantidad_producto_mas_vendido = df["Producto"].value_counts().max()
        hora_pico = df["Hora"].mode()[0]

        resumen = {
            "Total de Pedidos": total_pedidos,
            "Total de Ingresos (S/)": total_ingresos,
            "Producto Más Vendido": producto_mas_vendido,
            "Cantidad del Producto Más Vendido": cantidad_producto_mas_vendido,
            "Hora Pico de Ventas": f"{hora_pico}:00"
        }

        pd.DataFrame([resumen]).to_csv(archivo_reporte, index=False)
        print(f"Reporte generado exitosamente en {archivo_reporte}")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo_excel}")
