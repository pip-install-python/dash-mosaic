# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashMosaic <- function(id=NULL, layout=NULL, onChange=NULL, onRelease=NULL, renderTile=NULL, resize=NULL, showExpandButton=NULL, showNavbar=NULL, showRemoveButton=NULL, showSplitButton=NULL, style=NULL, theme=NULL, tileContent=NULL, windowTitles=NULL, zeroStateView=NULL) {
    
    props <- list(id=id, layout=layout, onChange=onChange, onRelease=onRelease, renderTile=renderTile, resize=resize, showExpandButton=showExpandButton, showNavbar=showNavbar, showRemoveButton=showRemoveButton, showSplitButton=showSplitButton, style=style, theme=theme, tileContent=tileContent, windowTitles=windowTitles, zeroStateView=zeroStateView)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMosaic',
        namespace = 'dash_mosaic',
        propNames = c('id', 'layout', 'onChange', 'onRelease', 'renderTile', 'resize', 'showExpandButton', 'showNavbar', 'showRemoveButton', 'showSplitButton', 'style', 'theme', 'tileContent', 'windowTitles', 'zeroStateView'),
        package = 'dashMosaic'
        )

    structure(component, class = c('dash_component', 'list'))
}
