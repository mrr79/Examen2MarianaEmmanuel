import unittest
from Examen2 import MiClase


class TestMiClase(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    def test_obtiene_valencia_1(self):
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)

    def test_obtiene_valencia_2(self):
        resultado = self.objeto.ObtieneValencia(13579)
        self.assertEqual(resultado, 5)

    def test_obtiene_valencia_3(self):
        resultado = self.objeto.ObtieneValencia(24680)
        self.assertEqual(resultado, 0)

    def test_obtiene_valencia_4(self):
        resultado = self.objeto.ObtieneValencia(987654321)
        self.assertEqual(resultado, 5)

    def test_obtiene_valencia_5(self):
        # Prueba con un único dígito cero
        resultado = self.objeto.ObtieneValencia(0)
        self.assertEqual(resultado, 0)

    def test_divisible_tempo_1(self):
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])

    def test_divisible_tempo_2(self):
        resultado = self.objeto.DivisibleTempo(15)
        self.assertEqual(resultado, [1, 3, 5, 15])

    def test_divisible_tempo_3(self):
        resultado = self.objeto.DivisibleTempo(8)
        self.assertEqual(resultado, [1, 2, 4, 8])

    def test_divisible_tempo_4(self):
        resultado = self.objeto.DivisibleTempo(20)
        self.assertEqual(resultado, [1, 2, 4, 5, 10, 20])

    def test_divisible_tempo_5(self):
        # Prueba con un tempo primo
        resultado = self.objeto.DivisibleTempo(13)
        self.assertEqual(resultado, [1, 13])

    def test_obtiene_mas_bailable_1(self):
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)

    def test_obtiene_mas_bailable_2(self):
        resultado = self.objeto.ObtieneMasBailable([0.5, 0.6, 0.4])
        self.assertEqual(resultado, 0.6)

    def test_obtiene_mas_bailable_3(self):
        resultado = self.objeto.ObtieneMasBailable([0.3, 0.2, 0.1])
        self.assertEqual(resultado, 0.3)

    def test_obtiene_mas_bailable_4(self):
        resultado = self.objeto.ObtieneMasBailable([0.7, 0.6, 0.8])
        self.assertEqual(resultado, 0.8)

    def test_obtiene_mas_bailable_5(self):
        # Prueba con una lista vacía
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    def test_verifica_lista_canciones_1(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)

    def test_verifica_lista_canciones_2(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", None, "Canción 3"])
        self.assertFalse(resultado)

    def test_verifica_lista_canciones_3(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción A", "Canción B", "Canción C"])
        self.assertTrue(resultado)

    def test_verifica_lista_canciones_4(self):
        resultado = self.objeto.VerificaListaCanciones([None, None, None])
        self.assertFalse(resultado)


    def test_verifica_lista_canciones_6(self):
        # Prueba con tempo par
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()