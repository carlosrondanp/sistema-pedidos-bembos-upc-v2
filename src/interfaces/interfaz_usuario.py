import tkinter as tk
from tkinter import ttk
from controladores.sistema_pedidos import SistemaPedidos

class InterfazUsuario:
    def __init__(self):
        self.sistema = SistemaPedidos()
        self.root = tk.Tk()
        self.root.title("Sistema de Pedidos")
        self._crear_interfaz()

    def _crear_interfaz(self):
        # Formulario de pedidos
        frame_formulario = tk.Frame(self.root)
        frame_formulario.pack(pady=10)

        tk.Label(frame_formulario, text="Código Pedido").grid(row=0, column=0)
        self.codigo_entry = tk.Entry(frame_formulario)
        self.codigo_entry.grid(row=0, column=1)

        tk.Label(frame_formulario, text="Producto").grid(row=1, column=0)
        self.producto_entry = tk.Entry(frame_formulario)
        self.producto_entry.grid(row=1, column=1)

        tk.Label(frame_formulario, text="Cantidad").grid(row=2, column=0)
        self.cantidad_entry = tk.Entry(frame_formulario)
        self.cantidad_entry.grid(row=2, column=1)

        # Botones de acción
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Pedido", command=self.agregar_pedido).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Limpiar Registro", command=self.limpiar_registro).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Ver Registro", command=self.ver_registro).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Análisis Estadístico", command=self.analisis_estadistico).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Generar Reporte", command=self.generar_reporte).pack(side=tk.LEFT, padx=5)

        # Tabla de pedidos
        columnas = ["Código", "Producto", "Cantidad", "Precio", "Fecha", "Hora", "TiempoPreparacion"]
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
        self.tabla.pack(pady=10)

    def agregar_pedido(self):
        codigo = self.codigo_entry.get()
        producto = self.producto_entry.get()
        cantidad = int(self.cantidad_entry.get())
        precio = 10.0 * cantidad  # Precio ejemplo
        fecha = "2024-11-24"
        hora = "14:00:00"
        tiempo_preparacion = 5 * cantidad

        self.sistema.agregar_pedido(codigo, producto, cantidad, precio, fecha, hora, tiempo_preparacion)
        self.ver_registro()

    def limpiar_registro(self):
        self.sistema.limpiar_registro()
        self.ver_registro()

    def ver_registro(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for pedido in self.sistema.obtener_registro_completo():
            self.tabla.insert("", tk.END, values=list(pedido.values()))

    def analisis_estadistico(self):
        estadisticas = self.sistema.analisis_estadistico()
        if estadisticas is not None:
            print(estadisticas)
        else:
            print("No hay datos para analizar.")

    def generar_reporte(self):
        self.sistema.generar_reporte()
        print("Reporte generado.")

    def ejecutar(self):
        self.root.mainloop()
