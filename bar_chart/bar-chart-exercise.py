#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels. Extra credit: make a horizontal bar chart
#######

# Perfom impors here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/mocksurvey.csv', index_col=0)

# Create traces using a list comprehension:
data = [go.Bar(x=df.index, y=df[response], name=response) for
        response in df.columns
        ]
# Create a Layout, remember to set the barmode here
layout = go.Layout(title='Survey Results', barmode='stack')
figure = go.Figure(data=data, layout=layout)

pyo.plot(figure, filename='bar-chart-exercise.html')

