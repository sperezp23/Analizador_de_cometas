# Librerías
import plotly.express as px

from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def crear_curvas_de_luz(nombre_cometa, variable_x, variable_y, data_frame, titulo, promediada = False, color = 'obs_method_key'):

    # Crear carpetas
    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    variable_a_graficar = list(variable_y.keys())[0]

    labels = {
        'obs_date':'Observation Date',
        'delta_t':'t-Tq',
        # 'obs_method_key' : 'Observation Method',
    }

    labels.update(variable_y)

    if not promediada: 

        fig = px.scatter(data_frame, x= variable_x, y= variable_a_graficar,
            # color= color,
            template= 'plotly_dark', labels= labels,
            title= titulo)

    elif promediada: 

        fig = px.scatter(data_frame, x= variable_x, y= variable_a_graficar, 
            template= 'plotly_dark', labels= labels, title= titulo)

        fig.update_traces(marker=dict(color= color, size=6, line=dict(width=1, color='DarkSlateGrey')))

    fig.update_yaxes(autorange="reversed")
    fig.write_image(ruta_archivos_graficas, width = 1500, height = 700)
    fig.write_html(ruta_archivos_graficas.replace('png', 'html'))
    # fig.show()

    if __name__ == '__main__':
        crear_curvas_de_luz()
