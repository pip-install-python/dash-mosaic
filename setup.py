import json
from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent
with open('package.json') as f:
    package = json.load(f)
long_description = (here / 'README.md').read_text()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'dash_mosaic': [
            'dash_mosaic.min.js',
            'dash_mosaic.min.js.map',
            'async-*.js',
            'async-*.js.map',
            '*-shared.js',
            '*-shared.js.map',
            'assets/*',
            'assets/**/*',
            'metadata.json',
            'package-info.json',
        ]
    },
    license=package['license'],
    description=package.get('description', package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers = [
        'Framework :: Dash',
    ],
)
