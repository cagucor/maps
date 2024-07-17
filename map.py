import plotly.graph_objects as go
import requests
lati = 45.50352
long = -122.58373
response = requests.get("http://localhost:8080/otp/traveltime/isochrone?batch=true&location=45.50352,%20-122.58373&time=2024-07-12T10:19:03%2B02:00&modes=WALK,TRANSIT&arriveBy=false&cutoff=15M&cutoff=30M&cutoff=45M")

fig = go.Figure(go.Scattermapbox(

    mode = "markers",
    lon = [long], lat = [lati],
    marker = {'size': 10, 'color': ["cyan"]}))

fig.update_layout(
    mapbox = {
        'style': "open-street-map",
        'center': { 'lat': lati, 'lon': long},
        'zoom': 12, 'layers': [{
            'source': response.json(), 
            'type': "fill", 'below': "traces", 'color': "royalblue"}]},
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()
