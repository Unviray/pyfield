"""
Module to hold text field
"""

from pyfield.field import Field


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

        self.transformator = [str] + kwargs.pop('transformator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None
