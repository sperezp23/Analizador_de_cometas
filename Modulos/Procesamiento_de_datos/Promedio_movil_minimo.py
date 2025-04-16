def promedio_movil_minimo(curva_de_luz_procesada_df, numero_elementos_grupo = 9):
    curva_de_luz_interna_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').max()
    curva_de_luz_interna_df = curva_de_luz_interna_df.reset_index()

    curva_de_luz_interna_df = curva_de_luz_interna_df.copy()
    curva_de_luz_interna_df['promedio_movil'] = curva_de_luz_interna_df.magnitud_reducida.rolling(window = numero_elementos_grupo, center= True).mean()
    curva_de_luz_interna_df.dropna(inplace= True)
    return curva_de_luz_interna_df

if __name__ == '__main__':
    promedio_movil_minimo()