#profundizando en tipo float
a = 3.0
print(f'a: {a:.2f}')
#constructor tipo flotante puede recibir int y str
a = float(10)
a = float('10')
print(f'a: {a:.2f}')
#notacion exponencial (valores positivos o negativos)
a=3e5
a = 3e-5
# print(f'a: {a:.5f}')
#cualquier calculo que involucre un float, se promueve a punto float
a= 4.0 + 5
print(a)
print(type(a))

