def promedio_movil_maximo(curva_de_luz_procesada_df, numero_elementos_grupo = 7):
    curva_de_luz_externa_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').min()
    curva_de_luz_externa_df = curva_de_luz_externa_df.reset_index()

    curva_de_luz_externa_df = curva_de_luz_externa_df.copy()
    curva_de_luz_externa_df['promedio_movil'] = curva_de_luz_externa_df.magnitud_reducida.rolling(window = numero_elementos_grupo, center= True).mean()
    curva_de_luz_externa_df.dropna(inplace= True)
    return curva_de_luz_externa_df

if __name__ == '__main__':
    promedio_movil_maximo()