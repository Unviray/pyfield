"""
Module to hold boolean field
"""

from pyfield.field import Field
from pyfield.validator import valid_type


class Boolean(Field):
    """
    Boolean field

    >>> from pyfield import Boolean
    >>> stay = Boolean('stay connected')
    >>> stay(True)
    >>> print(stay.get)
    True
    """

    def __init__(self, name, **kwargs):
        super(Boolean, self).__init__(name, **kwargs)

        self.name = name
        self.hold = bool()
        self.base = kwargs.pop('base', bool)

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_type(self.base)] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
