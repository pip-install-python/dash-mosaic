import React from 'react';
import PropTypes from 'prop-types';
import {
    Mosaic,
    MosaicWindow,
    MosaicZeroState,
    getLeaves,
    updateTree,
    getNodeAtPath,
    getOtherDirection,
    getPathToCorner,
    Corner,
    createBalancedTreeFromLeaves,
    MosaicContext,
} from 'react-mosaic-component';
import { Classes, HTMLSelect, Button, Icon } from '@blueprintjs/core';
import { IconNames } from '@blueprintjs/icons';
import classNames from 'classnames';
import dropRight from 'lodash/dropRight';

import './assets/style.css';

const THEMES = {
    ['Blueprint']: 'mosaic-blueprint-theme',
    'Blueprint Dark': classNames('mosaic-blueprint-theme', 'bp3-dark'),
    ['None']: '',
};


/**
 * DashMosaic is a component that provides a flexible, resizable, and draggable layout for organizing content.
 * It allows users to split the view into multiple panes that can be resized, rearranged, and customized.
 */
const DashMosaic = (props) => {
    const {
        id,
        layout,
        theme,
        renderTile,
        zeroStateView,
        onChange,
        onRelease,
        resize,
        setProps,
        tileContent,
        style,
        windowTitles,
        showSplitButton,
        showExpandButton,
        showRemoveButton,
        showNavbar
    } = props;

    const handleChange = (newNode) => {
        onChange(newNode);
        setProps({ layout: newNode });
    };

    const handleRelease = (newNode) => {
        onRelease(newNode);
        console.log('Mosaic.onRelease():', newNode);
    };

    const autoArrange = () => {
        const leaves = getLeaves(layout);
        const newLayout = createBalancedTreeFromLeaves(leaves);
        handleChange(newLayout);
    };

    const addToTopRight = () => {
        let currentNode = layout;
        const totalWindowCount = getLeaves(currentNode).length;
        if (currentNode) {
            const path = getPathToCorner(currentNode, Corner.TOP_RIGHT);
            const parent = getNodeAtPath(currentNode, dropRight(path));
            const destination = getNodeAtPath(currentNode, path);
            const direction = parent ? getOtherDirection(parent.direction) : 'row';

            let first, second;
            if (direction === 'row') {
                first = destination;
                second = totalWindowCount + 1;
            } else {
                first = totalWindowCount + 1;
                second = destination;
            }

            currentNode = updateTree(currentNode, [
                {
                    path,
                    spec: {
                        $set: {
                            direction,
                            first,
                            second,
                        },
                    },
                },
            ]);
        } else {
            currentNode = totalWindowCount + 1;
        }

        handleChange(currentNode);
    };

    // useEffect(() => {
    //     function resizeMap() {
    //         const mapWrapper = document.getElementById('map-wrapper');
    //         if (mapWrapper) {
    //             const map = mapWrapper.querySelector('.leaflet-container');
    //             if (map && map._leaflet) {
    //                 map._leaflet.invalidateSize(true);
    //             }
    //         }
    //     }
    //
    //     function setupResizeObserver() {
    //         const container = document.getElementById(id);
    //         if (container) {
    //             new ResizeObserver(() => {
    //                 setTimeout(resizeMap, 100);
    //             }).observe(container);
    //         }
    //     }
    //
    //     setupResizeObserver();
    //     window.addEventListener('resize', () => {
    //         setTimeout(resizeMap, 100);
    //     });
    //
    //     // Initial resize after a short delay to ensure map is loaded
    //     // eslint-disable-next-line no-magic-numbers
    //     setTimeout(resizeMap, 500);
    //
    //     return () => {
    //         window.removeEventListener('resize', resizeMap);
    //     };
    // }, [id]);


    const defaultRenderTile = (id, path) => (
        <MosaicContext.Consumer>
            {({ mosaicActions }) => (
                <MosaicWindow
                    path={path}
                    title={windowTitles[id] || `Window ${id}`}
                    toolbarControls={[
                        showSplitButton && (
                            <Button
                                key="split"
                                onClick={() => mosaicActions.split(path)}
                                minimal={true}
                                icon={<Icon icon="add-column-right" />}
                            />
                        ),
                        showExpandButton && (
                            <Button
                                key="expand"
                                onClick={() => mosaicActions.expand(path)}
                                minimal={true}
                                icon={<Icon icon="arrows-horizontal" />}
                            />
                        ),
                        showRemoveButton && (
                            <Button
                                key="remove"
                                onClick={() => mosaicActions.remove(path)}
                                minimal={true}
                                icon={<Icon icon="cross" />}
                            />
                        )
                    ].filter(Boolean)}
                >
                    {tileContent && tileContent[id] ? tileContent[id] : <div>Content for Window {id}</div>}
                </MosaicWindow>
            )}
        </MosaicContext.Consumer>
    );

    return (
        <div id={id} style={{...style, height: style.height || '100vh', width: '100%'}}>
            {showNavbar && (
                <div className={classNames(Classes.NAVBAR, Classes.DARK, 'mobile-friendly-navbar')}>
                    <div className={Classes.NAVBAR_GROUP + ' responsive-navbar-group'}>
                        <div className="navbar-controls">
                            <HTMLSelect
                                className="responsive-select"
                                value={theme}
                                onChange={(e) => setProps({theme: e.target.value})}
                            >
                                {Object.keys(THEMES).map((label) => (
                                    <option key={label} value={label}>{label}</option>
                                ))}
                            </HTMLSelect>

                            <Button
                                className={Classes.BUTTON + ' responsive-button'}
                                icon={IconNames.GRID_VIEW}
                                onClick={autoArrange}
                            >
                                Auto Arrange
                            </Button>
                            <Button
                                className={Classes.BUTTON + ' responsive-button'}
                                icon={IconNames.ARROW_TOP_RIGHT}
                                onClick={addToTopRight}
                            >
                                Add Window
                            </Button>
                        </div>
                    </div>
                </div>
            )}
            <Mosaic
                renderTile={renderTile || defaultRenderTile}
                value={layout}
                onChange={(newNode) => {
                    handleChange(newNode);
                    // Trigger map resize after layout change
                    setTimeout(() => {
                        const mapWrapper = document.getElementById('map-wrapper');
                        if (mapWrapper) {
                            const map = mapWrapper.querySelector('.leaflet-container');
                            if (map && map._leaflet) {
                                map._leaflet.invalidateSize(true);
                            }
                        }
                    }, 100);
                }}
                onRelease={handleRelease}
                className={THEMES[theme]}
                zeroStateView={zeroStateView || <MosaicZeroState/>}
                resize={resize}
            />
        </div>
    );
};

