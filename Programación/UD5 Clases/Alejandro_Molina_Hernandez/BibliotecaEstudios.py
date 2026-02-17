from EstudiosAnima import Estudio

class BibliotecaEstudios:
    def __init__(self, id: int, titulo: str, estudios: list[Estudio]):
        self.id = id
        self.titulo = titulo
        if len(estudios) > 0:
            self.estudios = estudios
    

    def añadir(self, e: Estudio) -> None:
        self.estudios.append(e)
    

    def eliminar_estudio(self, id: int) -> bool:
        for e in self.estudios:
            if e.id == id:
                self.estudios.remove(e)
                return True
        return False
    

    def actualiza_estado(cambio: str, eleccion: int) -> None:
        eleccion = input(int("Que estudio quieres cambiar?"))
        cambio = input("Sigue abierto el estudio?(S/N) ")

        if cambio == "S" and Estudio.id == eleccion:
            Estudio.abierto == True
        elif cambio == "N" and Estudio.id == eleccion:
            Estudio.abierto == False


    def cambia_nombre(nuevo: str) -> None:
        eleccion = input("Que estudio quieres cambiarle el nombre?")
        nuevo = input(int("Escribe el nuevo nombre: "))
        if eleccion == Estudio.id:
            Estudio.nombre = nuevo


    def menor_ganacia():
        pass


    def ordenar_apertura():
        sorted(Estudio.fecha_apertura)


    def tiempo_abierto():
        pass


    def estreno_hoy():
        pass


    def __str__(self):
        str_biblioteca = f"{self.id} | {self.titulo}"
        for e in self.estudios:
            str_biblioteca += f"{e}\n"
        return str_biblioteca