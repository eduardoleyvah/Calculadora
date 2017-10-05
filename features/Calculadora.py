import math

class Calculadora():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self,num1,num2):
        self.resultado = num1 + num2

    def resta(self, num1, num2):
        self.resultado = num1 - num2

    def multiplicacion(self, num1, num2):
        self.resultado = num1 * num2

    def division(self, num1, num2):
        self.resultado = num1 / num2

    def raiz(self, num1, num2):
        self.resultado = round((math.sqrt(num1)),1)

    def potencia(self, num1, num2):
        self.resultado = pow(num1,num2)
