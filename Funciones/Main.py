# %% Funciones  
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Buscar_cometa import buscar_cometa
from Funciones.Verificar_cometa import verificar_cometa
from Funciones.Envolvente_superior import envolvente_superior
from Funciones.Envolvente_inferior import envolvente_inferior
from Funciones.Envolvente_superior_inferior import envolvente_superior_inferior

# %% Main
def main() -> None:
    '''
    Realiza el llamado a los principales módulos del programa y controla la ejecución del mismo.
    '''

    #  Variables
    Terminar : bool = False
    opcion_elegida: str = '-1'
    opciones : str = '12345'
    texto_opciones : str  = f'''Elija una de las siguientes opciones:
[1] : Buscar un comenta.
[2] : Graficar curvas de luz externas (Envolvente superior).
[3] : Graficar curvas de luz internas (Envolvente inferior).
[4] : Graficar curvas de luz externa e internas (Envolvente inferior e inferior).
[5] : Finalizar programa.\n
Ingrese aquí su elección: '''
    
    # Verificar la conexión a internet.
    conectado_a_internet = verificar_conexion()

    # Ciclo principal
    while conectado_a_internet:

        # Leer opcion elegida
        while opcion_elegida not in opciones:
            opcion_elegida = input(texto_opciones)

        # Buscar cometa
        if opcion_elegida == '1':
            nombre_cometa = input('\nIngrese el nombre del cometa que desea buscar o, "volver_menu" para regresar: ')

            if nombre_cometa != 'volver_menu':
                buscar_cometa(nombre_cometa)
        
        # Graficar curvas de luz externa 
        elif opcion_elegida == '2':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "volver_menu" para regresar: ') #'C/2023 A3'
            fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD: ')

            if nombre_cometa != 'volver_menu' and verificar_cometa(nombre_cometa, conectado_a_internet):
                envolvente_superior(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Graficar curvas de luz interna
        elif opcion_elegida == '3':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "volver_menu" para regresar: ') #'C/2023 A3'
            fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD: ')

            if nombre_cometa != 'volver_menu' and verificar_cometa(nombre_cometa, conectado_a_internet):
                envolvente_inferior(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Graficar ambas curvas de luz interna y externa
        elif opcion_elegida == '4':
            nombre_cometa = input('Ingrese el nombre del cometa que desea graficar o, "volver_menu" para regresar: ') #'C/2023 A3'
            fecha_inicial = input('Ingrese la fecha inicial para el análisis en el formato AAAA-MM-DD: ')

            if nombre_cometa != 'volver_menu' and verificar_cometa(nombre_cometa, conectado_a_internet):
                envolvente_superior_inferior(nombre_cometa, fecha_inicial)

        # Finalizar programa
        elif opcion_elegida == '5':
            print('\nPrograma finalizado por el usuario.')
            break

        # Resetear opción elegida
        opcion_elegida = '-1'

        # Verificar la conexión a internet.
        conectado_a_internet = verificar_conexion()

if __name__ == '__main__':
    main()