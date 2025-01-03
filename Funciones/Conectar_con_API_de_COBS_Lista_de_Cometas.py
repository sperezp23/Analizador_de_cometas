# Librerías
import requests

# Función
def conectar_con_API_de_COBS_Lista_de_Cometas(conectado_a_internet: bool) -> object:
    '''
    Realiza la conexión con la API de COBS para generar la lista de nombres registrados. Retorna un objeto tipo Json.
    '''

    Link_cops_API = 'https://cobs.si/api/comet_list.api'

    if conectado_a_internet:
        print(f'⌛ Conectando con la base de datos [COBS lista de Cometas].')
        response = requests.get(Link_cops_API)

        if response.status_code == 200:
            content = response.json()
            print('✅ Base de datos actualizada [COBS lista de Cometas].')

        else:
            print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response.status_code}\n{response.content}')

    return content

if __name__ == '__main__':
    conectar_con_API_de_COBS_Lista_de_Cometas()