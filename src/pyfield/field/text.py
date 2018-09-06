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
        self.name = name
        self.hold = ''

    def __call__(self, _input):
        """
        Inject value
        """

        self.hold = str(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
