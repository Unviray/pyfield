"""
Module to hold boolean field
"""

from pyfield.field import Field
from pyfield.error import InvalidError


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
        self.base = kwargs.pop('base', bool)

        def valid_str(arg):
            if not isinstance(arg, self.base):
                typebase = type(self.base)
                typearg = type(arg)
                raise InvalidError(f'Input must be {typebase} not {typearg}')

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_str] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
