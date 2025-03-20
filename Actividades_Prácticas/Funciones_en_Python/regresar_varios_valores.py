print('++++ Regresar una tupla de valores desde una funcion ++++')

#definir la funcion
def persona_mayuscula(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (tupla)')
    return nombre.upper(),apellido.upper(), edad

#main
nombre,apellido,edad= persona_mayuscula('Fabio','Aoad', 35) #usamos el concepto de empaque
print(f'\nResultado Persona: nombre:{nombre}, apellido: {apellido}, edad: {edad}')
