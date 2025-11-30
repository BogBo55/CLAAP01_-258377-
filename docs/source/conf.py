# conf.py – minimalne ustawienia
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CLAAP01_258377'
author = 'Bogusław Borkowski'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
