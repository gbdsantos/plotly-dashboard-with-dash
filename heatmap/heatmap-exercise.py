#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# Create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
#######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a DataFrame from "flights" data:
df = pd.read_csv('../data/flights.csv')

# Define a data variable
data = [go.Heatmap(x=df['year'], y=df['month'],
                    z=df['passengers']
                    )]

# Define a layout and figure
layout = go.Layout(title='Flights')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='heatmap-exercise.html')
