import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('tesla.csv', sep=',')

trace = go.Pie(
    labels=data['date'],
    values=data['price']
)
fig = go.Figure(data=trace)
fig.update_layout(
    title=f'Price of {data_name}', title_font_size=20, title_x=0.5,
    height=700,
    margin=dict(l=0, r=0, t=40, b=0),
)
fig.update_traces(marker=dict(line=dict(color='black', width=2)))
fig.show()
