import pandas as pd
import plotly.express as px

data = pd.read_csv('tesla.csv', sep=',')

fig = px.line(data, x="date", y="price", markers=True)
fig.update_layout(
    title=f'Price of {data_name}', title_font_size=20, title_x=0.5,
    xaxis_title='Date', xaxis_title_font_size=16, xaxis_tickfont_size=14,
    yaxis_title='Price', yaxis_title_font_size=16, yaxis_tickfont_size=14,
    height=700,
    margin=dict(l=0, r=0, t=40, b=0),
)
# 5.1
fig.update_traces(
    line_color="crimson",
    marker=dict(size=12, line=dict(width=2, color='black'), color='white',),
)
# 5.2
fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='ivory')
fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='ivory')

fig.show()
