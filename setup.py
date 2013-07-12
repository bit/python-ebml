#!/usr/bin/env python
# vi:si:et:sw=4:sts=4:ts=4
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name="ebml",
    version="0.1",
    description="python-ebml",
    author="Joseph Spiros",
    url="https://github.com/jspiros/python-ebml",
    packages=find_packages(),
    include_package_data=True,
    package_data = { '': [ '*.xml' ] },
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

