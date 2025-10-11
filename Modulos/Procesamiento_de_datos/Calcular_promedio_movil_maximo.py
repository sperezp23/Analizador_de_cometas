def calcular_promedio_movil_maximo(curva_de_luz_procesada_df: object, numero_elementos_grupo: int = 7) -> object:
    '''
    Calcula la curva de luz externa del cometa. Primero agrupando los datos por fecha, y tomando el valor mínimo de magnitud reducida.
    Luego, calcula el promedio móvil de la magnitud reducida con una ventana centrada del tamaño especificado por numero_elementos_grupo.

    Retorna: DataFrame con la curva de luz externa del cometa.
    '''
    curva_de_luz_externa_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').min()
    curva_de_luz_externa_df = curva_de_luz_externa_df.reset_index()

    curva_de_luz_externa_df = curva_de_luz_externa_df.copy()
    curva_de_luz_externa_df['promedio_movil'] = curva_de_luz_externa_df.magnitud_reducida.rolling(window = numero_elementos_grupo, center= True).mean()
    curva_de_luz_externa_df.dropna(inplace= True)
    
    return curva_de_luz_externa_df

if __name__ == '__main__':
    calcular_promedio_movil_maximo()