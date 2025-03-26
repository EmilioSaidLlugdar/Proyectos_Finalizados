print('*** Concertidor de Temperatura ***')

#funcion que convierte de celcius a fahrenheit

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_celsius(far):
    return (far - 32)* 5 / 9

#probamos convertir de Celsius a Fahrenheit
celsius = float(input('Proporcione su valor en CELSIUS: '))
print(f'{celsius} C a F --> {celsius_fahrenheit(celsius):.2f}')

#probamos convertir de Fahrenheit a Celsius
far = float(input('Proporcione su valor en FAHRENHEIT: '))
print(f'{far} F a C --> {fahrenheit_celsius(far):.2f}')
