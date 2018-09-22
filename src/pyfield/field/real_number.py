"""
Module to hold real number field
"""

from pyfield.field import Field
from pyfield.validator import valid_type


class RealNumber(Field):
    """
    Real number field

    >>> from pyfield import RealNumber
    >>> heigth = RealNumber('heigth')
    >>> heigth('1.85')
    >>> print(heigth.get)
    1.85
    """

    def __init__(self, name, **kwargs):
        super(RealNumber, self).__init__(name, **kwargs)

        self.name = name
        self.hold = float()
        self.base = kwargs.pop('base', float)

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_type(self.base)] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
