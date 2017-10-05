import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.operaciones = Calculadora()

	def test_sumar_2_mas_2_igual_4(self):
		self.operaciones.suma(2, 2)
		self.assertEquals(self.operaciones.obtener_resultado(),4)

	def test_sumar_1_mas_12_igual_13(self):
		self.operaciones.suma(1, 12)
		self.assertEquals(self.operaciones.obtener_resultado(),13)

	def test_sumar_3_mas_3_igual_6(self):
		self.operaciones.suma(3, 3)
		self.assertEquals(self.operaciones.obtener_resultado(),6)

	def test_sumar_menos1_mas_2_igual_1(self):
		self.operaciones.suma(-1, 2)
		self.assertEquals(self.operaciones.obtener_resultado(),1)

	def test_restar_5_menos_4_igual_1(self):
		self.operaciones.resta(5,4)
		self.assertEquals(self.operaciones.obtener_resultado(),1)

	def test_restar_3_menos_3_igual_0(self):
		self.operaciones.resta(3,3)
		self.assertEquals(self.operaciones.obtener_resultado(),0)

	def test_multiplicar_3_por_2_igual_6(self):
		self.operaciones.multiplicacion(3,2)
		self.assertEquals(self.operaciones.obtener_resultado(),6)

	def test_multiplicar_menos2_por_2_igual_menos4(self):
		self.operaciones.multiplicacion(-2,2)
		self.assertEquals(self.operaciones.obtener_resultado(),-4)

	def test_multiplicar_menos2_por_menos2_igual_4(self):
		self.operaciones.multiplicacion(-2,-2)
		self.assertEquals(self.operaciones.obtener_resultado(),4)

	def test_division_4_entre_2_igual_2(self):
		self.operaciones.division(4,2)
		self.assertEquals(self.operaciones.obtener_resultado(),2)

	def test_division_1_entre_10_igual_0(self):
		self.operaciones.division(1,10)
		self.assertEquals(self.operaciones.obtener_resultado(),0)

	def test_division_1_entre_menos1_igual_menos1(self):
		self.operaciones.division(1,-1)
		self.assertEquals(self.operaciones.obtener_resultado(),-1)

	def test_raiz_de_5_igual_2punto2(self):
		self.operaciones.raiz(5,0)
		self.assertEquals(self.operaciones.obtener_resultado(),2.2)

	def test_raiz_de_0_igual_0punto0(self):
		self.operaciones.raiz(0,0)
		self.assertEquals(self.operaciones.obtener_resultado(),0.0)

	def test_potencia_de_5_al_cuadrado_igual_25(self):
		self.operaciones.potencia(5,2)
		self.assertEquals(self.operaciones.obtener_resultado(),25)

	def test_potencia_de_2_al_cuadrado_igual_4(self):
		self.operaciones.potencia(2,2)
		self.assertEquals(self.operaciones.obtener_resultado(),4)

	def test_potencia_de_4_al_cubo_igual_64(self):
		self.operaciones.potencia(4,3)
		self.assertEquals(self.operaciones.obtener_resultado(),64)

if __name__ == '__main__': #pragma: no cover
	unittest.main()
