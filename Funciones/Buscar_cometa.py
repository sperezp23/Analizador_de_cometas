# Librerías
import pandas as pd

# Funciones
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Conectar_con_API_de_COBS_Lista_de_Cometas import conectar_con_API_de_COBS_Lista_de_Cometas

def buscar_cometa(cometa_buscado: str) -> None:
    '''
    Busca el cometa ingresado ó, coincidencias aproximadas del mismo.
    '''

    conectado_a_internet = verificar_conexion()
    cometas_hallados = []
    content = conectar_con_API_de_COBS_Lista_de_Cometas(conectado_a_internet)

    cometas_df = pd.DataFrame(content['objects'])
    lista_cometas_df = cometas_df[['name', 'fullname']]
    cometas_hallados =  lista_cometas_df.name[lista_cometas_df.fullname.str.contains(cometa_buscado)].values

    if len(cometas_hallados) == 0:
        print(f'🛑 No hay coincidencias para: {cometa_buscado}, en la base de datos (COBS).')
    
    else:
        aux = '\n'*2
        print(f'✅ Coincidencias halladas:{aux}{cometas_hallados}')

if __name__ == '__main__':
    buscar_cometa()
