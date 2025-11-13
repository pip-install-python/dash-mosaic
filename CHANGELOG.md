# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-12

### Added
- Initial stable release of Dash Mosaic
- Multi-pane resizable and draggable layouts using react-mosaic-component
- Three built-in themes: Blueprint, Blueprint Dark, and None (custom)
- Interactive controls: split, expand, and remove buttons
- Customizable window titles for each pane
- Layout change tracking via Dash callbacks
- Support for single-pane and nested split layouts
- Optional navbar with theme selector and layout controls
- Comprehensive documentation and examples
- Professional README with detailed usage guide
- Example application (`usage.py`) with Plotly charts and statistics
- Full MIT License
- Python 3.7+ support
- Dash 2.0.0+ compatibility

### Features
- **Flexible Layout System**: Hierarchical row/column splits with customizable percentages
- **Rich Content Support**: Embed any Dash components (charts, maps, tables, etc.)
- **Responsive Design**: Mobile-friendly with adaptive controls
- **Blueprint.js Integration**: Professional UI components and theming
- **Zero-State Support**: Custom component when layout is empty
- **Auto-arrange**: Automatically balance all panes
- **Dynamic Content**: Update pane content through callbacks

### Documentation
- Comprehensive README.md with examples
- claude.md technical guide for developers
- Usage examples with Plotly visualizations
- Contributing guidelines
- Code review checklist

### Known Limitations
- Font and asset files require manual copying to project assets folder
- Maps (like Leaflet) may require resize handling when panes change

### Contributors
Special thanks to [@dantreiman](https://github.com/dantreiman) for contributing the single window support feature in [PR #1](https://github.com/pip-install-python/dash-mosaic/pull/1), which allows layouts to accept either an integer (single pane) or a dict (split layout).

## [Unreleased]

### Planned
- Automated asset inclusion in package distribution
- Layout persistence (save/restore layouts)
- Layout presets for common configurations
- Keyboard shortcuts for pane navigation
- Min/max size constraints for panes
- Additional theme options
- Storybook component gallery
- Video tutorials

---

[1.0.0]: https://github.com/pip-install-python/dash-mosaic/releases/tag/v1.0.0