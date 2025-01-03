# Librerías
import requests

def conectar_con_API_de_COBS_Observaciones(nombre_cometa: str, fecha_inicial: str, conectado_a_internet: bool) -> object:
    '''
    Realiza la conexión con la API de COBS para generar la lista de observaciones. Retorna un objeto tipo Json.
    '''
    
    try:
        Link_cops_API_pagina_1 = f'https://cobs.si/api/obs_list.api?des={nombre_cometa}&format=json&from_date={fecha_inicial} 00:00&page=1&exclude_faint=False&exclude_not_accurate=False'

        if conectado_a_internet:
            print(f'⌛ Conectando con la base de datos [COBS Observaciones].')
            response_pagina_1 = requests.get(Link_cops_API_pagina_1)

            if response_pagina_1.status_code == 200:
                content_pagina_1 = response_pagina_1.json()
                numero_de_paginas = int(content_pagina_1['info']['pages'])

                content = content_pagina_1['objects']

                for pagina in range(2, numero_de_paginas + 1):
                    Link_cops_API_pagina = f'https://cobs.si/api/obs_list.api?des={nombre_cometa}&format=json&from_date={fecha_inicial}&page={pagina}&exclude_faint=False&exclude_not_accurate=False'
                    response_pagina = requests.get(Link_cops_API_pagina)
                    content_pagina = response_pagina.json()
                    content.extend(content_pagina['objects'])

                print('✅ Base de datos actualizada [COBS Observaciones].')
                return content
            
    except:
        print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response_pagina.status_code}\n{response_pagina.content}')

if __name__ == '__main__':
    conectar_con_API_de_COBS_Observaciones()
