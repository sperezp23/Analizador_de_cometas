# Funciones
from Modulos.Manejo_de_errores.Verificar_conexion import verificar_conexion
from Modulos.Manejo_de_errores.Verificar_cometa import verificar_cometa
from Modulos.Manejo_de_errores.Verificar_fecha import verificar_fecha
from Modulos.Coneccion_con_API.Conectar_con_API_de_COBS_Observaciones import conectar_con_API_de_COBS_Observaciones
from Modulos.Procesamiento_de_datos.Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Modulos.Coneccion_con_API.Conectar_con_API_de_MPC_Efemerides import descargar_efemerides
from Modulos.Coneccion_con_API.Obtener_perihelio import obtener_perihelio
from Modulos.Procesamiento_de_datos.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Modulos.Procesamiento_de_datos.Promedio_movil_maximo import promedio_movil_maximo
from Modulos.Procesamiento_de_datos.Promedio_movil_minimo import promedio_movil_minimo
from Modulos.Visualizacion_de_datos.Crear_curvas_de_luz import crear_curvas_de_luz
from Modulos.Visualizacion_de_datos.Curvas_de_luz_interna_externa import curvas_de_luz_interna_externa

def envolvente_superior_inferior(nombre_cometa: str, fecha_inicial: str)-> None:
    '''
    Procesa los datos del cometa especificado para calcular la 
    envolvente inferior de su curva de luz.
    '''

    conectado_a_internet = verificar_conexion() 

    # Verificar cometa en la base de datos y conexión a internet
    if conectado_a_internet and verificar_cometa(nombre_cometa, conectado_a_internet) and verificar_fecha(fecha_inicial):
        
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
        curva_de_luz_externa_df = promedio_movil_maximo(curva_de_luz_procesada_df)
        curva_de_luz_interna_df = promedio_movil_minimo(curva_de_luz_procesada_df)

        # Curva de luz cruda
        variable_a_graficar  = {'magnitude': r'$m(\Delta, R, \alpha)$'}
        titulo = f'Crude lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'obs_date', variable_a_graficar , curva_de_luz_cruda_df, titulo, titulo_eje_x = 'Observation Date')

        # Curva de luz reducida
        variable_a_graficar  = {'magnitud_reducida' :'m(1,1,0)'}
        titulo = f'Reduced lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_procesada_df, titulo)

        # Curva de luz externa
        variable_a_graficar  = {'magnitud_reducida':'Maximized m(1,1,0)'}
        titulo = f'Maximized external lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_externa_df, titulo)

        # Envolvente superior
        variable_a_graficar = {'promedio_movil':'Averaged m(1,1,0)'}
        titulo = f'Averaged external lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_externa_df, titulo, promediada = True, color= '#FFEE00')

        # Curva de luz interna
        variable_a_graficar  = {'magnitud_reducida':'Minimized m(1,1,0)'}
        titulo = f'Minimized internal lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_interna_df, titulo)

        # Envolvente inferior
        variable_a_graficar = {'promedio_movil':'Averaged m(1,1,0)'}
        titulo = f'Averaged internal lightcurve of {nombre_cometa} - data from COBS'
        crear_curvas_de_luz(nombre_cometa, 'delta_t', variable_a_graficar , curva_de_luz_interna_df, titulo, promediada = True, color= 'red')

        # Generar Curva de luz interna y externa
        titulo = f'Max/Min Averaged Lightcurve of comet {nombre_cometa} data from COBS'
        curvas_de_luz_interna_externa(nombre_cometa, curva_de_luz_externa_df, curva_de_luz_interna_df, titulo=titulo)

        # Generar Curva de luz interna y externa sobrepuesta con la curva de luz procesada
        titulo = f'Max/Min/Reduced Lightcurve of comet {nombre_cometa} data from COBS'
        curvas_de_luz_interna_externa(nombre_cometa, curva_de_luz_externa_df, curva_de_luz_interna_df, curva_de_luz_procesada_df, titulo=titulo, sobrepuestas=True)

if __name__ == '__main__':
    envolvente_superior_inferior()
