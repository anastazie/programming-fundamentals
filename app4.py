import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

titanic = pd.read_excel('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Titanic data
    '''),
    dcc.Dropdown(
        id = 'dropdown-input',
        options=[
            {'label': 'Ticket price by passengers class', 'value': 'fare_class'},
            {'label': 'Age by passengers class', 'value': 'age_class'},
        ],
        value='fare_class'
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Histogram', 'value': 'hist'},
            {'label': 'Boxplot', 'value': 'boxplot'}
        ],
        value='hist',
        id='radio-input'
    ),
    dcc.Graph(
        id='example-graph',
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='radio-input', component_property='value'),
    Input(component_id='dropdown-input', component_property='value')]
)
def update_figure(plot_type, plot_data):
    if plot_data == 'fare_class':
        first = titanic[titanic.pclass == 1].fare
        second = titanic[titanic.pclass == 2].fare
        third = titanic[titanic.pclass == 3].fare
        title = "Ticket price based on passenger's class"
    else:
        first = titanic[titanic.pclass == 1].age
        second = titanic[titanic.pclass == 2].age
        third = titanic[titanic.pclass == 3].age
        title = "Age by passengers class"

    if plot_type == 'hist':
        plot_function = go.Histogram
    else:
        plot_function = go.Box

    trace1 = plot_function(x = first, opacity = 0.75, name = 'First class')
    trace2 = plot_function(x = second, opacity = 0.75, name = 'Second class')
    trace3 = plot_function(x = third, opacity = 0.75, name = 'Third class')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {
            'title': title,
        },

    }
    return figure



if __name__ == '__main__':
    app.run_server(debug=True)
