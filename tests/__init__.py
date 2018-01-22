import functools
import logging
import os.path


@functools.lru_cache(maxsize=10)  # makes this a singleton for free
def setup_module():
    logger = logging.getLogger('tests.setup_module')
    my_dir = os.path.abspath(os.path.dirname(__file__))
    top_dir = os.path.join(my_dir, os.pardir)
    with open(os.path.join(top_dir, 'build', 'test-environment')) as f:
        for line_no, line in enumerate(f):
            if '#' in line:
                line = line[:line.index('#')]
            line = line.strip()
            if line.startswith('export '):
                line = line[7:].strip()
            name, sep, value = line.partition('=')
            if sep != '=':
                logger.warning('failed to process line %d: %r',
                               line_no, line)
                continue
            if value:
                logger.debug('setting environment variable %s=%r',
                             name, value)
                os.environ[name] = value
            else:
                logger.debug('clearing environment variable %s', name)
                os.environ.pop(name, None)


setup_module()  # makes python -munittest work too
