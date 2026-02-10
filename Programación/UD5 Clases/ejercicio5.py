from dataclasses import dataclass


@dataclass
class Alumno:
   id_alumno: int
   nombre: str
   email: str

class Pedido:
   id_asignatura: int
   nombre: str
   horas_semanales: float

class Matricula:
   id_alumno: int
   id_asignatura: int

