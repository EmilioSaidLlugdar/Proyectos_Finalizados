from random import randint

print('*** Juego de Adivinanzas ***')

nro_secreto = randint(1,50)
intentos =0
adivinanza = None
INTENTOS_MAX= 5

while adivinanza != nro_secreto and intentos < INTENTOS_MAX:
    adivinanza= int(input('Adivina el número secreto (1 - 50): '))
    #agregamos una ayuda
    if adivinanza < nro_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > nro_secreto:
        print('El numero secreto es menor')
    #incrementamos la variable de intentos
    intentos += 1

#conclusion del juegos
else:
    if adivinanza == nro_secreto:
        print(f'FELICIDADES adivinaste el numero secreto en {intentos} intentos')
    else:
        print(f' Lo siento, has agotado tus intentos máximo: {INTENTOS_MAX}')
        print(f' El número secreto era: {nro_secreto}')