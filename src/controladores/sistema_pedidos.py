from entidades.pedido import Pedido
from controladores.base_datos_pedidos import BaseDatosPedidos
from datetime import datetime

class SistemaPedidos:
    def __init__(self):
        self.base_datos = BaseDatosPedidos()

    def agregar_pedido(self, codigo, producto, cantidad, precio_kg):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        precio = precio_kg * cantidad
        tiempo_entrega = 1 * cantidad

        nuevo_pedido = Pedido(codigo, producto, cantidad, precio, fecha, hora, tiempo_entrega)
        self.base_datos.guardar_pedido(nuevo_pedido)

    def obtener_registro(self):
        return self.base_datos.cargar_pedidos()

    def limpiar_registro(self):
        self.base_datos.limpiar_registro()
