# Dash Mosaic

[![PyPI](https://img.shields.io/pypi/v/dash-mosaic.svg)](https://pypi.org/project/dash-mosaic/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Dash Mosaic is a powerful, flexible layout component for Dash applications that enables resizable, draggable multi-pane layouts. Built on top of [react-mosaic-component](https://github.com/nomcopter/react-mosaic-component) and integrated with [Blueprint.js](https://blueprintjs.com/), it provides an intuitive interface for organizing complex dashboards.

![Dash Mosaic Demo](https://imgur.com/yBAK6si.gif)

## Features

- **Flexible Multi-Pane Layouts** - Create sophisticated split-view interfaces with hierarchical row and column arrangements
- **Interactive Controls** - Built-in split, expand, and remove buttons for dynamic layout reconfiguration
- **Drag-to-Resize** - Intuitive drag handles between panes for resizing
- **Multiple Themes** - Choose between Blueprint (light), Blueprint Dark, or custom styling
- **Responsive Design** - Mobile-friendly with optional navbar and adaptive controls
- **Rich Content Support** - Embed any Dash components including maps, charts, calendars, and custom visualizations
- **Layout Callbacks** - Track and respond to layout changes through Dash callbacks
- **Customizable Titles** - Set custom titles for each window pane

## Installation

```bash
pip install dash-mosaic
```

### Asset Configuration

After installation, you need to copy the following files from the package assets folder to your project's assets folder:

```bash
dash_mosaic/assets/8a26d7e1bb38c9c64a59.woff2
dash_mosaic/assets/8a525ab91769f6d60c94.ttf
dash_mosaic/assets/8b1c5e35bad17bae103e.woff2
dash_mosaic/assets/9ad9cbe47f2f5821528d.woff
dash_mosaic/assets/565ce5e4e7c8be823549.ttf
dash_mosaic/assets/3843580eab4844b48210.woff
dash_mosaic/assets/main.js
dash_mosaic/assets/style.css
```

**Note:** We're working on automating this step in future releases. See [Contributing](#contributing) if you'd like to help.

## Quick Start

Here's a simple example to get you started:

```python
import dash
from dash import html
from dash_mosaic import DashMosaic

app = dash.Dash(__name__)

# Define a three-pane layout: left pane and right split into top/bottom
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

# Define content for each pane
tile_content = {
    1: html.Div("Content for pane 1", style={'padding': '20px'}),
    2: html.Div("Content for pane 2", style={'padding': '20px'}),
    3: html.Div("Content for pane 3", style={'padding': '20px'}),
}

app.layout = html.Div([
    DashMosaic(
        id='mosaic',
        layout=initial_layout,
        theme='Blueprint Dark',
        tileContent=tile_content,
        style={'height': '95vh'},
        windowTitles={1: "Left Panel", 2: "Top Right", 3: "Bottom Right"},
        showSplitButton=True,
        showExpandButton=True,
        showRemoveButton=True,
        showNavbar=True
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Layout Configuration

### Single Pane Layout

For a simple single-pane layout, just use a number:

```python
layout = 1
```

### Multi-Pane Layout

For split layouts, use a nested dictionary structure:

```python
layout = {
    'direction': 'row',           # 'row' for horizontal, 'column' for vertical split
    'first': 1,                   # Left/top pane (can be a number or nested layout)
    'second': 2,                  # Right/bottom pane (can be a number or nested layout)
    'splitPercentage': 40,        # Optional: percentage allocated to first pane (default: 50)
}
```

### Complex Nested Example

```python
layout = {
    'direction': 'row',
    'first': 1,
    'second': {
        'direction': 'column',
        'first': {
            'direction': 'row',
            'first': 2,
            'second': 3,
        },
        'second': 4,
    },
    'splitPercentage': 30,
}
```

## Component Properties

### DashMosaic

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `id` | string | - | The ID used to identify this component in Dash callbacks |
| `layout` | dict or int | - | The layout configuration (number for single pane, dict for splits) |
| `theme` | string | 'Blueprint' | Theme selection: 'Blueprint', 'Blueprint Dark', or 'None' |
| `tileContent` | dict | - | Dictionary mapping pane IDs to Dash components |
| `windowTitles` | dict | - | Dictionary mapping pane IDs to custom title strings |
| `style` | dict | - | Inline CSS styles for the mosaic container |
| `showSplitButton` | bool | True | Show/hide the split button in tile toolbar |
| `showExpandButton` | bool | True | Show/hide the expand button in tile toolbar |
| `showRemoveButton` | bool | True | Show/hide the remove button in tile toolbar |
| `showNavbar` | bool | True | Show/hide the top navbar with theme selector |
| `zeroStateView` | component | - | Component to display when layout is empty |

## Advanced Examples

### Using with Dash Leaflet Maps

```python
import dash_leaflet as dl

tile_content = {
    1: html.Div([
        dl.Map([
            dl.TileLayer(
                url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
            ),
        ], center=[56, 10], zoom=6,
           style={'width': '100%', 'height': '100%'},
           id="map")
    ], style={"width": "100%", "height": "100%", "position": "relative"})
}
```

### Tracking Layout Changes with Callbacks

```python
from dash import Output, Input

@app.callback(
    Output('output', 'children'),
    Input('mosaic', 'layout')
)
def display_output(layout):
    return f'Current layout: {layout}'
```

### Dynamic Content Updates

```python
from dash import Output, Input, State

@app.callback(
    Output('mosaic', 'tileContent'),
    Input('update-button', 'n_clicks'),
    State('mosaic', 'layout')
)
def update_content(n_clicks, current_layout):
    # Update content based on user interaction
    new_content = {
        1: html.Div(f"Updated content - Click {n_clicks}"),
        2: html.Div("Static content"),
    }
    return new_content
```

### Custom Styling

```python
app.layout = html.Div([
    DashMosaic(
        id='mosaic',
        layout=initial_layout,
        theme='None',  # Use custom CSS
        tileContent=tile_content,
        style={
            'height': '100vh',
            'backgroundColor': '#f5f5f5',
        }
    )
])
```

## Theming

Dash Mosaic supports three built-in themes:

- **Blueprint** - Clean light theme with Blueprint.js styling
- **Blueprint Dark** - Dark mode theme
- **None** - No built-in styling (use your own CSS)

Change themes dynamically through the navbar dropdown or programmatically via the `theme` prop.

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/pip-install-python/dash-mosaic.git
cd dash-mosaic

# Install Python dependencies
pip install dash>=2.0.0

# Install Node dependencies
npm install

# Start development server
npm start
```

### Build Process

```bash
# Build JavaScript bundle
npm run build:js

# Generate Python/R/Julia bindings
npm run build:backends

# Full build (both JS and bindings)
npm run build
```

### Running Tests

```bash
pytest
```

## Contributing

Contributions are welcome! Here are some areas where we'd especially appreciate help:

- **Automated Asset Inclusion** - Help automate the asset copying process during installation
- **Additional Examples** - Create examples with different visualization libraries
- **Documentation** - Improve API documentation and tutorials
- **Testing** - Expand test coverage

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Reporting Issues

If you encounter bugs or have feature requests, please [open an issue](https://github.com/pip-install-python/dash-mosaic/issues) on GitHub.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

- Built on [react-mosaic-component](https://github.com/nomcopter/react-mosaic-component) by Palantir
- UI components from [Blueprint.js](https://blueprintjs.com/)
- Created with [Dash Component Boilerplate](https://github.com/plotly/dash-component-boilerplate)

## Resources

- **Documentation:** [GitHub Wiki](https://github.com/pip-install-python/dash-mosaic)
- **Examples:** See `usage.py` for a complete example
- **Dash Documentation:** https://dash.plotly.com/
- **React Mosaic:** https://github.com/nomcopter/react-mosaic-component

## Support

For questions and support:
- Open an [issue](https://github.com/pip-install-python/dash-mosaic/issues) on GitHub
- Check existing issues for solutions
- Review the `usage.py` example file

---

Built with by [Pip Install Python](https://github.com/pip-install-python)