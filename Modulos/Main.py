# %% Funciones  
from Modulos.Manejo_de_errores.Verificar_conexion import verificar_conexion
from Modulos.Lectura_de_archivos.Leer_instrucciones import leer_instrucciones
from Modulos.Manejo_de_errores.Buscar_cometa import buscar_cometa
from Modulos.Manejo_de_errores.Verificar_fecha import verificar_fecha
from Modulos.Procesamiento_de_datos.Envolvente_superior import envolvente_superior
from Modulos.Procesamiento_de_datos.Envolvente_inferior import envolvente_inferior
from Modulos.Procesamiento_de_datos.Envolvente_superior_inferior import envolvente_superior_inferior
from Modulos.Generar_archivos.Generar_archivos import generar_archivos

# %% Main
def main() -> None:
    '''
    Realiza el llamado a los principales módulos del programa y controla la ejecución del mismo.
    '''

    #  Variables
    opcion_elegida: str = '-1'
    opciones : str = 'i123456'
    mensaje_de_inicio: str = f'{'\n'*2}{'='*32}\n|| GENERADOR DE CURVAS DE LUZ ||\n{'='*32}'
    texto_opciones : str  = f'''Elija una de las siguientes opciones:\n
[i] : Instrucciones (mostrar en pantalla las instrucciones del programa).\n
[1] : Buscar el nombre de un cometa en la base de datos COBS.
[2] : Graficar curvas de luz externas (Envolvente superior).
[3] : Graficar curvas de luz internas (Envolvente inferior).
[4] : Graficar curvas de luz externa e internas (Envolvente Exterior e inferior).
[5] : Generar archivo.
[6] : Finalizar programa.\n
Ingrese aquí su elección: '''
    
    # Mensaje de inicio.
    print(mensaje_de_inicio)
    
    # Verificar la conexión a internet.
    conectado_a_internet = verificar_conexion()

    # Ciclo principal
    while conectado_a_internet:

        # Leer opcion elegida
        while opcion_elegida not in opciones:
            opcion_elegida = input(texto_opciones)

        # Instrucciones
        if opcion_elegida == 'i':
            leer_instrucciones(r'Instrucciones.txt')

        # Buscar cometa
        if opcion_elegida == '1':
            nombre_cometa = input('\nIngrese el nombre del cometa que desea buscar o, "menu" para regresar al inicio: ')

            if nombre_cometa != 'menu':
                buscar_cometa(nombre_cometa)
        
        # Graficar curvas de luz externa 
        elif opcion_elegida == '2':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "menu" para regresar al inicio: ') #'C/2023 A3'

            if nombre_cometa != 'menu':
                fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD o, "menu" para regresar al inicio: ')

                if fecha_inicial != 'menu' and verificar_fecha(fecha_inicial):
                    envolvente_superior(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Graficar curvas de luz interna
        elif opcion_elegida == '3':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "menu" para regresar al inicio: ') #'C/2023 A3'

            if nombre_cometa != 'menu':

                fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD o, "menu" para regresar al inicio: ')

                if fecha_inicial != 'menu' and verificar_fecha(fecha_inicial):
                    envolvente_inferior(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Graficar ambas curvas de luz interna y externa
        elif opcion_elegida == '4':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "menu" para regresar al inicio: ') #'C/2023 A3'
        
            if nombre_cometa != 'menu':
                fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD o, "menu" para regresar al inicio: ')

                if fecha_inicial != 'menu' and verificar_fecha(fecha_inicial):
                    envolvente_superior_inferior(nombre_cometa, fecha_inicial)

        # Generar archivo
        elif opcion_elegida == '5':
            nombre_cometa = input('Ingrese el nombre del cometa que desea buscar o, "menu" para regresar al inicio: ') #'C/2023 A3'

            if nombre_cometa != 'menu':
                fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD o, "menu" para regresar al inicio: ')

                if fecha_inicial != 'menu' and verificar_fecha(fecha_inicial):
                    generar_archivos(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Finalizar programa
        elif opcion_elegida == opciones[-1]:
            print('\nPrograma finalizado por el usuario.')
            break
        
        # Mensaje de inicio
        print(mensaje_de_inicio)

        # Resetear opción elegida
        opcion_elegida = '-1'

        # Verificar la conexión a internet.
        conectado_a_internet = verificar_conexion()

if __name__ == '__main__':
    main()