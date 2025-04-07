from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,lado, color):
        FiguraGeometrica.__init__(self,lado, lado)
        Color.__init__(self,color)
        #no usamos super().__init__() por que presta confusion
    def calcular_area(self):
        return self.alto * self.ancho #accedemos directo a los atributos padre