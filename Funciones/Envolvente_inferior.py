# Funciones
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Verificar_cometa import verificar_cometa
from Funciones.Verificar_fecha import verificar_fecha
from Funciones.Conectar_con_API_de_COBS_Observaciones import conectar_con_API_de_COBS_Observaciones
from Funciones.Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Funciones.Descargar_efemerides import descargar_efemerides
from Funciones.Obtener_perihelio import obtener_perihelio
from Funciones.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Funciones.Promedio_movil_minimo import promedio_movil_minimo
from Funciones.Crear_curvas_de_luz import crear_curvas_de_luz

def envolvente_inferior(nombre_cometa: str, fecha_inicial: str, conectado_a_internet: bool) -> tuple[object]:
    '''
    Procesa los datos del cometa especificado para calcular la 
    envolvente inferior de la curva de luz del cometa especificado.
    Retorna: 
    [1] curva_de_luz_cruda_df,
    [2] curva_de_luz_procesada_df, 
    [3] curva_de_luz_interna_df.
    '''

    # Verificar cometa en la base de datos y conexión a internet
    if verificar_conexion() and verificar_cometa(nombre_cometa, conectado_a_internet) and verificar_fecha(fecha_inicial):
    
        # Conexión con la API de COBS
        content = conectar_con_API_de_COBS_Observaciones(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Tratamiento de datos observacionales
        curva_de_luz_cruda_df = tratamiento_de_datos_cometa(content)

        # Descargar efemérides
        efemerides = descargar_efemerides(nombre_cometa, curva_de_luz_cruda_df)

        # Obtener perihelio de la API de COBS
        perihelio = obtener_perihelio(nombre_cometa, conectado_a_internet)

        # Tratamiento de datos con efemerides
        curva_de_luz_procesada_df = tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, efemerides, perihelio)

        # Promedio movil
        curva_de_luz_interna_df = promedio_movil_minimo(curva_de_luz_procesada_df)

        # Curva de luz cruda
        variable_a_graficar  = {'magnitude': 'Crude magnitude'}
        titulo = f'Crude lightcurve of {nombre_cometa}'
        crear_curvas_de_luz(nombre_cometa, 'obs_date', variable_a_graficar , curva_de_luz_cruda_df, titulo)

        # Curva de luz reducida
        variable_a_graficar  = {'magnitud_reducida' :'Reduced magnitude'}
        titulo = f'Reduced lightcurve of {nombre_cometa}'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_procesada_df, titulo)

        # Curva de luz interna
        variable_a_graficar  = {'magnitud_reducida':'Minimized reduced magnitude'}
        titulo = f'Minimized external lightcurve of {nombre_cometa}'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_interna_df, titulo)

        # Envolvente inferior
        variable_a_graficar = {'promedio_movil':'Averaged reduced magnitude'}
        titulo = f'Averaged internal lightcurve of {nombre_cometa}'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_interna_df, titulo, promediada = True, color = 'red')

if __name__ == '__main__':
    envolvente_inferior()