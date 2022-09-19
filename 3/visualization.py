import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

DATA_NAME = 'Google'


def load_data():
    return pd.read_csv('google.csv', sep=',')


def task_1_2():
    print('\nTask #2')
    data = load_data()
    print(data.info())
    print(data.head())
    print(data.isna().sum())


def task_3():
    print('\nTask #3')
    data = load_data()
    # 3.1
    data = [go.Bar(
        x=data['Date'],
        y=data['Close']
    )]
    fig = go.Figure(data=data)
    # 3.2
    # idk what they want from me
    # 3.3
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    fig.update_layout(
        # 3.4
        title=f'Price of {DATA_NAME}', title_font_size=20, title_x=0.5,
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


def task_4():
    print('\nTask #4')
    data = load_data()
    trace = go.Pie(
        labels=data['Date'],
        values=data['Close']
    )
    fig = go.Figure(data=trace)
    fig.update_layout(
        title=f'Price of {DATA_NAME}', title_font_size=20, title_x=0.5,
        height=700,
        margin=dict(l=0, r=0, t=40, b=0),
    )
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    fig.show()


def task_5():
    print('\nTask #5')
    data = load_data()
    fig = px.line(data, x="Date", y="Close", markers=True)
    fig.update_layout(
        title=f'Price of {DATA_NAME}', title_font_size=20, title_x=0.5,
        xaxis_title='Date', xaxis_title_font_size=16, xaxis_tickfont_size=14,
        yaxis_title='Price', yaxis_title_font_size=16, yaxis_tickfont_size=14,
        height=700,
        margin=dict(l=0, r=0, t=40, b=0),
    )
    # 5.1
    fig.update_traces(
        line_color="crimson",
        marker=dict(size=12, line=dict(width=2, color='black'), color='white', ),
    )
    # 5.2
    fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='ivory')
    fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='ivory')
    fig.show()


def main():
    task_1_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
