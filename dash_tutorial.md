# Dash

## Introduction

Dash is python library for creating interactive visualizaiton and reports, which enables createing web application without knowing fron-end languages like HTML, CSS and JavaScript. Projects created using Dash can be then easyli deployed in cloud (e.g. Heroku).

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

If we put code from above into file and name it `app.py`, we can run application localy by running following command in terminal:
```
$ python app.py
 * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
```
Your application will be on following address `http://127.0.0.1:8050/`

### Exercise

Copy example code to `app.py` file and edit it so that there is y-axis name is `passenger class`.

## `Dash` components

`Dash` app can be buld from the objects contained in 2 libarries  - `dash_html_components` and `dash_core_components`.

### HTML components

`dash_html_components` contains objects wrapping different HTML tags, e.g. `html.Div()` (section element) a
`html.H1()` (big header).

*Note*: in this tutorial we will import `dash_html_components` as abbreviation: `import dash_html_components as html`

### Exercise

Add paragraph(`html.P`) containing following text `Data description here` right after header.
 

 
## `Dash` core components

`Dash` contains objects enabling easy obsahuje funkce, které dovolují jednoduše vytvářet interaktivní objekty, například grafy, interaktivní tabulky, možnosti volby a markdown.

Imporobjects using following code: `import dash_core_components as dcc`.

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
        {'label': 'Možnost A', 'value': 'val_a'},
        {'label': 'Možnost B', 'value': 'val_b'},
    ],
    value='val_a'
)
```
`label` má hodnotu, která se zobrazí ne webové stránce, `value` je hodnota, která může být použitá pro rozhodování v programu.

*Note*: pokud chete vyzkoušet výše uvedený kód, uložte ho do samostatného souboru a spusťte pomocí příkazu `python <nazev_vaseho_souboru.py>`.


Příklad přepínače - můžete vybrat jednu z hodnot:

```python
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'Tato možnost', 'value': 'variant1'},
        {'label': 'Nebo tato', 'value': 'variant2'}
    ],
    value='variant'
)
```

Další možnosti jsou [tady](https://plot.ly/dash/dash-core-components).


### Exercise

Do své aplikace přidejte výběrové pole s možnostmi: 'Cena lístků podle třídy' a 'Věk cestujících podle třídy' (hodnoty 'fare_class' a 'age_class').
Poté přijdete přepínač s možnostmi: 'Histogram' a 'Boxplot' (hodnoty 'hist' a 'boxplot').

## Decorators

Dekorátor je funkce, která obaluje jinou funkci. V našem případě se jedná o `@app.callback`, který říká, že pokud se vstup do této funkce změní, má se zavolat funkce, která je definována níže.

Here is an example

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
    return 'Napsali jste "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()

```
Pokud napíšeme cokoliv do okénka (`dcc.Input`), změní se vstupní data do `@app.callback` (`Input(component_id='input-text', component_property='value')`). Proto se zavolá funkce a `html.Div` s id `display-text` zobrazí text, který jsme zadali do okénka, protože tak je definována funkce `update_output_div`.
 
### Exercise

Upravte výše uvedený kod:
1. Vložte nadpis (`html.H1`) před `dcc.Input` a pojmenujte jeho id 'big-title'.
2. Předělejte `@app.callback` aby aktualizoval nadpis, ne `html.Div`.
3. Předělejte funkci `update_output_div` na `update_output_h1` aby vracela 'Zprava dne:' a text, který jste zadali.


## Rozhodování na základě vstupních hodnot

Následující kód bere jako vstupní hodnotu typ grafu vybrany uživatelem a na zakladě ní vykreslí histogram nebo boxplot.
`update_figure` dostane jako první parametr vybranou hodnotu přepinače (její `value`). V `@app.callback` lze definovat i více vstupů, proto je `Input` zapsán jako prvek seznamu. Hodnoty `Input` dostane funkce ve stejném pořadí jako `@app.callback`.

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
        Data o Titaniku
    '''),

    dcc.Graph(
        id='example-graph',
    ),
    dcc.Dropdown(
        id = 'dropdown-input',
        options=[
            {'label': 'Cena listků podle třídy', 'value': 'fare_class'},
            {'label': 'Věk cestujících podle třídy', 'value': 'age_class'},
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
    trace1 = plot_function(x = first_fare, opacity = 0.75, name = 'První třída')
    trace2 = plot_function(x = second_fare, opacity = 0.75, name = 'Druhá třída')
    trace3 = plot_function(x = third_fare, opacity = 0.75, name = 'Třetí třída')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {
            'title': 'Cena jízdenky dle třídy jizdenky',
        },

    }
    return figure

titanic = pd.read_excel('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls')

if __name__ == '__main__':
    app.run_server()

```

### Exercise

Upravte předchozí příklad; přidejte rozhodování na základě výběrového pole. 

- Pokud uživatel vybere "Cena listků podle třídy" (`fare_class`), zobrazí se histogram nebo boxplot cen lístků dle tříd - tak, jak už je v příkladu. 
- Pokud uživatel vybere "Věk cestujících podle třídy" (`age_class`), zobrazí se histogram nebo boxplot věku cestujících dle tříd.

## Deployment

See [official tutorial](https://plot.ly/dash/deployment) from plotly.
