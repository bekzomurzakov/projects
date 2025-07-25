import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output

df = px.data.gapminder()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Graphic App"),
    html.Label("Выберите страну"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Canada'
    ),

    html.Label("Выберите год"),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),

    dcc.Graph(id='indicator-graphic')
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('country-dropdown', 'value'),
    Input('year-slider', 'value'),
)
def update_graph(selected_country, selected_year):
    filtered = df[(df['country'] == selected_country) & (df['year'] == selected_year)]

    fig = px.bar(filtered, x='country', y='gdpPercap', hover_data=['pop', 'lifeExp'], color='lifeExp', labels={'gdpPercap': 'GDP'}, height=400)

    return fig

if __name__ == '__main__':
    app.run(debug=True)