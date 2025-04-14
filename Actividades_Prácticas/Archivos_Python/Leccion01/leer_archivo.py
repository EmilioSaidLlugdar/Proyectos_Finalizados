archivo = open('prueba.txt','r',encoding='utf8')
# print(archivo.read())

#leer algunos caracteres

# print(archivo.read(5))
# print(archivo.read(3))

#leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

#iterar el archivo cada linea
# for linea in archivo:
#     print(linea)

#leer todas las lineas
# print(archivo.readlines())

#acceder a una linea de una lista
# print(archivo.readlines()[2])

#abrimos un nuevo archivo
#a - anexar info
archivo2 =  open('copia.txt','w',encoding='utf8')
archivo2.write(archivo.read())

archivo2.close()
archivo.close()
print('Terminó el proceso de leer y copiar archivos')