import dash.dependencies
import dash_html_components as html
import dash_core_components as dcc
import os
import pandas as pd
import plotly.graph_objs as go



app = dash.Dash()
my_css_url = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
app.css.append_css({
    "external_url": my_css_url
})
server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'xyz')


migration_data = pd.read_csv('migration.csv')

app.layout = html.Div(children=[
	dcc.Markdown('''# Worldwide migration'''),
	html.Div(html.Label('''Choose country/region'''), style={'display': 'inline-block', 'vertical-align': 'middle',
				   'textAlign': 'center', 'font-size': '1.6em',
		}),
		html.Div([

			dcc.Dropdown(
			id='choice',
			options=[{'label': item, 'value': item} for item in migration_data[migration_data.columns[1]]],
			value='Czechia'
		)], style={'display': 'inline-block', 'vertical-align': 'middle',
				   'textAlign': 'center', 'font-size': '1.6em', 'width': '40%'
		}),
	html.Div(html.Label('Click on the data to see detailed results'), style={'font-size': '1.7em'}),
	dcc.Graph(
			id='country-graph',
			clickData={'points': [{'x': 'Syrian Arab Republic'}]},
			figure={
				'data': [],
				'layout': {
					'title': ''
				}
			}
	),
	dcc.Graph(
			id='year-graph',
			figure={
				'data': [],
				'layout': {
					'title': ''
				}
			}
	),
dcc.Markdown('''
*Source:* [International migrant stock: The 2017 revision](http://www.un.org/en/development/desa/population/migration/data/estimates2/estimates17.shtml)
    '''),
], style={'textAlign': 'center'})



@app.callback(
	dash.dependencies.Output(component_id='country-graph', component_property='figure'),
	[dash.dependencies.Input(component_id='choice', component_property='value')],
)
def update_country_graph(choice):
	country_data = migration_data.loc[migration_data['Major area, region, country or area of destination'] == choice]
	country_data_2017 = country_data.loc[country_data['Year'] == 2017]
	country_data_2017 = country_data_2017.transpose()
	country_data_2017.drop(country_data_2017.index[0:4], inplace=True)
	country_data_2017.sort_values(country_data_2017.columns[0], inplace=True, ascending=False)
	country_data_2017 = country_data_2017.loc[country_data_2017[country_data_2017.columns[0]].notnull()]
	trace = go.Bar(
		x=country_data_2017.index,
		y=country_data_2017[country_data_2017.columns[0]],
		marker=dict(color='#7fc97f')
	)
	data = [trace]

	layout = go.Layout(
		title='Number of migrants in {0} in 2017 by country of origin'.format(choice),
		xaxis=dict(
			tickangle=60),
	)
	figure = dict(data=data, layout=layout)

	return figure

@app.callback(
	dash.dependencies.Output(component_id='year-graph', component_property='figure'),
	[dash.dependencies.Input(component_id='choice', component_property='value'),
	 dash.dependencies.Input(component_id='country-graph', component_property='clickData')
	 ],
)
def update_country_graph(choice, clickData):
	country_data = migration_data.loc[migration_data['Major area, region, country or area of destination'] == choice]
	country_data_year = country_data.loc[:, ['Year', clickData['points'][0]['x']]]
	country_data_year.fillna(value=0, inplace=True)
	trace = go.Scatter(
		x=country_data_year[country_data_year.columns[0]],
		y=country_data_year[country_data_year.columns[1]],
		marker=dict(color='#fdc086'),
	)

	layout = go.Layout(
		title='Number of migrants from {0} to {1} in 1990-2017'.format(clickData['points'][0]['x'], choice),
		showlegend=False,
		xaxis=dict(
			title="Year"),
	)

	data = [trace]
	figure = dict(data=data, layout=layout)

	return figure

if __name__ == '__main__':
	app.run_server()
