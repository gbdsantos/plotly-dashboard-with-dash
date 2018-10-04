#######
# Objetive: Using the iris dataset, develop a Distplot
# that compares the petal lenghts of each class.
# File: '../data/iris.csv'
# Fields 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'
#######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')

#Define traces
# HINT:
# This grabs the petal_length column for a particular flower
trace0 = df[df['class']=='Iris-setosa']['petal_length']
trace1 = df[df['class']=='Iris-versicolor']['petal_length']
trace2 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
hist_data = [trace0, trace1, trace2]
group_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-versicolor']

# Create a figure from data and layout, and plot the figure
figure = ff.create_distplot(hist_data, group_labels)
pyo.plot(figure, filename='distplot-exercise.html')
