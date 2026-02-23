# Librerías
from numpy import log10

def procesar_datos_con_efemerides(curva_de_luz_cruda_df, efemerides_df, perihelio, beta):
    
    # Unión de las bases de datos COBS y MPC
    curva_de_luz_procesada_df = curva_de_luz_cruda_df.merge(efemerides_df, on='obs_date')

    # Reducción de la magnitud aparente sin la fase
    curva_de_luz_procesada_df['magnitud_reducida'] = (
        curva_de_luz_cruda_df['magnitude'] 
        - 5 * log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
        )
    
    # Reducción de la magnitud aparente con la fase
    curva_de_luz_procesada_df['magnitud_reducida_con_fase'] = (
        curva_de_luz_cruda_df['magnitude'] 
        - 5 * log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
        - 1.0 * (beta * curva_de_luz_procesada_df['phase'])
        )
    
    # Calculo del Delta t
    curva_de_luz_procesada_df['delta_t'] = (curva_de_luz_procesada_df.obs_date - perihelio) # type: ignore
    curva_de_luz_procesada_df['delta_t'] = curva_de_luz_procesada_df.delta_t.dt.days
    
    return curva_de_luz_procesada_df

if __name__ == '__main__':
    procesar_datos_con_efemerides()
