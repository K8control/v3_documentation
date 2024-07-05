
# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Ableton v3 Framework'
author = 'Ableton Documentation Team'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# -- Options for HTML output

html_theme = 'alabaster'
html_static_path = ['_static']
