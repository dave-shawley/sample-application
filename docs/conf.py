import crudite

project = 'crudite'
copyright = 'AWeber Communications, Inc.'
version = crudite.version
release = '.'.join(str(c) for c in crudite.version_info[:2])
needs_sphinx = '1.6'
extensions = ['sphinx.ext.intersphinx',
              'sphinxcontrib.autohttp.tornado']
source_suffix = '.rst'
master_doc = 'index'
html_sidebars = {'**': ['about.html', 'navigation.html', 'searchbox.html']}
html_theme_options = {
    'github_user': 'sprockets',
    'github_repo': 'sample-application',
    'github_banner': True,
}

intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
    'tornado': ('http://tornadoweb.org/en/latest/', None),
    'sprockets-http': ('https://sprocketshttp.readthedocs.io/en/latest', None),
}
