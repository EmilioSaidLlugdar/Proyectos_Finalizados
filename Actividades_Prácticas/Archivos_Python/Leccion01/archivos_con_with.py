#with abre y cierra el archivo, automaticamente
# sin necesidad de try catch
# with open('prueba.txt','r',encoding='utf8') as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())


