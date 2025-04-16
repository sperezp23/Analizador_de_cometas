# Librerías
import plotly.express as px

def crear_curvas_de_luz(variable, data_frame, titulo, promediada = False, color = 'obs_method_key'):
    
    variable_a_graficar = list(variable.keys())[0]

    labels = {
        'obs_date':'Observation Date',
        'obs_method_key' : 'Observation Method',
    }

    labels.update(variable)

    if not promediada: 

        fig = px.scatter(data_frame, x='obs_date', y= variable_a_graficar,
            color= color, template= 'plotly_dark', labels= labels,
            title= titulo)

    elif promediada: 

        fig = px.scatter(data_frame, x='obs_date', y= variable_a_graficar, 
            template= 'plotly_dark', labels= labels, title= titulo)

        fig.update_traces(marker=dict(color= color, size=6, line=dict(width=1, color='DarkSlateGrey')))

    fig.update_yaxes(autorange="reversed")
    fig.show()

    if __name__ == '__main__':
        crear_curvas_de_luz()
