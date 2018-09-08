"""
Module to hold boolean field
"""

from pyfield.field import Field


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
        self.hold = False

        self.transformator = kwargs.pop('transformator', [bool])
