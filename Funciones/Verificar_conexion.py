# Librerías
import requests

def verificar_conexion():
    try:
        requests.get("http://www.google.com", timeout=5)
        aux = ('\n'*2, '-'*40)
        print(f'{aux[0]}✅ Conectado a internet.\n{aux[1]}')
        return True
    
    except requests.ConnectionError:
        print('🛑 Sin conexión a internet.')
        return False

if __name__ == '__main__':
    verificar_conexion()
