# Librerías
from numpy import log10

def procesar_datos_con_efemerides(curva_de_luz_cruda_df, efemerides_df, perihelio, beta = 0):
    
    # Unión de las bases de datos COBS y MPC
    curva_de_luz_procesada_df = curva_de_luz_cruda_df.merge(efemerides_df, on='obs_date')

    # Reducción de la magnitud aparente
    curva_de_luz_procesada_df['magnitud_reducida'] = (
        curva_de_luz_cruda_df['magnitude'] 
        - 5 * log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
        - (beta * curva_de_luz_procesada_df['phase'])
        )
    
    # Calculo del Delta t
    curva_de_luz_procesada_df['delta_t'] = (curva_de_luz_procesada_df.obs_date - perihelio) # type: ignore
    curva_de_luz_procesada_df['delta_t'] = curva_de_luz_procesada_df.delta_t.dt.days
    
    return curva_de_luz_procesada_df

if __name__ == '__main__':
    procesar_datos_con_efemerides()
