"""
Dash Mosaic - Comprehensive Usage Example

This example demonstrates the key features of Dash Mosaic including:
- Multi-pane layouts with nested splits
- Interactive charts and data visualizations
- Real-time data updates
- Layout change tracking
- Theme switching
- Dynamic content updates
"""

import dash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
from dash_mosaic import DashMosaic
from datetime import datetime, timedelta
import numpy as np

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Sample data for visualizations
def generate_time_series():
    """Generate sample time series data"""
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    values = np.cumsum(np.random.randn(30)) + 100
    return dates, values

def create_line_chart():
    """Create an interactive line chart"""
    dates, values = generate_time_series()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=values,
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=6)
    ))
    fig.update_layout(
        title='Revenue Trend (Last 30 Days)',
        xaxis_title='Date',
        yaxis_title='Revenue ($)',
        template='plotly_white',
        hovermode='x unified',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_bar_chart():
    """Create a bar chart"""
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    values = [45, 62, 38, 51, 29]
    colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6']

    fig = go.Figure(data=[
        go.Bar(x=categories, y=values, marker_color=colors, text=values, textposition='auto')
    ])
    fig.update_layout(
        title='Sales by Product',
        xaxis_title='Product',
        yaxis_title='Units Sold',
        template='plotly_white',
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_pie_chart():
    """Create a pie chart"""
    labels = ['Desktop', 'Mobile', 'Tablet', 'Other']
    values = [42, 35, 18, 5]
    colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444']

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors),
        hole=0.4
    )])
    fig.update_layout(
        title='Traffic by Device Type',
        template='plotly_white',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def create_stats_card(title, value, change, icon="📊"):
    """Create a statistics card"""
    change_color = '#10b981' if change >= 0 else '#ef4444'
    change_symbol = '+' if change >= 0 else ''

    return html.Div([
        html.Div([
            html.Span(icon, style={'fontSize': '48px', 'marginBottom': '10px'}),
            html.H3(title, style={'margin': '10px 0', 'color': '#6b7280'}),
            html.H1(value, style={'margin': '10px 0', 'fontSize': '36px', 'fontWeight': 'bold'}),
            html.Div([
                html.Span(f'{change_symbol}{change}%',
                         style={'color': change_color, 'fontWeight': 'bold', 'fontSize': '18px'}),
                html.Span(' vs last month', style={'color': '#9ca3af', 'marginLeft': '8px'})
            ])
        ], style={
            'textAlign': 'center',
            'padding': '40px',
            'height': '100%',
            'display': 'flex',
            'flexDirection': 'column',
            'justifyContent': 'center',
            'backgroundColor': '#ffffff',
            'borderRadius': '8px'
        })
    ], style={'height': '100%', 'padding': '10px'})

# Define the initial layout - 4 panes with nested splits
initial_layout = {
    'direction': 'column',
    'first': {
        'direction': 'row',
        'first': 1,
        'second': 2,
        'splitPercentage': 50,
    },
    'second': {
        'direction': 'row',
        'first': 3,
        'second': 4,
        'splitPercentage': 50,
    },
    'splitPercentage': 40,
}

# Define content for each tile with rich visualizations
tile_content = {
    1: html.Div([
        dcc.Graph(
            id='line-chart',
            figure=create_line_chart(),
            style={'height': '100%'},
            config={'displayModeBar': False}
        )
    ], style={'height': '100%', 'padding': '10px'}),

    2: html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=create_bar_chart(),
            style={'height': '100%'},
            config={'displayModeBar': False}
        )
    ], style={'height': '100%', 'padding': '10px'}),

    3: html.Div([
        dcc.Graph(
            id='pie-chart',
            figure=create_pie_chart(),
            style={'height': '100%'},
            config={'displayModeBar': False}
        )
    ], style={'height': '100%', 'padding': '10px'}),

    4: html.Div([
        html.Div([
            create_stats_card("Total Revenue", "$45,231", 12.5, "💰"),
            html.Div(style={'height': '20px'}),
            create_stats_card("Active Users", "8,282", 8.2, "👥"),
            html.Div(style={'height': '20px'}),
            create_stats_card("Conversion Rate", "3.24%", -2.1, "📈"),
        ], style={'padding': '10px'})
    ], style={'height': '100%', 'overflowY': 'auto', 'backgroundColor': '#f9fafb'}),
}

# Define custom window titles
window_titles = {
    1: "Revenue Analytics",
    2: "Product Performance",
    3: "Traffic Sources",
    4: "Key Metrics"
}

# Main app layout
app.layout = html.Div([
    html.Div([
        html.H1("Dash Mosaic Dashboard", style={
            'margin': '0',
            'fontSize': '24px',
            'fontWeight': 'bold',
            'color': '#1f2937'
        }),
        html.P("Interactive multi-pane layout demonstration", style={
            'margin': '5px 0 0 0',
            'color': '#6b7280',
            'fontSize': '14px'
        }),
    ], style={
        'padding': '20px 20px 10px 20px',
        'backgroundColor': '#ffffff',
        'borderBottom': '1px solid #e5e7eb'
    }),

    DashMosaic(
        id='mosaic',
        layout=initial_layout,
        theme='Blueprint Dark',
        tileContent=tile_content,
        style={'height': '90vh'},
        windowTitles=window_titles,
        showSplitButton=True,
        showExpandButton=True,
        showRemoveButton=True,
        showNavbar=True
    ),

    # Hidden div to store layout changes
    html.Div(id='layout-info', style={
        'padding': '10px 20px',
        'backgroundColor': '#f3f4f6',
        'borderTop': '1px solid #e5e7eb',
        'fontSize': '12px',
        'color': '#6b7280',
        'fontFamily': 'monospace'
    }),

    # Interval component for live updates (optional)
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # Update every 10 seconds
        n_intervals=0,
        disabled=True  # Set to False to enable live updates
    ),
], style={
    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    'backgroundColor': '#f9fafb',
    'minHeight': '100vh'
})

@app.callback(
    Output('layout-info', 'children'),
    Input('mosaic', 'layout')
)
def display_layout_info(layout):
    """Display information about the current layout"""
    if layout is None:
        return "Layout: Not initialized"

    # Count number of panes
    def count_panes(layout_obj):
        if isinstance(layout_obj, (int, str)):
            return 1
        return count_panes(layout_obj.get('first', 0)) + count_panes(layout_obj.get('second', 0))

    pane_count = count_panes(layout)
    timestamp = datetime.now().strftime("%H:%M:%S")

    return html.Div([
        html.Span(f"📐 Active Panes: {pane_count} | ", style={'marginRight': '10px'}),
        html.Span(f"🕐 Last Updated: {timestamp} | ", style={'marginRight': '10px'}),
        html.Span("💡 Tip: Drag the borders to resize panes, use toolbar buttons to split/expand/remove")
    ])

@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    Input('interval-component', 'n_intervals')
)
def update_charts(n):
    """Update charts with new data (when interval is enabled)"""
    return create_line_chart(), create_bar_chart(), create_pie_chart()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Dash Mosaic Example Application")
    print("="*60)
    print("\n📊 Features demonstrated:")
    print("  • Multi-pane resizable layout")
    print("  • Interactive Plotly charts")
    print("  • Dynamic statistics cards")
    print("  • Layout change tracking")
    print("  • Theme switching via navbar")
    print("\n🌐 Opening browser at http://127.0.0.1:8050")
    print("="*60 + "\n")

    app.run(debug=True, port=8040)