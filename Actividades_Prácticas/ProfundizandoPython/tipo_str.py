from quopri import ishex

from mi_clase import MiClase
#profundizando en el tipo str

#concatenacion automatica en python
# variable = 'adios'
# mensaje = 'Hola'  'Mundo'+  variable
# mensaje += 'universidad' 'python'
# print(mensaje)

#help sirve para cualquier tipo de dato o modulo
# help(math.isnan)
# help(str.capitalize)

# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))

# mensaje1 = 'hola mundo'
# mensaje2 =  mensaje1.capitalize()
# print(f'Mensaje 1: {mensaje1},id {hex(id(mensaje1))}') #id es la direccion de la memoria
# print(f'Mensaje 2: {mensaje2},id {hex(id(mensaje2))}')

#-------------------------dar formato a str
# nombre = 'Juan'
# edad = 28
# mensaje_con_formato = 'Mi nombre es %s y tengo %s años'%(nombre, edad)
# print(mensaje_con_formato)

# persona = ('Emilio', 'Llugdar', 100000)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' %(persona)
# print(mensaje_con_formato)

# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)


nombre = 'Emilio'
edad = 34
sueldo = 30000
# mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad, sueldo)
# print(mensaje)

# mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)

# mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre,edad,sueldo)
# print(mensaje)

# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

# diccionario = {'nombre': 'emilio', 'edad': 34, 'sueldo': 20000}
# mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]}'.format(persona=diccionario)
# print(mensaje)

mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
# print(mensaje)

#metodo print
print(nombre,edad,sueldo, sep=' , ')