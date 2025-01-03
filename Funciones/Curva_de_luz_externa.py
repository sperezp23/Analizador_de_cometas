# Librerías
import plotly.express as px

# Funciones
from Funciones.Crear_carpetas import crear_carpetas

def curva_de_luz_externa(nombre_cometa, curva_de_luz_externa_df):
    labels = {'obs_date':'Observation Date','promedio_movil':'Maximum averaged reduced magnitude', 'obs_method_key' : 'Observation Method'}
    titulo = f'External lightcurve of {nombre_cometa}'

    # ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    fig = px.scatter(curva_de_luz_externa_df, x='obs_date', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    # fig.write_image(ruta_archivos_graficas)
    fig.show()

if __name__ == '__main__':
    curva_de_luz_externa()
