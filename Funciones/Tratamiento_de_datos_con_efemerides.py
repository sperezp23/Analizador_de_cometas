# Librerías
import numpy as np

def tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, efemerides_filtrada_df, perihelio):
    
    # Unión de las bases de datos COBS y MPC
    curva_de_luz_procesada_df = curva_de_luz_cruda_df.merge(efemerides_filtrada_df, on='obs_date')

    # Reducción de la magnitud aparente
    beta = 0

    curva_de_luz_procesada_df['magnitud_reducida'] = (
        curva_de_luz_cruda_df['magnitude'] 
        - 5 * np.log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
        - (beta * curva_de_luz_procesada_df['phase'])
        )
    
    # Calculo del Delta t
    curva_de_luz_procesada_df['delta_t'] = (curva_de_luz_procesada_df.obs_date - perihelio) # type: ignore
    curva_de_luz_procesada_df['delta_t'] = curva_de_luz_procesada_df.delta_t.dt.days
    return curva_de_luz_procesada_df

if __name__ == '__main__':
    tratamiento_de_datos_con_efemerides()
