# Librerías
from pandas import DataFrame

# Funciones
from Modulos.Manejo_de_errores.Verificar_conexion import verificar_conexion
from Modulos.Manejo_de_errores.Verificar_cometa import verificar_cometa
from Modulos.Manejo_de_errores.Verificar_fecha import verificar_fecha
from Modulos.Coneccion_con_API.Conectar_con_API_de_COBS_Observaciones import conectar_con_API_de_COBS_Observaciones
from Modulos.Procesamiento_de_datos.Extraer_datos_del_cometa import extraer_datos_del_cometa
from Modulos.Coneccion_con_API.Conectar_con_API_de_MPC_Efemerides import descargar_efemerides
from Modulos.Coneccion_con_API.Obtener_perihelio import obtener_perihelio
from Modulos.Procesamiento_de_datos.Procesar_datos_con_efemerides import procesar_datos_con_efemerides
from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def generar_archivos(nombre_cometa: str, fecha_inicial: str, conectado_a_internet: bool) -> None:
    '''
    Procesa los datos del cometa especificado, para calcular la 
    curva de luz reducida y retornar el archivo con los datos respectivos.
    '''

    # Verificar cometa en la base de datos y conexión a internet
    if verificar_conexion() and verificar_cometa(nombre_cometa, conectado_a_internet) and verificar_fecha(fecha_inicial):
    
        # Conexión con la API de COBS
        content = conectar_con_API_de_COBS_Observaciones(nombre_cometa, fecha_inicial, conectado_a_internet)

        # Tratamiento de datos observacionales
        curva_de_luz_cruda_df = extraer_datos_del_cometa(content)

        # Descargar efemérides
        efemerides_df = descargar_efemerides(nombre_cometa, curva_de_luz_cruda_df)

        # Obtener perihelio de la API de COBS
        perihelio = obtener_perihelio(nombre_cometa, conectado_a_internet)

        # Tratamiento de datos con efemerides
        curva_de_luz_procesada_df = procesar_datos_con_efemerides(curva_de_luz_cruda_df, efemerides_df, perihelio)

        # Generar archivos txt
        
        print('⏳ Generando archivo de datos procesados.')

        archivo_curva_de_luz_procesada_df = DataFrame()
        archivo_curva_de_luz_procesada_df['Year'] = curva_de_luz_procesada_df.obs_date.dt.year
        archivo_curva_de_luz_procesada_df['Month'] = curva_de_luz_procesada_df.obs_date.dt.month
        archivo_curva_de_luz_procesada_df['Day'] = curva_de_luz_procesada_df.obs_date.dt.day
        archivo_curva_de_luz_procesada_df['t-Tq'] = curva_de_luz_procesada_df.delta_t
        archivo_curva_de_luz_procesada_df['delta'] = curva_de_luz_procesada_df.delta.round(3)
        archivo_curva_de_luz_procesada_df['R'] = curva_de_luz_procesada_df.r.round(3)
        archivo_curva_de_luz_procesada_df['alpha'] = curva_de_luz_procesada_df.phase
        archivo_curva_de_luz_procesada_df['MAG'] = curva_de_luz_procesada_df.magnitude.round(2)
        archivo_curva_de_luz_procesada_df['m(1,1,0)'] = curva_de_luz_procesada_df.magnitud_reducida.round(2)
        archivo_curva_de_luz_procesada_df['m(1,1,alpha)'] = curva_de_luz_procesada_df.magnitud_reducida_con_phase.round(2)

        nombre_archivo = f'Datos_procesados_cometa_{nombre_cometa}_COBS'

        ruta_archivos = crear_carpetas(nombre_cometa, nombre_archivo = nombre_archivo, carpeta_base='Bases_de_datos', tipo_archivo= 'txt')
        archivo_curva_de_luz_procesada_df.to_csv(ruta_archivos, index=False, sep='\t')

        print(f'✅ Archivo de datos procesados creado.')

        # Numero de registros obtenidos
        filas, __ = curva_de_luz_cruda_df.shape
        print(f'{'-'*40 + '\n'*2}📊 Se descargó con éxito un total de {filas} observaciones de la base de datos COBS referentes al cometa: {nombre_cometa}.')


if __name__ == '__main__':
    generar_archivos()