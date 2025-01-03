# Librerías
import plotly.express as px

# Funciones
from Funciones.Crear_carpetas import crear_carpetas

def curva_de_luz_interna(nombre_cometa, curva_de_luz_externa_df):
    labels = {'delta_t':'t-Δt','promedio_movil':'Minimum averaged reduced magnitude', 'obs_method_key' : 'Observation Method'}
    titulo = f'Minimum averaged reduced internal lightcurve of {nombre_cometa}'

    # ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    fig = px.scatter(curva_de_luz_externa_df, x='delta_t', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    # fig.write_image(ruta_archivos_graficas)
    fig.show()

    print('✅ Creada: curva de luz interna.')

if __name__ == '__main__':
    curva_de_luz_interna()
