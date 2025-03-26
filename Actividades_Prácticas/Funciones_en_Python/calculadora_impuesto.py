print('*** Calculadora de Impuestos ***')

def calcular_total_pago(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

#llamamos a la funcion
pago_sin_imp = float(input('Ingrese el pago sin impuestos: '))
impuesto = float(input('Ingrese el monto del impuesto: '))
print(f' Pago con Impuesto: {calcular_total_pago(pago_sin_imp, impuesto)}')
