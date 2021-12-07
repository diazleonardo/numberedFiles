import os
import sys


sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../../src'))

# import src
from conf_local import git_tag

# -- Project information -----------------------------------------------------

project = 'Numbered Files'
copyright = '2021, Leonardo Díaz'
author = 'Leonardo Díaz'

# The full version, including alpha/beta/rc tags
version = '0.'
release = f"{version}{git_tag()}"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc']
autodoc_default_options = {'members': True,
                           "inherited-members": True,
                           "undoc-members": True,
                           'member-order': 'bysource', }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['.build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinxdoc'
# html_theme = 'classic'
# html_theme = 'agogo'
# html_theme = 'nature'
# html_theme = 'scrolls'
html_theme = 'pyramid'
# html_theme = 'haiku'
# html_theme = 'bizstyle'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ['custom.css']
