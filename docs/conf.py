# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config


# -- Project information -----------------------------------------------------

project = 'gadfly'
copyright = '2022, Brett M. Morris'
author = 'Brett M. Morris'

# The full version, including alpha/beta/rc tags
from gadfly import __version__
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/': None,
    'numpy': ('https://numpy.org/doc/stable/', None),
    'celerite2': ('https://celerite2.readthedocs.io/en/latest/', None),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
    'lightkurve': ('https://docs.lightkurve.org/', None),
    'matplotlib': ('http://matplotlib.org/stable', None)
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_logo = "assets/logo.png"
html_favicon = "assets/logo.ico"

numpydoc_show_class_members = False
autodoc_inherit_docstrings = True

html_context = {
    "display_github": True,
    "github_user": "bmorris3",
    "github_repo": "gadfly",
    "github_version": "master",
    "conf_py_path": "docs/",
}

