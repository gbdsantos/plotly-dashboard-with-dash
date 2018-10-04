import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#df = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df = pd.read_csv('../data/2010YumaAZ.csv')

print(df)
print(df.columns)

data = [go.Heatmap(x=df['DAY'], y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist(),
                   colorscale='Jet')]

layout = go.Layout(title='SB CA Temps')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='heatmap.html')
