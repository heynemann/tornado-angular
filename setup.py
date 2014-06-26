#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com


from setuptools import setup, find_packages
from tornado_angular import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
    'honcho',
]

setup(
    name='tornado_angular',
    version=__version__,
    description='tornado-angular is an opinionated way of distributing angular applications with tornado web server as api handler.',
    long_description='''
tornado-angular is an opinionated way of distributing angular applications with tornado web server as api handler.
''',
    keywords='tornado web angular api',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='https://github.com/heynemann/tornado-angular',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        'cow-framework',
        'pycurl',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'tornado_angular=tornado_angular.server:main',
        ],
    },
)
