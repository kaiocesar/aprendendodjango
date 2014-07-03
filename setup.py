# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import segundo
version = segundo.__version__

setup(
    name='segundo',
    version=version,
    author='',
    author_email='programador.kaio@gmail.com',
    packages=[
        'segundo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['segundo/manage.py'],
)