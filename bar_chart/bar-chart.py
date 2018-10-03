import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/2018WinterOlympics.csv')

data = [go.Bar(x=df['NOC'], y=df['Total'])]
layout = go.Layout(title='Medals')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='bar-char.html')
