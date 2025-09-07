# Librerías
import os
from pathlib import Path
from datetime import date

def crear_carpetas(nombre_cometa, nombre_archivo=None, carpeta_base='Graficas', tipo_archivo = 'png') -> str:
    fecha_actual = str(date.today())
    carpeta_cometa = Path(carpeta_base, nombre_cometa.replace('/', '_'))
    carpeta_fecha = Path(carpeta_cometa, fecha_actual)

    if not os.path.exists(carpeta_base):
        Path.mkdir(carpeta_base)

    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    if not os.path.exists(carpeta_fecha):
        Path.mkdir(carpeta_fecha)

    aux = nombre_archivo.replace('/', '_')
    return f'{carpeta_fecha}/{aux}__{fecha_actual}.{tipo_archivo}'

if __name__ == '__main__':
    crear_carpetas()
