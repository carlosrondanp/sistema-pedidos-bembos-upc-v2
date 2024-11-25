from entidades.pedido import Pedido
from controladores.base_datos_pedidos import BaseDatosPedidos

class SistemaPedidos:
    def __init__(self):
        self.base_datos = BaseDatosPedidos()

    def agregar_pedido(self, codigo, producto, cantidad, precio, fecha, hora, tiempo_preparacion):
        pedido = Pedido(codigo, producto, cantidad, precio, fecha, hora, tiempo_preparacion)
        self.base_datos.guardar_pedido(pedido)

    def obtener_registro_completo(self):
        return self.base_datos.obtener_pedidos()

    def limpiar_registro(self):
        self.base_datos.limpiar_registro()

    def analisis_estadistico(self):
        return self.base_datos.analizar_pedidos()

    def generar_reporte(self):
        self.base_datos.generar_reporte()
