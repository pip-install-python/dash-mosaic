# Dash Mosaic

Dash Mosaic is a flexible, resizable, and draggable layout component for Dash applications. It allows users to split the view into multiple panes that can be resized, rearranged, and customized.

![Dash Mosaic](https://imgur.com/yBAK6si.gif)

## Features

- Flexible layout with resizable and draggable panes
- Customizable themes (Blueprint, Blueprint Dark, None)
- Ability to add, remove, and rearrange panes
- Support for custom content in each pane
- Responsive design with mobile-friendly options

## Installation

```bash
pip install dash-mosaic
```

Go to the assets folder and copy over these files to your project's assets folder:
dash_mosaic/assets/8a26d7e1bb38c9c64a59.woff2
dash_mosaic/assets/8a525ab91769f6d60c94.ttf
dash_mosaic/assets/8b1c5e35bad17bae103e.woff2
dash_mosaic/assets/9ad9cbe47f2f5821528d.woff
dash_mosaic/assets/565ce5e4e7c8be823549.ttf
dash_mosaic/assets/3843580eab4844b48210.woff
dash_mosaic/assets/main.js
dash_mosaic/assets/style.css

## Usage
Here's a basic example of how to use the DashMosaic component:

```python
import dash
from dash import html
from dash_mosaic import DashMosaic

app = dash.Dash(__name__)

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

tile_content = {
    1: html.Div("Content for pane 1"),
    2: html.Div("Content for pane 2"),
    3: html.Div("Content for pane 3"),
}

app.layout = html.Div([
    DashMosaic(
        id='mosaic',
        layout=initial_layout,
        theme='Blueprint Dark',
        tileContent=tile_content,
        style={'height': '95vh'},
        windowTitles={1: "Pane 1", 2: "Pane 2", 3: "Pane 3"},
        showSplitButton=True,
        showExpandButton=True,
        showRemoveButton=True,
        showNavbar=True
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

Properties

- `id` (string; optional): The ID used to identify this component in Dash callbacks.
- `layout` (dict; optional): The layout configuration for the mosaic.
- `theme` (string; optional): The theme to apply to the mosaic. Options are 'Blueprint', 'Blueprint Dark', or 'None'.
- `tileContent` (dict; optional): An object containing the content for each tile, keyed by tile ID.
- `style` (dict; optional): Inline styles to apply to the mosaic container.
- `windowTitles` (dict; optional): An object containing custom titles for each window, keyed by tile ID.
- `showSplitButton` (boolean; optional): Whether to show the split button in the tile toolbar.
- `showExpandButton` (boolean; optional): Whether to show the expand button in the tile toolbar.
- `showRemoveButton` (boolean; optional): Whether to show the remove button in the tile toolbar.
- `showNavbar` (boolean; optional): Whether to show the navbar at the top of the mosaic.

## Callbacks
You can use the layout property in Dash Mosaic callbacks to show the changes in the mosaic layout. For example:
```python
@app.callback(
    Output('output', 'children'),
    Input('mosaic', 'layout')
)
def display_output(layout):
    return f'Current layout: {layout}'
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Could use help setting up assets in a way that they are automatically included in the package.