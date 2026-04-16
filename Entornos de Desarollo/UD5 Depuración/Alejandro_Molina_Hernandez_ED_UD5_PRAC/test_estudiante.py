from estudiante import Estudiante
import unittest


class TestEstudiante(unittest.TestCase):
    
    def test_promocionar(self):
        pass


    def test_media(self):
        self.assertEqual(Estudiante.media(), 4)
        self.assertAlmostEqual(Estudiante.media(), 1.5)
    
    
    def test_añadir_nota(self):
        pass


if __name__ == "__main__":

    alumno = Estudiante(1, "Juan", [4, 5, 6])

    unittest.main()