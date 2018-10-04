import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

# Multiple Heat Maps with subplots
df0 = pd.read_csv('../data/2010SitkaAK.csv')
df1 = pd.read_csv('../data/2010SantaBarbaraCA.csv')
df2 = pd.read_csv('../data/2010YumaAZ.csv')

trace0 = go.Heatmap(x=df0['DAY'], y=df0['LST_TIME'],
                    z=df0['T_HR_AVG'], colorscale='Jet',
                    zmin=5, zmax=40
                    )

trace1 = go.Heatmap(x=df1['DAY'], y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'], colorscale='Jet',
                    zmin=5, zmax=40
                    )

trace2 = go.Heatmap(x=df2['DAY'], y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'], colorscale='Jet',
                    zmin=5, zmax=40
                    )

figure = tools.make_subplots(rows=1, cols=3, subplot_titles=['Sitka AK', 'SB CA', 'Yuma AZ'],
                             shared_yaxes=True
                             )

figure.append_trace(trace0, 1, 1)
figure.append_trace(trace1, 1, 2)
figure.append_trace(trace2, 1, 3)

figure['layout'].update(title='Temps for 3 cities')

pyo.plot(figure, filename='heatmap-2.html')
