# Librerías
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

# Funciones
from Modulos.Crear_carpetas.Crear_carpetas import crear_carpetas

def crear_curva_de_fase(nombre_cometa, variable_x, variable_y, data_frame, titulo):

    # Crear carpetas
    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    variable_a_graficar = list(variable_y.keys())[0]
    labels = {
        'phase':'Phase'
    }

    labels.update(variable_y)

    plt.title(titulo)
    plt.xlabel('Phase')
    plt.ylabel(list(variable_y.values())[0])
    plt.grid(True)

    sns.scatterplot(data=data_frame, x=variable_x, y=variable_a_graficar, color='#049dfc', 
            size=4, legend=False, edgecolor='#0227FA', linewidth=0.5)

    fig = px.scatter(data_frame, x= variable_x, y= variable_a_graficar,
        template= 'plotly_dark', labels= labels, title= titulo)

    plt.savefig(ruta_archivos_graficas.replace('html', 'png'), dpi=300)
    print(f'✅ Grafica estática: {titulo} creada.')
    plt.show()

    fig.write_html(ruta_archivos_graficas.replace('png', 'html'))
    print(f'✅ Grafica interactiva: {titulo} creada.')

    if __name__ == '__main__':
        crear_curva_de_fase()
