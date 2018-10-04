#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# Hint: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
#######

# Perform imports here:
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# Take two random samples of different sizes:
a = np.random.choice(df['rings'], 30, replace=False)
b = np.random.choice(df['rings'], 20, replace=False)

# Create a data variable with two Box plots:
data = [go.Box(y=a, name='A'), go.Box(y=b, name='B')]

layout = go.Layout(title='2 Random Samples')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='box-plot-exercise.html')