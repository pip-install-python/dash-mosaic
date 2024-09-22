% Auto-generated: do not edit by hand
\name{dashMosaic}

\alias{dashMosaic}

\title{DashMosaic component}

\description{
DashMosaic is a component that provides a flexible, resizable, and draggable layout for organizing content. It allows users to split the view into multiple panes that can be resized, rearranged, and customized.
}

\usage{
dashMosaic(id=NULL, layout=NULL, onChange=NULL, onRelease=NULL,
renderTile=NULL, resize=NULL, showExpandButton=NULL,
showNavbar=NULL, showRemoveButton=NULL,
showSplitButton=NULL, style=NULL, theme=NULL,
tileContent=NULL, windowTitles=NULL, zeroStateView=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{layout}{Named list. The layout configuration for the mosaic. It defines the structure and arrangement of the panes.}

\item{onChange}{Callback function that is called when the layout changes.}

\item{onRelease}{Callback function that is called when the user releases a tile after dragging.}

\item{renderTile}{A function that renders the content of each tile. It receives the tile ID and path as arguments.}

\item{resize}{Named list. Object containing resize-related options for the mosaic.}

\item{showExpandButton}{Logical. Whether to show the expand button in the tile toolbar.}

\item{showNavbar}{Logical. Whether to show the navbar at the top of the mosaic.}

\item{showRemoveButton}{Logical. Whether to show the remove button in the tile toolbar.}

\item{showSplitButton}{Logical. Whether to show the split button in the tile toolbar.}

\item{style}{Named list. Inline styles to apply to the mosaic container.}

\item{theme}{A value equal to: "blueprint", "blueprint dark", "none". The theme to apply to the mosaic. Options are 'Blueprint', 'Blueprint Dark', or 'None'.}

\item{tileContent}{List with named elements and values of type a list of or a singular dash component, string or number. An object containing the content for each tile, keyed by tile ID.}

\item{windowTitles}{List with named elements and values of type character. An object containing custom titles for each window, keyed by tile ID.}

\item{zeroStateView}{Dash component. The component to display when there are no tiles (zero state).}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

