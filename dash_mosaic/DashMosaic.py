# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashMosaic(Component):
    """A DashMosaic component.
DashMosaic is a component that provides a flexible, resizable, and draggable layout for organizing content.
It allows users to split the view into multiple panes that can be resized, rearranged, and customized.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- layout (dict; default {    direction: 'row',    first: 1,    second: {        direction: 'column',        first: 2,        second: 3,    },    splitPercentage: 40,}):
    The layout configuration for the mosaic. It defines the structure
    and arrangement of the panes.

- resize (dict; optional):
    Object containing resize-related options for the mosaic.

- showExpandButton (boolean; default True):
    Whether to show the expand button in the tile toolbar.

- showNavbar (boolean; default True):
    Whether to show the navbar at the top of the mosaic.

- showRemoveButton (boolean; default True):
    Whether to show the remove button in the tile toolbar.

- showSplitButton (boolean; default True):
    Whether to show the split button in the tile toolbar.

- style (dict; optional):
    Inline styles to apply to the mosaic container.

- theme (a value equal to: "Blueprint", "Blueprint Dark", "None"; default 'Blueprint'):
    The theme to apply to the mosaic. Options are 'Blueprint',
    'Blueprint Dark', or 'None'.

- tileContent (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    An object containing the content for each tile, keyed by tile ID.

- windowTitles (dict with strings as keys and values of type string; optional):
    An object containing custom titles for each window, keyed by tile
    ID.

- zeroStateView (dash component; optional):
    The component to display when there are no tiles (zero state)."""
    _children_props = ['zeroStateView', 'tileContent{}']
    _base_nodes = ['zeroStateView', 'children']
    _namespace = 'dash_mosaic'
    _type = 'DashMosaic'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, layout=Component.UNDEFINED, theme=Component.UNDEFINED, renderTile=Component.UNDEFINED, zeroStateView=Component.UNDEFINED, onChange=Component.UNDEFINED, onRelease=Component.UNDEFINED, resize=Component.UNDEFINED, tileContent=Component.UNDEFINED, style=Component.UNDEFINED, windowTitles=Component.UNDEFINED, showSplitButton=Component.UNDEFINED, showExpandButton=Component.UNDEFINED, showRemoveButton=Component.UNDEFINED, showNavbar=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'layout', 'resize', 'showExpandButton', 'showNavbar', 'showRemoveButton', 'showSplitButton', 'style', 'theme', 'tileContent', 'windowTitles', 'zeroStateView']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'layout', 'resize', 'showExpandButton', 'showNavbar', 'showRemoveButton', 'showSplitButton', 'style', 'theme', 'tileContent', 'windowTitles', 'zeroStateView']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashMosaic, self).__init__(**args)
