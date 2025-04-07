from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(f'Cálculo área Cuadrado:{cuadrado1.calcular_area()}')

#MRO - Method Resolution Order
print(Cuadrado.mro())
