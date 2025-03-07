print('***** Cálculo Área y Perímetro de un Rectángulo *****')

base = int(input('Ingrese la base del Rectángulo:\n'))
altura = int(input('Ingrese la altura del Rectángulo:\n'))

#calculamos
area = base * altura
perimetro = 2 * (base + altura)

print(f'El área del Rectángulo es:\n {area}')
print(f'El perímetro del Rectángulo es:\n {perimetro}')