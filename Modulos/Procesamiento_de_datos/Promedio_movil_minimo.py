def promedio_movil_minimo(curva_de_luz_procesada_df: object, numero_elementos_grupo: int = 9) -> object:
    '''
    Calcula la curva de luz interna del cometa. Primero agrupando los datos por fecha, y tomando el valor maximo de magnitud reducida.
    Luego, calcula el promedio móvil de la magnitud reducida con una ventana centrada del tamaño especificado por numero_elementos_grupo.

    Retorna: DataFrame con la curva de luz interna del cometa.
    '''

    curva_de_luz_interna_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').max()
    curva_de_luz_interna_df = curva_de_luz_interna_df.reset_index()

    curva_de_luz_interna_df = curva_de_luz_interna_df.copy()
    curva_de_luz_interna_df['promedio_movil'] = curva_de_luz_interna_df.magnitud_reducida.rolling(window = numero_elementos_grupo, center= True).mean()
    curva_de_luz_interna_df.dropna(inplace= True)
    return curva_de_luz_interna_df

if __name__ == '__main__':
    promedio_movil_minimo()