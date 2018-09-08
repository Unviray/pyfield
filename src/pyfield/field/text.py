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

    def __call__(self, _input):
        """
        Inject value
        """

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        self.hold = str(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
