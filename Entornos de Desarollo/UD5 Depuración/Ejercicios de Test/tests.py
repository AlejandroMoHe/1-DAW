#Ejercicio 1
import unittest
from Estudiante import Estudiante
from Grupo import Grupo

class TestEstudiante(unittest.TestCase):
    
    def test_promocionar(self):
        e = Estudiante(1, "Laura", [5.1, 8.2, 9.4, 6.7])
        self.assertTrue(e.promocionar())


    def test_media(self):
        pass


class TestGrupo(unittest.TestCase):
    
    def test_agregar(self):
        grupo = Grupo(1, "1Daw")
        e = Estudiante(1, "Alberto", [6, 8.2, 4.8, 6.7])

        grupo.agregar(e)

        self.assertEqual(len(grupo.estudiantes), 1)


    def test_eliminar(self):
        grupo = Grupo(2, "2DAW")

        e1 = Estudiante(1, "Manuel", [5, 8, 7, 9.2])
        e2 = Estudiante(2, "Antonio",[6, 4, 7, 9])

        grupo.agregar(e1)
        grupo.agregar(e2)

        grupo.eliminar(1)

        self.assertEqual(len(grupo.estudiantes), 1)
        self.assertEqual(grupo.estudiantes[0].nombre, "Antonio")
    

    def test_buscar_por_id(self):
        grupo = Grupo(1, "1ASIR")

        grupo.agregar(Estudiante("Ragnar", "guerrero", 5, 15, 40))
        grupo.agregar(Estudiante("Arthos", "guerrero", 3, 10, 30))
        grupo.agregar(Estudiante("Merlin", "mago", 4, 12, 25))

        estudiantes = grupo.buscar_por_id(1)

        self.assertEqual(len(estudiantes), 2)


    def test_promocionados(self):
        pass


    def test_media_grupo(self):
        grupo = Grupo(1, "1DAW")

        grupo.agregar(Estudiante(1, "Álvaro", [2, 10, 30]))
        grupo.agregar(Estudiante(2, "Ernesto", [4, 8, 20]))

        self.assertAlmostEqual(grupo.media_grupo(), 3)


if __name__ == "__main__":
    unittest.main()