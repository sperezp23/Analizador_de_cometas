# Librerías
import plotly.express as px

# Funciones
from Funciones.Crear_carpetas import crear_carpetas

def curva_de_luz_externa_promediada(nombre_cometa, curva_de_luz_externa_df):
    labels = {'obs_date':'Observation Date','promedio_movil':'Averaged reduced magnitude'}
    titulo = f'Averaged external lightcurve of {nombre_cometa}'

    # ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    fig = px.scatter(curva_de_luz_externa_df, x='obs_date', y='promedio_movil', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_traces(marker=dict(color='yellow', size=6, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_yaxes(autorange="reversed")
    # fig.write_image(ruta_archivos_graficas)
    fig.show()

if __name__ == '__main__':
    curva_de_luz_externa_promediada()
