import crudite

project = 'crudite'
copyright = 'AWeber Communications, Inc.'
version = crudite.version
release = '.'.join(str(c) for c in crudite.version_info[:2])
needs_sphinx = '1.6'
extensions = ['sphinx.ext.intersphinx']
source_suffix = '.rst'
master_doc = 'index'

intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
    'tornado': ('http://tornadoweb.org/en/latest/', None),
}
