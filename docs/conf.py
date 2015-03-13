extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

master_doc = 'index'
project = u'openprovider.py'
copyright = u'2014, Antagonist B.V'
version = '0.9.0'
release = '0.9.0'

html_static_path = ['_static']
templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = ['_build']

pygments_style = 'sphinx'
html_theme = 'default'

htmlhelp_basename = 'openproviderpydoc'

latex_elements = {
    'papersize': 'a4paper',
    'classoptions': ',openany,oneside',
    'babel': '\\usepackage[english]{babel}',
    'preamble': '\usepackage{microtype}',
}

latex_documents = [
    ('index', 'openproviderpy.tex', u'openprovider.py Documentation',
    u'Antagonist B.V.', 'manual'),
]
