import unittest
from estudiante import Estudiante
from grupo import Grupo


class TestGrupo(unittest.TestCase):

    def test_agregar(self):
        estudiante1 = Estudiante(1, "Marta", [7, 8])
        
        grupo = Grupo(1, "1DAW")
        grupo.agregar(estudiante1)
        self.assertEqual(len(grupo.estudiantes), 1)

    def test_eliminar(self):
        grupo = Grupo(1, "1DAW")

        estudiante1 = Estudiante(1, "Juan", [6, 8])
        estudiante2 = Estudiante(2, "Marta", [7, 8])
        
        grupo.agregar(estudiante1)
        grupo.agregar(estudiante2)

        grupo.eliminar(1)

        self.assertEqual(grupo.estudiantes[0].nombre, "Marta")

    def test_buscar_por_id(self):
        grupo = Grupo(1, "1DAW")

        estudiante1 = Estudiante(1, "Juan", [6, 8])
        estudiante2 = Estudiante(2, "Marta", [7, 8])
        estudiante3 = Estudiante(3, "Pedro", [6, 7])
        estudiante4 = Estudiante(4, "Daniela", [8, 8])
        
        grupo.agregar(estudiante1)
        grupo.agregar(estudiante2)
        grupo.agregar(estudiante3)
        grupo.agregar(estudiante4)

        tercero = grupo.buscar_por_id(3)

        self.assertEqual(tercero.nombre, "Pedro")

    def test_promocionados(self):
        grupo = Grupo(1, "1DAW")

        estudiante1 = Estudiante(1, "Juan", [6, 8])
        estudiante2 = Estudiante(2, "Marta", [4, 4])
        estudiante3 = Estudiante(3, "Pedro", [4, 5])
        estudiante4 = Estudiante(4, "Daniela", [8, 8])
        
        grupo.agregar(estudiante1)
        grupo.agregar(estudiante2)
        grupo.agregar(estudiante3)
        grupo.agregar(estudiante4)

        promocionados = grupo.promocionados()

        self.assertEqual(promocionados, [estudiante1, estudiante4])

    def test_ordenar_por_media(self):
        grupo = Grupo(1, "1DAW")

        estudiante1 = Estudiante(1, "Juan", [6, 8])
        estudiante2 = Estudiante(2, "Marta", [4, 6])
        estudiante3 = Estudiante(3, "Pedro", [4, 5])
        estudiante4 = Estudiante(4, "Daniela", [8, 8])
        
        grupo.agregar(estudiante1)
        grupo.agregar(estudiante2)
        grupo.agregar(estudiante3)
        grupo.agregar(estudiante4)

        ordenados = grupo.ordenar_por_media()

        self.assertEqual(ordenados[0], estudiante3)
        self.assertEqual(ordenados[-1], estudiante4)

    def test_media_grupo(self):
        grupo = Grupo(1, "1DAW")

        estudiante1 = Estudiante(1, "Juan", [6, 8])
        estudiante2 = Estudiante(2, "Marta", [4, 6])
        estudiante3 = Estudiante(3, "Pedro", [4, 5])
        
        grupo.agregar(estudiante1)
        grupo.agregar(estudiante2)
        grupo.agregar(estudiante3)

        media = (
            estudiante1.media() +
            estudiante2.media() +
            estudiante3.media()
        ) / 3

        self.assertEqual(grupo.media_grupo(), media)
    
if __name__ == "__main__":
    unittest.main()