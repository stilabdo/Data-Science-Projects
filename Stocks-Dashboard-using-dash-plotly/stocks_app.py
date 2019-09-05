import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dateutil.relativedelta import relativedelta
import pandas as pd
import plotly.graph_objs as go



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([

    html.Div([
        html.H2("Stock App"),
        html.Img(src="/assets/Stock-Market.png")
    ], className='banner'),

    html.Div([
        html.Div([
            dcc.Input(
                id='stock-input',
                value='FB',
                type='text'
            ),
            html.Button(id='submit-button', n_clicks=0, children='Submit')
        ]),
        html.Div([
            dcc.Graph(
                id='graph_close',
            )
        ]),        
    ])
])

@app.callback(
    dash.dependencies.Output('graph_close', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('stock-input', 'value')]
    )
def update_fig(n_clicks, input_value):
    df = pd.read_csv('E:\Jupyter\Python Learning files\Machine Learning\Time Series\stocks.csv')
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    input_stock = input_value
    df = df[df['Name'] == input_stock]

    trace_line = go.Scatter(x=list(df.index),
                                y=list(df.close),
                                name="Close",
                                showlegend=False)

    trace_candle = go.Candlestick(x=df.index,
                           open=df.open,
                           high=df.high,
                           low=df.low,
                           close=df.close,
                           visible=False,
                           showlegend=False)

    trace_bar = go.Ohlc(x=df.index,
                           open=df.open,
                           high=df.high,
                           low=df.low,
                           close=df.close,
                           visible=False,
                           showlegend=False)

    data = [trace_line, trace_candle, trace_bar]

    updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Line',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False]}],
                    label='Candle',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True]}],
                    label='Bar',
                    method='update'
                ),
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),
    ])

    layout = dict(
        title=input_value,
        updatemenus=updatemenus,
        autosize=False,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                         label='YTD',
                         step='year',
                         stepmode='todate'),
                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )

    return {
        "data": data,
        "layout": layout
    }
if __name__ == "__main__":
    app.run_server(debug=True)    