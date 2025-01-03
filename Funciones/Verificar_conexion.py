# Librerías
import requests

def verificar_conexion() -> None:
    try:
        requests.get("http://www.google.com", timeout=5)
        print(f'{'\n'*2}✅ Conectado a internet.\n{'-'*40}')
        return True
    
    except requests.ConnectionError:
        print('🛑 Sin conexión a internet.')
        return False

if __name__ == '__main__':
    verificar_conexion()