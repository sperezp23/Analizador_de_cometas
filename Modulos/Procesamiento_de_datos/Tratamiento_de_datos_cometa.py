import pandas as pd

def tratamiento_de_datos_cometa(content):
    cometa_df = pd.DataFrame(content)
    
    cometa_df['obs_method_key'] = cometa_df.obs_method.apply(
        lambda registro: registro['key'] if registro is not None and 'key' in registro else 'Dato faltante'
        )
    cometa_df['obs_date'] = pd.to_datetime(pd.to_datetime(cometa_df.obs_date).dt.date)
    cometa_df['magnitude'] = pd.to_numeric(cometa_df.magnitude)

    curva_de_luz_cruda_df = cometa_df[['obs_method_key', 'obs_date', 'magnitude']].copy()

    return curva_de_luz_cruda_df

if __name__ == '__main__':
    tratamiento_de_datos_cometa()