# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class DashMosaic(Component):
    """A DashMosaic component.
DashMosaic is a component that provides a flexible, resizable, and draggable layout for organizing content.
It allows users to split the view into multiple panes that can be resized, rearranged, and customized.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- layout (dict | number; default {    direction: 'row',    first: 1,    second: {        direction: 'column',        first: 2,        second: 3,    },    splitPercentage: 40,}):
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
    _children_props: typing.List[str] = ['zeroStateView', 'tileContent{}']
    _base_nodes = ['zeroStateView', 'children']
    _namespace = 'dash_mosaic'
    _type = 'DashMosaic'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        layout: typing.Optional[typing.Union[dict, NumberType]] = None,
        theme: typing.Optional[Literal["Blueprint", "Blueprint Dark", "None"]] = None,
        renderTile: typing.Optional[typing.Any] = None,
        zeroStateView: typing.Optional[Component] = None,
        onChange: typing.Optional[typing.Any] = None,
        onRelease: typing.Optional[typing.Any] = None,
        resize: typing.Optional[dict] = None,
        tileContent: typing.Optional[typing.Dict[typing.Union[str, float, int], ComponentType]] = None,
        style: typing.Optional[typing.Any] = None,
        windowTitles: typing.Optional[typing.Dict[typing.Union[str, float, int], str]] = None,
        showSplitButton: typing.Optional[bool] = None,
        showExpandButton: typing.Optional[bool] = None,
        showRemoveButton: typing.Optional[bool] = None,
        showNavbar: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'layout', 'resize', 'showExpandButton', 'showNavbar', 'showRemoveButton', 'showSplitButton', 'style', 'theme', 'tileContent', 'windowTitles', 'zeroStateView']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'layout', 'resize', 'showExpandButton', 'showNavbar', 'showRemoveButton', 'showSplitButton', 'style', 'theme', 'tileContent', 'windowTitles', 'zeroStateView']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashMosaic, self).__init__(**args)

setattr(DashMosaic, "__init__", _explicitize_args(DashMosaic.__init__))