DashMosaic.defaultProps = {
    layout: {
        direction: 'row',
        first: 1,
        second: {
            direction: 'column',
            first: 2,
            second: 3,
        },
        splitPercentage: 40,
    },
    theme: 'Blueprint',
    onChange: () => {
    },
    onRelease: () => {},
    tileContent: {},
    style: {},
    windowTitles: {},
    showSplitButton: true,
    showExpandButton: true,
    showRemoveButton: true,
    showNavbar: true,
};

DashMosaic.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The layout configuration for the mosaic. It defines the structure and arrangement of the panes.
     */
    layout: PropTypes.object,

    /**
     * The theme to apply to the mosaic. Options are 'Blueprint', 'Blueprint Dark', or 'None'.
     */
    theme: PropTypes.oneOf(Object.keys(THEMES)),

    /**
     * A function that renders the content of each tile. It receives the tile ID and path as arguments.
     */
    renderTile: PropTypes.func,

    /**
     * The component to display when there are no tiles (zero state).
     */
    zeroStateView: PropTypes.element,

    /**
     * Callback function that is called when the layout changes.
     */
    onChange: PropTypes.func,

    /**
     * Callback function that is called when the user releases a tile after dragging.
     */
    onRelease: PropTypes.func,

    /**
     * Object containing resize-related options for the mosaic.
     */
    resize: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * An object containing the content for each tile, keyed by tile ID.
     */
    tileContent: PropTypes.objectOf(PropTypes.node),

    /**
     * Inline styles to apply to the mosaic container.
     */
    style: PropTypes.object,

    /**
     * An object containing custom titles for each window, keyed by tile ID.
     */
    windowTitles: PropTypes.objectOf(PropTypes.string),

    /**
     * Whether to show the split button in the tile toolbar.
     */
    showSplitButton: PropTypes.bool,

    /**
     * Whether to show the expand button in the tile toolbar.
     */
    showExpandButton: PropTypes.bool,

    /**
     * Whether to show the remove button in the tile toolbar.
     */
    showRemoveButton: PropTypes.bool,

    /**
     * Whether to show the navbar at the top of the mosaic.
     */
    showNavbar: PropTypes.bool,
};

export default DashMosaic;