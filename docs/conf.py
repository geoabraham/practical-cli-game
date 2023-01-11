"""Sphinx configuration."""
project = "Practical Cli Game"
author = "Geo Abraham"
copyright = "2023, Geo Abraham"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
