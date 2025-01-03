# Funciones
from Funciones.Curva_de_luz_cruda import curva_de_luz_cruda
from Funciones.Curva_de_luz_reducida import curva_de_luz_reducida
from Funciones.Curva_de_luz_interna import curva_de_luz_interna
from Funciones.Curva_de_luz_interna_promediada import curva_de_luz_interna_promediada
from Funciones.Curva_de_luz_externa import curva_de_luz_externa
from Funciones.Curva_de_luz_externa_promediada import curva_de_luz_externa_promediada
from Funciones.Curvas_de_luz_interna_externa import curvas_de_luz_interna_externa

def generar_grafica(opcion_elegida: str, nombre_cometa: str, bases_de_datos: tuple[object]) -> None:
    '''
    Genera la grafica especificada. Opciones a elegir:
    [1]: Curva de luz cruda,
    [2]: Curva de luz reducida,
    [3]: Curva de luz externa,
    [4]: Curva de luz externa promediada,
    [5]: Curva de luz interna,
    [6]: Curva de luz interna promediada,
    [7]: Curvas de luz  interna y externa.
    '''
    if opcion_elegida == '1':
        curva_de_luz_cruda(nombre_cometa, bases_de_datos[0])

    elif opcion_elegida == '2':
        curva_de_luz_reducida(nombre_cometa, bases_de_datos[1])

    elif opcion_elegida == '3':
        curva_de_luz_externa(nombre_cometa, bases_de_datos[2])

    elif opcion_elegida == '4':
        curva_de_luz_externa_promediada(nombre_cometa, bases_de_datos[2])

    elif opcion_elegida == '5':
        curva_de_luz_interna(nombre_cometa, bases_de_datos[3])

    elif opcion_elegida == '6':
        curva_de_luz_interna_promediada(nombre_cometa, bases_de_datos[3])

    elif opcion_elegida == '7':
        curvas_de_luz_interna_externa(nombre_cometa, bases_de_datos[2],bases_de_datos[3])