#!/usr/bin/env python
# vi:si:et:sw=4:sts=4:ts=4
# encoding: utf-8
try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name="ebml",
    version="0.1",
    description="python-ebml",
    author="Joseph Spiros",
    url="https://github.com/jspiros/python-ebml",
    packages=['ebml', 'ebml.tests', 'ebml.utils', 'ebml.schema'],
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

