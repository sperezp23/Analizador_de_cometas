# Funciones
from Funciones.Conectar_con_API_de_COBS_Observaciones import conectar_con_API_de_COBS_Observaciones
from Funciones.Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Funciones.Curva_de_luz_cruda import curva_de_luz_cruda
from Funciones.Conectar_con_API_de_MPC import conectar_con_API_de_MPC
from Funciones.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Funciones.Curva_de_luz_reducida import curva_de_luz_reducida
from Funciones.Promedio_movil_minimo import promedio_movil_minimo
from Funciones.Curva_de_luz_interna import curva_de_luz_interna
from Funciones.Curva_de_luz_interna_promediada import curva_de_luz_interna_promediada

def envolvente_inferior(nombre_cometa, conectado_a_internet):
    # Conexión con la API de COBS
    content = conectar_con_API_de_COBS_Observaciones(nombre_cometa, conectado_a_internet)

    # Tratamiento de datos observacionales
    curva_de_luz_cruda_df = tratamiento_de_datos_cometa(content)

    # Conexión con la API del MPC
    ephemeris = conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa)

    # Tratamiento de datos con efemerides
    curva_de_luz_procesada_df = tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, ephemeris)

    # Promedio movil
    curva_de_luz_interna_df = promedio_movil_minimo(curva_de_luz_procesada_df)
    
    # Curva de luz cruda.
    curva_de_luz_cruda(nombre_cometa, curva_de_luz_cruda_df, 'Envolvente_inferior')

    # Curva de luz reducida
    curva_de_luz_reducida(nombre_cometa, curva_de_luz_procesada_df, 'Envolvente_inferior')

    # Curva de luz minima
    curva_de_luz_interna(nombre_cometa, curva_de_luz_interna_df, 'Envolvente_inferior')

    # Gráfica de luz promediada
    curva_de_luz_interna_promediada(nombre_cometa, curva_de_luz_interna_df, 'Envolvente_inferior')

if __name__ == '__main__':
    envolvente_inferior()