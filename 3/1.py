import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv('data.csv', sep=',')
print('Task #2: info')
print(data.info())
print('\nTask #2: head')
print(data.head())
print('\nTask #2: clear')
print(data.isna().sum())

print('\nTask #3')
# 3.1
data = [go.Bar(
    x=data['date'],
    y=data['price']
)]
fig = go.Figure(data=data)

# 3.2
# ?????????????????????????????????

# 3.3
fig.update_traces(marker=dict(line=dict(color='black', width=2)))

fig.update_layout(
    # 3.4
    title='Price of gold', title_font_size=20, title_x=0.5,
    # 3.5 & 3.6
    xaxis_title='Date', xaxis_title_font_size=16, xaxis_tickfont_size=14,
    yaxis_title='Price', yaxis_title_font_size=16, yaxis_tickfont_size=14,
    # 3.7
    height=700,
    # 3.8
    margin=dict(l=0, r=0, t=40, b=0),
)

# 3.5
fig.update_xaxes(tickangle=315)

fig.show()
