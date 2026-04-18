# Librerías
from pandas import DataFrame

# Modulos
from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def guardar_archivo(nombre_cometa: str, curva_de_luz_df: DataFrame, nombre_archivo) -> None:
    '''
    Guarda el archivo con los datos procesados del cometa.
    '''

    archivo_curva_de_luz_df = DataFrame()
    archivo_curva_de_luz_df['Year'] = curva_de_luz_df.obs_date.dt.year
    archivo_curva_de_luz_df['Month'] = curva_de_luz_df.obs_date.dt.month
    archivo_curva_de_luz_df['Day'] = curva_de_luz_df.obs_date.dt.day
    archivo_curva_de_luz_df['t-Tq'] = curva_de_luz_df.delta_t
    archivo_curva_de_luz_df['delta'] = curva_de_luz_df.delta.round(3)
    archivo_curva_de_luz_df['R'] = curva_de_luz_df.r.round(3)
    archivo_curva_de_luz_df['alpha'] = curva_de_luz_df.phase
    archivo_curva_de_luz_df['MAG'] = curva_de_luz_df.magnitude.round(2)
    archivo_curva_de_luz_df['m(1,1,0)'] = curva_de_luz_df.magnitud_reducida.round(2)
    archivo_curva_de_luz_df['m(1,1,alpha)'] = curva_de_luz_df.magnitud_reducida_con_fase.round(2)

    nombre_archivo = f'{nombre_archivo}_{nombre_cometa}_COBS'
    
    ruta_archivos = crear_carpetas(nombre_cometa, nombre_archivo = nombre_archivo, carpeta_base='Bases_de_datos', tipo_archivo= 'txt')
    archivo_curva_de_luz_df.to_csv(ruta_archivos, index=False, sep='\t')

if __name__ == '__main__':
    guardar_archivo()