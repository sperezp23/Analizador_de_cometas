# Librerías
import pandas as pd

# Funciones
from Funciones.Conectar_con_API_de_COBS_Lista_de_Cometas import conectar_con_API_de_COBS_Lista_de_Cometas

def verificar_cometa(cometa_buscado, conectado_a_internet):
    content = conectar_con_API_de_COBS_Lista_de_Cometas(conectado_a_internet)

    cometas_df = pd.DataFrame(content['objects'])
    lista_cometas_df = cometas_df['name']

    if cometa_buscado in lista_cometas_df.to_list():
        print(f'✅ Cometa hallado: {cometa_buscado}')
        return True
    
    else:
        print(f'🛑 El cometa buscado, {cometa_buscado}, no se encuentra en la base de datos.')
        return False

if __name__ == '__main__':
    verificar_cometa()