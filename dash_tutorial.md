# Dash

## Introduction

Dash is python library for creating interactive visualizaiton and reports, which enables creating web application without knowing front-end languages like HTML, CSS and JavaScript. Projects created using Dash can be then easily deployed in cloud (e.g. Heroku).

[Official tutorials](https://plot.ly/dash/).

In order to create Dash application, we need to import `dash` libraries (`dash`, `dash_core_components`, `dash_html_components`). Here is an example of simple application:
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Titanic data
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Bar(x = [1, 2, 3], y = [4, 1, 2], name ='Cherbourg'),
                go.Bar(x = [1, 2, 3], y = [2, 4, 5], name = 'Queenstown'),
                go.Bar(x = [1, 2, 3], y = [3, 2, 3], name = 'Southampton')
            ],
            'layout': {
                'title': 'Port of embarkation'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
```

If we put code from above into file and name it `app.py`, we can run application locally by running following command in terminal:
```
$ python app.py
 * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
```
Your application will be on following address `http://127.0.0.1:8050/`

### Exercise

Copy example code to `app.py` file and edit it so that there is y-axis name is `passenger class`.

*Note*: If you want to run example code, save it to file and then run it in terminal using following command `python filename.py`.

## `Dash` components

`Dash` app can be build from the objects contained in 2 libraries  - `dash_html_components` and `dash_core_components`.

### HTML components

`dash_html_components` contains objects wrapping different HTML tags, e.g. `html.Div()` (section element) a
`html.H1()` (big header).

*Note*: in this tutorial we will import `dash_html_components` as abbreviation: `import dash_html_components as html`

### Exercise

Add paragraph(`html.P`) containing following text `Data description here` right after header.



## `Dash` core components

Using `Dash` library you can easily create interactive objects, such as plot, dropdown, date range slider and much more.

Import library using following code: `import dash_core_components as dcc`.

Instead of HTML paragraphs we can use markdown:

```python
import dash_core_components as dcc

dcc.Markdown('''
#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
''')
```

### Exercise

Using `dcc.Markdown` add link to [data description](https://www.kaggle.com/c/titanic/data) to `html.Div`, delete `html.P`.

### Dropdown

Here is example of dropdown

```python
import dash_core_components as dcc


dcc.Dropdown(
    options=[
        {'label': 'Variant A', 'value': 'val_a'},
        {'label': 'Variant B', 'value': 'val_b'},
    ],
    value='val_a'
)
```
`label` is Name which will be displayed on the web site, `value` is option name that can be used later in code.
In the given example `Variant A` is default value selected in dropdown



Radio item example, default selected value is `Variant 1`

```python
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'Variant 1', 'value': 'variant1'},
        {'label': 'Variant 2', 'value': 'variant2'}
    ],
    value='variant1'
)
```

More information about library [here](https://plot.ly/dash/dash-core-components).


### Exercise

Add to your application code dropdown menu with following options: 'Ticket price by passengers class' and 'Age by passengers class', (values 'fare_class' and 'age_class', respectively).
Then add radio button with following labels: 'Histogram' and 'Boxplot' (values 'hist' and 'boxplot', respectively).

## Decorators

Decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. In this tutorial, we will use `@app.callback` decorator. Whenever an input property changes (here it is `value` property of `input-text` component), the function that the callback decorator wraps (here it is `update_output_div`) will get called automatically.

```python
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-text', value='initial value', type="text"),
    html.Div(id='display-text')
])

@app.callback(
    Output(component_id='display-text', component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)
def update_output_div(input_value):
    return 'You wrote: "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()

```
Whenever we write something to input window (`dcc.Input`) it fill fire `@app.callback` function (`Input(component_id='input-text', component_property='value')`), which subsequently will call `update_output_div` with updated value of parameter `input value` producing different output that will be displayed in `html.Div` with id `display-text`.

### Exercise

Edit example code:
1. Add header (`html.H1`) before `dcc.Input` with `big-title` id
2. Edit `@app.callback` function so that it updates header and not `html.Div`
3. Rename `update_output_div` to `update_output_h1` to return following text 'Today's news:' and text from the input.


## Deciding based on input values

Following code takes plot type as an input value and based on selected value will show either histogram or boxplot.
`update_figure` function will get selected radio button value as first parameter. In `@app.callback` multiple inputs can be defined (that is why inputs are in list) and only one Output. Decorated function will get parameters in the same order as inputs were defined in `app.callback`.

```python
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Titanic data
    '''),

    dcc.Graph(
        id='example-graph',
    ),
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
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='radio-input', component_property='value')]
)
def update_figure(plot_type):
    first_fare = titanic[titanic.pclass == 1].fare
    second_fare = titanic[titanic.pclass == 2].fare
    third_fare = titanic[titanic.pclass == 3].fare

    plot_function = go.Histogram if plot_type == 'hist' else go.Box
    trace1 = plot_function(x = first_fare, opacity = 0.75, name = 'First class')
    trace2 = plot_function(x = second_fare, opacity = 0.75, name = 'Second class')
    trace3 = plot_function(x = third_fare, opacity = 0.75, name = 'Third class')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {
            'title': 'Ticket price based on passenger's class',
        },

    }
    return figure

titanic = pd.read_excel('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls')

if __name__ == '__main__':
    app.run_server()

```

### Exercise

Edit following code so that different plots are shown based on dropdown value


- If user selects 'Ticket price by passengers class' (`fare_class`), histogram or boxplot of ticket price is shown
- If user selects 'Age by passengers class' (`age_class`), histogram or boxplot of age is shown

## Deployment

See [official tutorial](https://plot.ly/dash/deployment) from plotly.
