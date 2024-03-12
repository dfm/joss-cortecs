#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import codecs
import os
import re
import sys

from sphinx_pyproject import SphinxConfig

from cortecs import __version__ as cortecs_version

config = SphinxConfig(
    "../pyproject.toml",
    globalns=globals(),
    config_overrides={"version": cortecs_version, "release": cortecs_version},
)

# MOCK_MODULES = [
#     "numpy",
#     "scipy",
#     "sklearn",
#     "matplotlib",
#     "matplotlib.pyplot",
#     "scipy.interpolate",
#     "scipy.special",
#     "math",
#     "__future__",
#     "toolboxutilities",
#     "exoplanet",
#     "sklearn",
#     "astropy.units",
#     "emcee",
#     "jax",
#     "jax.numpy",
#     "pandas",
#     "scipy.constants",
#     "numba",
#     "schwimmbad",
#     "astropy",
#     "astropy.constants",
# ]
# for mod_name in MOCK_MODULES:
#     sys.modules[mod_name] = mock.Mock()

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../src"))
sys.path.insert(0, os.path.abspath("../../src"))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

META_PATH = os.path.join("..", "src", "cortecs", "__init__.py")
HERE = os.path.abspath(os.path.dirname(__file__))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "sphinx_book_theme",
]


nbsphinx_prolog = """
This notebook is available at
https://github.com/arjunsavel/cortecs/tree/main/docs/{{ env.doc2path(env.docname, base=None) }}
"""
# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "cortecs"
copyright = "2023, Arjun B. Savel, Megan Bedell, Eliza M.-R. Kempton"
author = "Arjun B. Savel, Megan Bedell, Eliza M.-R. Kempton"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = find_meta("version")
# # The full version, including alpha/beta/rc tags.
# release = find_meta("release")

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_
# _path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "../src/cortecs/tests",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
# html_favicon = "_static/favicon.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "cortecsdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "cortecs.tex",
        "cortecs Documentation",
        "Arjun B. Savel, Megan Bedell, Eliza M.-R. Kempton",
        "manual",
    )
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "cortecs", "cortecs Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "cortecs",
        "cortecs Documentation",
        author,
        "cortecs",
        find_meta("description"),
        "Miscellaneous",
    )
]
