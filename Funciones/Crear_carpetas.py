# Librerías
import os
from pathlib import Path
from datetime import date

def crear_carpetas(nombre_cometa, titulo):
    fecha_actual = str(date.today())
    carpeta_cometa = Path('Graficas', nombre_cometa.replace('/', '_'))
    carpeta_fecha = Path(carpeta_cometa, fecha_actual)

    if not os.path.exists('Graficas'):
        Path.mkdir('Graficas')

    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    if not os.path.exists(carpeta_fecha):
        Path.mkdir(carpeta_fecha)

    aux = titulo.replace('/', '_')
    return f'{carpeta_fecha}/{aux}__{fecha_actual}.png'

if __name__ == '__main__':
    crear_carpetas()
