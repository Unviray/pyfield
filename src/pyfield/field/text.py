"""
Module to hold text field
"""

from pyfield.field import Field
from pyfield.error import InvalidError


class Text(Field):
    """
    Text field

    >>> from pyfield import Text
    >>> text = Text('First name')
    >>> text('Jonatana')
    >>> print(text.get)
    Jonatana
    """

    def __init__(self, name, **kwargs):
        super(Text, self).__init__(name, **kwargs)

        self.name = name
        self.hold = ''
        self.base = kwargs.pop('base', str)

        def valid_str(arg):
            if not isinstance(self.base):
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
