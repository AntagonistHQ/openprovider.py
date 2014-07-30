import sys
import os

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

master_doc = 'index'
project = u'openprovider.py'
copyright = u'2014, Antagonist B.V'
version = '0.0.1'
release = '0.0.1'

html_static_path = ['_static']
templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = ['_build']

pygments_style = 'sphinx'
html_theme = 'default'

htmlhelp_basename = 'openproviderpydoc'
