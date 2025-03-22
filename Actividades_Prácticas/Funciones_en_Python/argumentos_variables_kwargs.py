print('----- Argumentos Variables en forma de Diccionario------')
print(' kwargs --> keywords arguments (key. value) como un dictionary')

def superheroes_superpoderes(nombre, *args, **kwargs):
    print(f'\nSuperheroe: {nombre} - {args}  \nMas info: {kwargs}')

#llamamos a la funcion
superheroes_superpoderes('Spiderman','Arácnido', edad=17, empresa='Marvel')
superheroes_superpoderes('Ironman', 'Armadura','Playboy', edad=45)

#es opcional enviar argumentos variable
superheroes_superpoderes('mi vecino')