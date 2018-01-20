#!/usr/bin/env python
import os.path

import setuptools

import crudite


def read_requirements(name):
    requirements = []
    with open(os.path.join('requires', name)) as req_file:
        for line in req_file:
            if '#' in line:
                line = line[:line.index('#')]
            line = line.strip()
            if line.startswith('-r'):
                requirements.extend(line[2:].strip())
            elif line and not line.startswith('-'):
                requirements.append(line)
    return requirements


setuptools.setup(
    name='crudite',
    description='Sprockets/Tornado example application',
    long_description=open('README.rst').read(),
    url='https://github.com/sprockets/sample-application',
    version=crudite.version,
    author='AWeber Communications',
    author_email='api@aweber.com',
    license='BSD',
    packages=['crudite'],
    install_requires=read_requirements('installation.txt'),
    keywords='tornado example sprockets',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
