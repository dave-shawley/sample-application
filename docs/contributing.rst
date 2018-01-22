=================
How to contribute
=================

Set up a development environment
================================
We've been concentrating on pure Python 3 applications so I'm going to assume
that you have a Python 3 interpreter handy.  If not, please download one from
https://www.python.org/downloads/ and install it.  Development takes place
in a project-specific virtual environment that exists directly in the source
tree.  The SCM ignore file (e.g., *.gitignore*) is configured to ignore a
directory named *env* so put your virtual environment there::

   $ python3 -mvenv --copies env

You can omit the ``--copies`` flag if you are tight on disk space but the
symlinks may confuse some 3rd party tools -- PyCharm gets confused by this.

Once you have the environment ready, you can install the development toolchain
using the pip-formatted requirements files in the *requires* directory::

   $ env/bin/pip install -r requires/development.txt

The development environment requires some external services to run.  These are
run inside of docker containers via `docker-compose`_.  The *bootstrap*
script will start the containers necessary to run the application as well as
the tests::

   $ ./bootstrap

The services will be running as chil processes under the docker daemon.  They
are configured to bind to ephemeral ports so the *bootstrap* script
interrogates the docker daemon and writes the emphemeral port numbers to the
*build/test-environment* file.  Don't worry, the tests take care of reading
this in so you don't have to do anything special.

Once you have the enviroment installed, you are ready to start developing.
*setup.py* acts as your entry point with the following commands at your
disposal:

**./setup.py nosetests**
   Run the tests suite using the `nose`_ runner.  Include ``--with-coverage``
   for a coverage report.

**./setup.py build_sphinx**
   Generate documentation using `sphinx`_ into *build/sphinx/html*.

**./setup.py flake8**
   Run the `flake8`_ style checker.

**./setup.py httprun**
   Run the application locally.  This uses the `sprockets http setuptools
   command`_ to run the application as a tornado process.

If any of the preceding commands fail, then you will have to fix them
**before** you issue a pull request.  If these fail on a fresh clone of
master, then please create a github issue immediately so we can fix it.

Submitting a pull request
=========================
Once you have forked the repository and made whatever modifications were
required, it's time to contribute back by creating a pull request against the
upstream repository (https://github.com/sprockets/sample-application).

Describe why the changes are a good idea (or are necessary) in the body of the
pull request and wait for the continuous integration tests to run.  If the
tests pass, then someone will pick up the pull request.  If the tests fail,
then you can push additional commits to your branch to fix whatever is broken.

.. _flake8: https://flake8.readthedocs.io/
.. _nose: https://nose.readthedocs.io/
.. _sphinx: http://www.sphinx-doc.org/
.. _sprockets http setuptools command: https://sprocketshttp.readthedocs.io/en
   /latest/index.html#from-setup-py
