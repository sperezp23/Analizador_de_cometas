# Librerías
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

# Funciones
from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def crear_curvas_de_luz(nombre_cometa, variable_x, variable_y, data_frame, titulo, promediada = False, color = None):

    # Crear carpetas
    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    variable_a_graficar = list(variable_y.keys())[0]

    labels = {
        'obs_date':'Observation Date',
        'delta_t':'t-Tq'
    }

    labels.update(variable_y)

    plt.gca().invert_yaxis()  # Invertir el eje y
    plt.title(titulo)
    plt.xlabel('t-Tq [days]')
    plt.ylabel(list(variable_y.values())[0])
    plt.grid(True)

    if not promediada:
        sns.scatterplot(data=data_frame, x=variable_x, y=variable_a_graficar, color="#049dfc", 
                size=4, legend=False, edgecolor="#0227FA", linewidth=0.5)

        fig = px.scatter(data_frame, x= variable_x, y= variable_a_graficar,
            template= 'plotly_dark', labels= labels,
            title= titulo)

    elif promediada:
        sns.scatterplot(data=data_frame, x=variable_x, y=variable_a_graficar, color=color, 
        size=6, legend=False, edgecolor="#000000", linewidth=0.5)

        fig = px.scatter(data_frame, x= variable_x, y= variable_a_graficar, 
            template= 'plotly_dark', labels= labels, title= titulo)

        fig.update_traces(marker=dict(color= color, size=6, line=dict(width=1, color='DarkSlateGrey')))

    fig.update_yaxes(autorange="reversed")

    plt.savefig(ruta_archivos_graficas.replace('html', 'png'), dpi=300)
    plt.show()

    fig.write_html(ruta_archivos_graficas.replace('png', 'html'))

    if __name__ == '__main__':
        crear_curvas_de_luz()
