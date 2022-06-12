# 'dataset' tem os dados de entrada para este script
import pandas as pd
import plotly.express as px

df_agua_tratada_pais_pandas = pd.DataFrame(dataset)
df_agua_tratada_pais_pandas.sort_values(by=['ANOS'], inplace=True)

fig = px.choropleth(
    df_agua_tratada_pais_pandas, 
    locations = "CODIGO",
    color = "POPULACAO_USANDO_AGUA_POTAVEL",
    hover_name = "PAIS",
    color_continuous_scale = px.colors.sequential.Plasma,
    animation_frame = 'ANOS',
    animation_group = 'PAIS',
    range_color = [0, 100]
)

fig.show()