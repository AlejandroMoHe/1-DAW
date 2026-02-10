from dataclasses import dataclass
from datetime import datetime


@dataclass
class Proveedor:
   id_proveedor: int
   nombre: str
   telefono: float
   email: str
   localidad: str

class Pedido:
   id_pedido: int
   fecha_pedido: datetime
   fecha_entrega: datetime
   precio_total: float
   direccion_envio: str
   peso_kg: float
   tipo_producto: str
   id_proveedor: int