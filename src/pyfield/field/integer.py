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

        self.transformator = [int] + kwargs.pop('transformator', [])
        self.validator = kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            pass
