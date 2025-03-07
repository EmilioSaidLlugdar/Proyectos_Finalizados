print('*** Sistema Prestamo de Libros ***')

distancia_permitida_km = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)?')
distancia_biblioteca = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si'
                        or distancia_biblioteca <= distancia_permitida_km)

print(f'Eres elegible para prestamo de Libros? {es_elegible_prestamo}')