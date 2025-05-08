import  logging as log #renombramos el paquete para llamar simplemente log
#parametros posicional
# %(asctimes)s: esto agrega el tiempo (fecha/hs) al mensaje de log
# %(levelname)s agrega el nivel del mensaje que enviamos (info, error, etc)
# [%(filename)s] agrega el nombre del archivo al mensaje del log
#%(lineno)s agrega el numero de linea al mensaje del log
#%(message)s muestra el mensaje  que hemos agregado al log
#datefmt='%I:%M:%S %p' damos formato a la hs,min,seg y pm/am


#configuracion basica del manejo del loggin
log.basicConfig(level=log.INFO, #podemos usar DEBUG para mostrar mas informacion
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[ #para arrojar el error a un archivo llamado capa_datos.log y le agregamos info a StreamHandel la consola que manejamos
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')