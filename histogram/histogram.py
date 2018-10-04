import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=10))]

layout = go.Layout(title="Histogram")
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='histogram.html')