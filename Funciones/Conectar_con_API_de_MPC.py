import pandas as pd
from math import ceil
from astroquery.mpc import MPC

def conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa):
    efemerides_total = []

    fecha_inicial = curva_de_luz_cruda_df.obs_date.min()
    fecha_final = curva_de_luz_cruda_df.obs_date.max()
    fechas = (fecha_final - fecha_inicial).days + 1

    print('⌛ Conectando con la base de datos [MPC efemerides].')
    for i in range(ceil(fechas/1441)):
        efemerides = MPC.get_ephemeris(nombre_cometa, start = str(fecha_inicial), number = 1441)
        efemerides_ciclo_df = efemerides.to_pandas()
        efemerides_total.append(efemerides_ciclo_df)
    
        fecha_inicial = efemerides_ciclo_df.Date.max()

    # Creación del data frame efemerides filtrada
    efemerides_df = pd.concat(efemerides_total)
    efemerides_df.columns = efemerides_df.columns.str.lower().str.replace(' ', '_')

    efemerides_filtrada_df = efemerides_df[['date', 'delta','r', 'phase']].copy()
    efemerides_filtrada_df = efemerides_filtrada_df.rename(columns = {'date':'obs_date'})
    efemerides_filtrada_df['obs_date'] = pd.to_datetime(pd.to_datetime(efemerides_filtrada_df.obs_date).dt.date)
    efemerides_filtrada_df.reset_index(inplace = True)

    print('✅ Base de datos actualizada [MPC efemerides].')
    return efemerides_filtrada_df

if __name__ == '__main__':
    conectar_con_API_de_MPC()