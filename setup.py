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
    author_email='pipinstallpython@gmail.com',
    url=package.get('homepage', ''),
    project_urls={
        'Bug Reports': package.get('bugs', {}).get('url', ''),
        'Source': package.get('repository', {}).get('url', '').replace('git://', 'https://'),
    },
    packages=find_packages(exclude=['tests', 'tests.*']),
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
    keywords=['dash', 'plotly', 'react', 'mosaic', 'layout', 'dashboard', 'multi-pane', 'resizable'],
    install_requires=[
        'dash>=2.0.0',
    ],
    python_requires='>=3.7',
    classifiers=[
        # Development Status
        'Development Status :: 5 - Production/Stable',

        # Intended Audience
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',

        # Topic
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Scientific/Engineering :: Visualization',

        # License
        'License :: OSI Approved :: MIT License',

        # Python Versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',

        # Framework
        'Framework :: Dash',

        # Operating System
        'Operating System :: OS Independent',

        # Environment
        'Environment :: Web Environment',
    ],
)
