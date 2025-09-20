# Gráfica de luz promediada
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Funciones
from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def curvas_de_luz_interna_externa(nombre_cometa, curva_de_luz_externa_df, curva_de_luz_interna_df):

    titulo = f'Max/Min Averaged Lightcurve of comet {nombre_cometa} data from COBS'
    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    _, ax = plt.subplots()

    sns.scatterplot(data=curva_de_luz_externa_df, x='delta_t', y='promedio_movil', ax=ax,  color='#FFF200', edgecolor='#000000',  label='Envolvente', linewidth=0.5, s=17)
    sns.scatterplot(data=curva_de_luz_interna_df, x='delta_t', y='promedio_movil', ax=ax, color='red', edgecolor='#AF0000', label='Nucleo', linewidth=0.5, s=17)
    
    ax.invert_yaxis()   
    ax.set_title(titulo)
    ax.set_xlabel('t-Tq [days]')
    ax.set_ylabel('Average m(1,1,0)')
    ax.legend()
    ax.grid(True)

    # Guardar la imagen
    plt.savefig(ruta_archivos_graficas.replace('html', 'png'), dpi=300)

    # Mostrar el gráfico
    plt.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=curva_de_luz_externa_df.delta_t, y=curva_de_luz_externa_df.promedio_movil, mode='markers', name='Envolvente', marker=dict(color='yellow', line=dict(width=1, color='DarkSlateGrey'))))
    fig.add_trace(go.Scatter(x=curva_de_luz_interna_df.delta_t, y=curva_de_luz_interna_df.promedio_movil, mode='markers', name='Núcleo', marker=dict(color='red', line=dict(width=1, color='DarkSlateGrey'))))
    fig.update_layout(template='plotly_dark')
    fig.update_yaxes(autorange='reversed')
    fig.update_layout(template='plotly_dark', xaxis_title='t-Tq', yaxis_title=' Average m(1,1,0)', title = titulo)
    
    fig.write_html(ruta_archivos_graficas)

    print('✅ Creada: curva de luz Interna-Externa.')

if __name__ == '__main__':
    curvas_de_luz_interna_externa()