import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_mosaic
from dash_mosaic import DashMosaic
import dash_leaflet as dl
import dash_grocery
from dash_pannellum import DashPannellum
import full_calendar_component as fcc
from datetime import datetime

app = dash.Dash(__name__)

# Get today's date
today = datetime.now()

# Format the date
formatted_date = today.strftime("%Y-%m-%d")

events = [
        {
            "title": "Pip Install Python",
            "start": f"{formatted_date}",
            "end": f"{formatted_date}",
            "className": "bg-gradient-success",
            "context": "Pip Install FullCalendar",
        },
        {
            'title': 'Meeting with the boss',
            'start': f"{formatted_date}T14:30:00",
            'end': f"{formatted_date}T15:30:00",
            'className': 'bg-gradient-info',
            'context': 'Meeting with the boss',
        },
        {
            'title': 'Happy Hour',
            'start': f"{formatted_date}T17:30:00",
            'end': f"{formatted_date}T18:30:00",
            'className': 'bg-gradient-warning',
            'context': 'Happy Hour',
        },
        {
            'title': 'Dinner',
            'start': f"{formatted_date}T20:00:00",
            'end': f"{formatted_date}T21:00:00",
            'className': 'bg-gradient-danger',
            'context': 'Dinner',
        }
    ]

# Define the initial layout
initial_layout = {
    'direction': 'row',
    'first': 1,
    'second': {
        'direction': 'column',
        'first': 2,
        'second': 3,
    },
    'splitPercentage': 40,
}

# Define the content for each tile
tile_content = {
    1: DashPannellum(
        id='panorama',
        tour={
            "default": {
                "firstScene": "scene1",
                "sceneFadeDuration": 1000
            },
            "scenes": {
                "scene1": {
                    "title": "Example Panorama",
                    "hfov": 110,
                    "pitch": -3,
                    "yaw": 117,
                    "type": "equirectangular",
                    "panorama": "/assets/landscape.jpg"
                }
            }
        },
        autoLoad=True,
        width='100%',
        height='100%',
    ),
    2: html.Div([
        html.Div([
            dl.Map([dl.TileLayer(
                url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"),],
                center=[56, 10], zoom=6, style={'width': '100%', 'height': '100%'}, id="leaflet-map")
        ], id="map-wrapper", style={"width": "100%", "height": "100%", "position": "relative"})
    ], style={'height': '100vh', 'width': '100vw'}),
    3: html.Div([
        dash_grocery.ParticlesBg(type="cobweb", num=15, color="random"),
        fcc.FullCalendarComponent(
            id="api_calendar",  # Unique ID for the component
            initialView='dayGridMonth',  # dayGridMonth, timeGridWeek, timeGridDay, listWeek,
            # dayGridWeek, dayGridYear, multiMonthYear, resourceTimeline, resourceTimeGridDay, resourceTimeLineWeek
            headerToolbar={
                "left": "prev,next today",
                "center": "",
                "right": "",
            },  # Calendar header
            initialDate=f"{formatted_date}",  # Start date for calendar
            editable=True,  # Allow events to be edited
            selectable=True,  # Allow dates to be selected
            events=events,
            nowIndicator=True,  # Show current time indicator
            navLinks=True,  # Allow navigation to other dates
        )
    ], style={'height': '100%', 'width': '100%'})
}

# Define custom window titles
window_titles = {
    1: "Pannellum",
    2: "World Map",
    3: "Greeting"
}

app.layout = html.Div([
    DashMosaic(
        id='mosaic',
        layout=initial_layout,
        theme='Blueprint Dark', # Blueprint Dark, Blueprint, None
        tileContent=tile_content,
        style={'height': '95vh'},
        windowTitles=window_titles,
        showSplitButton=False, # Example: disabling the remove button
        showExpandButton=True,
        showRemoveButton=False,
        showNavbar=False
    ),
    dcc.Store(id='window-count', data=3),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('mosaic', 'layout')
)
def display_output(layout):
    return f'Current layout: {layout}'


if __name__ == '__main__':
    app.run_server(debug=True, port=9111)