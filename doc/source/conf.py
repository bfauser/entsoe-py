#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# entsoe-py documentation build configuration file, created by
# sphinx-quickstart on Sun Feb 11 17:50:00 2018.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
	'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode']

# todo
todo_include_todos=True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'entsoe-py'
copyright = '2018, EnergieID.be'
author = 'EnergieID.be'

# The short X.Y version.
version = '0.1.12'
# The full version, including alpha/beta/rc tags.
release = '0.1.12'

language = None

exclude_patterns = ['setup.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

html_theme = 'agogo'

html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'entsoe-pydoc'


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
    (master_doc, 'entsoe-py.tex', 'entsoe-py Documentation',
     'EnergieID.be', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'entsoe-py', 'entsoe-py Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'entsoe-py', 'Entsoe-py Documentation',
     author, 'EnergieID.be', 'python package to connect to Entso-e\'s API',
     'Miscellaneous'),
]
	 
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}




