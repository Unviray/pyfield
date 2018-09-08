"""
Module to hold integer field
"""

from pyfield.field import Field


class Integer(Field):
    """
    Integer field

    >>> from pyfield import Integer
    >>> age = Integer('age')
    >>> age('18')
    >>> print(age.get)
    18
    """

    def __init__(self, name, **kwargs):
        super(Integer, self).__init__(name, **kwargs)

        self.name = name
        self.hold = 0

        self.transformator = kwargs.pop('transformator', [int])
