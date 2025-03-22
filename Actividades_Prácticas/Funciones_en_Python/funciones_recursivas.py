print('+++++ imprimir del 1 al 5 de forma recursiva +++++')

#definir la funcion recursiva
def fcion_recursiva(num):
    #caso base
    if num ==1:
        print(num, end=' ') #1
    else:#caso recursivo

        fcion_recursiva(num - 1)
        print(num, end=' ')

#llamamos la funcion
fcion_recursiva(5)