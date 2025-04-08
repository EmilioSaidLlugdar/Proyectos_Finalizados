from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

#no se puede instanciar una clase abstracta
# figura =FiguraGeometrica()

print('\n')
print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5,'rojo')
# cuadrado1.alto = -10
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(f'Cálculo área Cuadrado:{cuadrado1.calcular_area()}')
print(cuadrado1)
print('\n')



print('Creación Objeto Rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(9,8,'Verde')
# rectangulo1.ancho = 15
print(f'Cálculo área Rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

# MRO - Method Resolution Order --> muestra el orden de jerarquia de clases
print(Cuadrado.mro())