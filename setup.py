#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for pyfield.

    This file was generated with PyScaffold 3.0.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup, find_packages

entry_points = """
[console_scripts]
# script_name = pyfield.module:function
# For example:
# fibonacci = pyfield.skeleton:run
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True)


def main():

    from os import path

    here = path.abspath(path.dirname(__file__))

    # long_description
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='pyfield',
        version='0.1.1',
        description='Collection of field for your form',
        license='MIT',
        long_description=long_description,
        url='https://github.com/Ublimjo/pyfield',
        author='Ublimjo',
        author_email='ublimjo@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6', ],
        keywords='field form validator',
        packages=find_packages(where='src'),
        package_dir={"": "src"},
        project_urls={
            'Source': 'https://github.com/Ublimjo/pyfield/',
            'Bug Reports': 'https://github.com/Ublimjo/pyfield/issues', })


if __name__ == "__main__":
    # setup_package()
    main()
