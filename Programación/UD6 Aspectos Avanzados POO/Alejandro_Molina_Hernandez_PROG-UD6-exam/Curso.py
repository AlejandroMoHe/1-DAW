class Curso:
    def __init__(self, id: int, nombre: str, creditos: int, profesor: str, alumnos: list[int], plazas_totales: int):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.profesor = profesor
        self.alumnos = alumnos
        self.plazas_totales = plazas_totales
    
    
    def matricular(self, alumno_id: int) -> bool:
        if alumno_id not in self.alumnos and len(self.alumnos) < self.plazas_totales:
            self.alumnos.append(alumno_id)
            return True
        else: 
            return False


    def desmatricular(self, alumno_id: int) -> bool:
        for alumno in self.alumnos:
            if alumno_id == alumno:
                self.alumnos.remove(alumno_id)
                return True
            else: 
                return False


    def plazas_disponibles(self) -> int:
        return self.plazas_totales


    def esta_matriculado(self, alumno_id: int) -> bool:
        for alumno in self.alumnos:
            if alumno_id == alumno:
                return True
            else: 
                return False


    def __eq__(self, other) -> bool:
        if isinstance(other, Curso):
            return self.id == other.id
        return False

    
    def __hash__(self) -> int:
        return self.id


    def __str__(self):
        return f"Curso | ID: {self.id} | Nombre: {self.nombre} | Créditos: {self.creditos} | Plazas libres: {self.plazas_disponibles()}"