import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../data/mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'], text=df['name'],
                   mode='markers',
                   #marker=dict(size=2*df['cylinders']))]
                    marker=dict(size=df['weight']/100,
                                color=df['cylinders'],
                                showscale=True))] #Scale Color Bar
layout = go.Layout(title='Bubble Chart', hovermode='closest') #parameters: x, closest
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='bubble-chart.html')