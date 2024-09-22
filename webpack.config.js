const path = require('path');
const webpack = require('webpack');
const WebpackDashDynamicImport = require('@plotly/webpack-dash-dynamic-import');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const fs = require('fs');

const packagejson = require('./package.json');

const dashLibraryName = packagejson.name.replace(/-/g, '_');

module.exports = (env, argv) => {
    const mode = argv && argv.mode || 'production';
    const filename = `${dashLibraryName}.${mode === 'development' ? 'dev' : 'min'}.js`;

    // Check if the icons directory exists
    const iconsDir = path.resolve(__dirname, 'node_modules', '@blueprintjs', 'icons', 'resources', 'icons');
    const iconsDirExists = fs.existsSync(iconsDir);

    const copyPatterns = [
        { from: 'src/lib/components/assets', to: 'assets' },
        { from: 'node_modules/@blueprintjs/core/lib/css', to: 'assets/css' },
        { from: 'node_modules/@blueprintjs/icons/lib/css', to: 'assets/css' },
    ];

    // Only add the icons directory if it exists
    if (iconsDirExists) {
        copyPatterns.push({ from: iconsDir, to: 'assets/icons' });
    }

    return {
        mode,
        entry: {main: './src/lib/index.js'},
        output: {
            path: path.resolve(__dirname, dashLibraryName),
            filename,
            library: dashLibraryName,
            libraryTarget: 'window',
        },
        devtool: 'source-map',
        externals: {
            react: 'React',
            'react-dom': 'ReactDOM',
            'plotly.js': 'Plotly',
            'prop-types': 'PropTypes',
        },
        module: {
            rules: [
                {
                    test: /\.jsx?$/,
                    exclude: [/node_modules/, /src\/lib\/components\/assets/],
                    use: {
                        loader: 'babel-loader',
                    },
                },
                {
                    test: /\.css$/,
                    use: ['style-loader', 'css-loader'],
                },
                {
                    test: /\.(woff|woff2|eot|ttf|otf)$/,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: '[name].[ext]',
                                outputPath: 'assets/fonts/',
                            },
                        },
                    ],
                },
                {
                    test: /\.svg$/,
                    use: [
                        {
                            loader: 'file-loader',
                            options: {
                                name: '[name].[ext]',
                                outputPath: 'assets/icons/',
                            },
                        },
                    ],
                },
            ],
        },
        resolve: {
            extensions: ['.js', '.jsx']
        },
        plugins: [
            new WebpackDashDynamicImport(),
            new webpack.SourceMapDevToolPlugin({
                filename: '[file].map',
                exclude: ['async-plotlyjs']
            }),
            new CopyWebpackPlugin({
                patterns: copyPatterns,
            }),
        ]
    };
};