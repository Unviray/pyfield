#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file for pyfield.
"""

from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# long_description
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def main():
    setup(
        name='pyfield',
        version='0.1.3',
        description='Collection of field for your form',
        license='MIT',
        long_description=long_description,
        url='https://github.com/Ublimjo/pyfield',
        author='Ublimjo',
        author_email='ublimjo@gmail.com',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Topic :: Terminals',
            'Topic :: Text Processing :: Filtersk',
            'Topic :: Utilities', ],
        keywords='field form validator',
        packages=find_packages(where='src'),
        package_dir={"": "src"},
        project_urls={
            'Source': 'https://github.com/Ublimjo/pyfield/',
            'Bug Reports': 'https://github.com/Ublimjo/pyfield/issues', })


if __name__ == "__main__":
    # setup_package()
    main()
