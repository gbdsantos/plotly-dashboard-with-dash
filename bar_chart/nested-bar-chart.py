import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/2018WinterOlympics.csv')

trace1 = go.Bar(x=df['NOC'], y=df['Gold'],
                name='Gold',
                marker={'color':'#FFD700'}
                )

trace2 = go.Bar(x=df['NOC'], y=df['Silver'],
                name='Silver',
                marker={'color':'#9EA0A1'}
                )

trace3 = go.Bar(x=df['NOC'], y=df['Bronze'],
                name='Bronze',
                marker={'color':'#CD7F32'}
                )

data = [trace1, trace2, trace3]
#data = [go.Bar(x=df['NOC'], y=df['Total'])]
layout = go.Layout(title='Medals')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='nested-bar-char.html')
