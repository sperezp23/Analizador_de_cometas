# Gráfica de luz promediada
import plotly.graph_objects as go

# Funciones
from Modulos.Visualizacion_de_datos.Crear_carpetas import crear_carpetas

def curvas_de_luz_interna_externa(nombre_cometa, curva_de_luz_externa_df, curva_de_luz_interna_df):
    titulo = f'Max/Min Averaged Lightcurve of comet {nombre_cometa}'
    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=curva_de_luz_externa_df.delta_t, y=curva_de_luz_externa_df.promedio_movil, mode='markers', name='Envolvente', marker=dict(color='yellow', line=dict(width=1, color='DarkSlateGrey'))))
    fig.add_trace(go.Scatter(x=curva_de_luz_interna_df.delta_t, y=curva_de_luz_interna_df.promedio_movil, mode='markers', name='Núcleo', marker=dict(color='red', line=dict(width=1, color='DarkSlateGrey'))))
    fig.update_layout(template='plotly_dark')
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(template='plotly_dark', xaxis_title='t-Δt', yaxis_title='Reduced Magnitude', title = titulo)
    fig.write_image(ruta_archivos_graficas, width = 1500, height = 700)
    fig.write_html(ruta_archivos_graficas.replace('png', 'html'))
    # fig.show()

    print('✅ Creada: curva de luz Interna-Externa.')

if __name__ == '__main__':
    curvas_de_luz_interna_externa()