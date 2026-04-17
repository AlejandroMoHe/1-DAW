import unittest
from estudiante import Estudiante


class TestEstudiante(unittest.TestCase):

    def test_promocionar(self):
        estudiante = Estudiante(1, "Juan", [5, 6])
        self.assertTrue(estudiante.promocionar())

    def test_media(self):
        estudiante = Estudiante(3, "Luis", [4, 6])
        self.assertEqual(estudiante.media(), 5)

    def test_añadir_nota(self):
        estudiante = Estudiante(5, "Carlos", [5, 6])
        estudiante.anadir_nota(7)

        self.assertEqual(estudiante.notas, [5, 6, 7])


if __name__ == "__main__":
    unittest.main()