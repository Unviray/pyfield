=======
pyfield
=======

.. image:: https://travis-ci.org/Ublimjo/pyfield.svg?branch=master
    :target: https://travis-ci.org/Ublimjo/pyfield

Collection of field for your form **not** *only web form*


Description
===========

**pyfield** is a collection of field with battery included.

This project is under developmment, please read
`CONTIBUTING.rst <https://github.com/Ublimjo/pyfield/blob/master/CONTRIBUTING.rst>`_


Example
=======

.. code-block:: python

 >>> from pyfield import Text
 >>>
 >>> def main():
 >>>     username = Text('Username')
 >>>     username(input(username.prompt_input()))
 >>>     print(f'Your name is {username.get}')
 >>>
 >>> main()
  Username: Bob
 Your name is Bob

It's very simple but pyfield comes with a lot of features

 - Default value
 - Transformator
 - Validator

Read the docs if you want to know more about these features or create your own
Transformator and validator


