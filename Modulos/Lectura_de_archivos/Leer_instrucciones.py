def leer_instrucciones(ruta):
    with open(ruta, 'r') as instrucciones:
        contenido = instrucciones.read()
        print(contenido)

if __name__ == '__main__':
    leer_instrucciones()