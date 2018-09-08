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

        self.transformator = kwargs.pop('transformator', [str])
