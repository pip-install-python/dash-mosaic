# AUTO GENERATED FILE - DO NOT EDIT

export dashmosaic

"""
    dashmosaic(;kwargs...)

A DashMosaic component.
DashMosaic is a component that provides a flexible, resizable, and draggable layout for organizing content.
It allows users to split the view into multiple panes that can be resized, rearranged, and customized.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `layout` (Dict; optional): The layout configuration for the mosaic. It defines the structure and arrangement of the panes.
- `resize` (Dict; optional): Object containing resize-related options for the mosaic.
- `showExpandButton` (Bool; optional): Whether to show the expand button in the tile toolbar.
- `showNavbar` (Bool; optional): Whether to show the navbar at the top of the mosaic.
- `showRemoveButton` (Bool; optional): Whether to show the remove button in the tile toolbar.
- `showSplitButton` (Bool; optional): Whether to show the split button in the tile toolbar.
- `style` (Dict; optional): Inline styles to apply to the mosaic container.
- `theme` (a value equal to: "Blueprint", "Blueprint Dark", "None"; optional): The theme to apply to the mosaic. Options are 'Blueprint', 'Blueprint Dark', or 'None'.
- `tileContent` (Dict with Strings as keys and values of type a list of or a singular dash component, string or number; optional): An object containing the content for each tile, keyed by tile ID.
- `windowTitles` (Dict with Strings as keys and values of type String; optional): An object containing custom titles for each window, keyed by tile ID.
- `zeroStateView` (dash component; optional): The component to display when there are no tiles (zero state).
"""
function dashmosaic(; kwargs...)
        available_props = Symbol[:id, :layout, :resize, :showExpandButton, :showNavbar, :showRemoveButton, :showSplitButton, :style, :theme, :tileContent, :windowTitles, :zeroStateView]
        wild_props = Symbol[]
        return Component("dashmosaic", "DashMosaic", "dash_mosaic", available_props, wild_props; kwargs...)
end

