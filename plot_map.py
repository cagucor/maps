from dash import Dash, dcc, html, Input, Output
import dash_leaflet as dl
import json
import requests

app = Dash()
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "height": "100vh"
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.H3("Latitude"),
        html.Div(
            id='lat'
        ),
        html.H3("Longitude"),
        html.Div(
            id='lon'
        ),
        html.Div([
            dcc.Slider(15, 60, 15,
            value=15,
            id='my-slider'
        ),
        html.Div(id='slider-output-container')
])
    ],
    style=SIDEBAR_STYLE,
)

maindiv = html.Div(
    dl.Map(
            id='map',
            children=[
                dl.TileLayer()
            ],
            center=[-33.862, 151.208],
            zoom=11,
            style=CONTENT_STYLE
    ),
)

app.layout = html.Div([sidebar, maindiv])

@app.callback(
    Output('slider-output-container', 'children'),
    Input('my-slider', 'value'))
def update_output(value):
    return '"{}" minutes'.format(value)

@app.callback(
    Output('lat', 'children'),
    Output('lon', 'children'),
    Output('map', 'children'),
    Input('map', 'clickData'),
    prevent_initial_call=True
)
def do(click_data):
    # extract coordinates form click_data
    coordinates = click_data['latlng']
    lat, lon = coordinates.values()

    return round(lat,4), round(lon,4), [dl.TileLayer(), dl.Marker(position=[lat, lon])]


if __name__ == '__main__':
    app.run(debug=True)
