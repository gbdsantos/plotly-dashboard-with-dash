#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
#######

# Perform imports here
import pandas as pd
import plotly.offline as go
import plotly.graph_objs as pyo

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# Create data by choosing fields for x, y and marker size attributes
data = go.Scatter(x=df['displacement'], y=df['acceleration'],
                  text=df['name'],
                  mode='markers',
                  marker=dict(size=df['weight']/400))

# Create a Layout  with a title and axis labels
layout = go.Layout(title='My Bubble Solution', hovermode='closest')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='bubble-chart-exercise.html')
# Create


