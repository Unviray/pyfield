"""
Module to hold text field
"""

from pyfield.field import Field
from pyfield.validator import valid_type


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
        self.hold = str()
        self.base = kwargs.pop('base', str)

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_type(self.base)] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
