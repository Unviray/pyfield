"""
Module to hold integer field
"""

from pyfield.field import Field
from pyfield.validator import valid_type


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
        self.hold = int()
        self.base = kwargs.pop('base', int)

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_type(self.base)] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
