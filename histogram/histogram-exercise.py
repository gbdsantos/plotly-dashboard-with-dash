#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset(../data/abalone.csv)
# Set the range from 0 to 1, with a bin size of 0.02
#######

#Perfom imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# Create a data variable
data = [go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))]

# Add a layout and Create a figure from data & layout, and plot the figure
layout = go.Layout(title="Histogram")
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='histogram.html')