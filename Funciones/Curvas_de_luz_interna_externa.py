# Gráfica de luz promediada
import plotly.graph_objects as go

def curvas_de_luz_interna_externa(nombre_cometa, curva_de_luz_externa_v2_df, curva_de_luz_interna_v2_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=curva_de_luz_externa_v2_df.obs_date, y=curva_de_luz_externa_v2_df.promedio_movil, mode='markers', name='Envolvente', marker=dict(color='yellow', line=dict(width=1, color='DarkSlateGrey'))))
    fig.add_trace(go.Scatter(x=curva_de_luz_interna_v2_df.obs_date, y=curva_de_luz_interna_v2_df.promedio_movil, mode='markers', name='Núcleo', marker=dict(color='red', line=dict(width=1, color='DarkSlateGrey'))))
    fig.update_layout(template='plotly_dark')
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(template='plotly_dark', xaxis_title='Observation Date', yaxis_title='Averaged Magnitude', title = f'Max/Min Averaged Lightcurve of comet {nombre_cometa}')
    fig.show()