#Ejercicio 2
import datos
from Mantecado import Mantecado


class Almacen:
    def __init__(self, id: int, direccion: str, mantecados: list[Mantecado]):
        self.id = id
        self.direccion = direccion
        self.mantecados = mantecados

    def total_mantecados(self) -> int:
        return len(self.mantecados)

    def anadir_mantecado(self, m: Mantecado) -> None:
        self.mantecados.append(m)

    def eliminar_mantecado(self, id_mantecado: int) -> bool:
        for m in self.mantecados:
            if m.id == id_mantecado:
                self.mantecados.remove(m)
                return True
            return False

    def mantecados_caducados(self) -> list[Mantecado]:
        caducados = []
        
        for m in self.mantecados:
            if m.esta_caducado() == True:
                caducados.append(m)
        return caducados

    def proximos_a_caducar(self, n: int) -> list[Mantecado]:
        casi_caducados = []

        for m in self.mantecados:
            if m.dias_para_caducar() <= n and m.esta_caducado() == False:
                casi_caducados.append(m)
        return casi_caducados

    def mantecados_en_rango_precio(self, minimo: float, maximo: float) -> list[Mantecado]:
        mantecados_en_precio = []
        for m in self.mantecados:
            if m.precio >= minimo and m.precio <= maximo:
                mantecados_en_precio.append(m)
        return mantecados_en_precio


    def sin_ingrediente(self, ingrediente: str) -> list[Mantecado]:
        for m in self.mantecados:
            for i in m.ingredientes:
                if i != ingrediente:
                    m.ingredientes.append(ingrediente)
        
        return m.ingredientes


    def reporte_por_ingrediente(self) -> dict[str, int]:
        pass

    def reporte_por_tipo(self) -> dict[str, int]:
        pass

    if __name__ == '__main__':
        pass