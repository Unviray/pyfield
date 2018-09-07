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
    >>> print(stay)
    True
    """

    def __init__(self, name):
        self.name = name
        self.hold = False

    def __call__(self, _input):
        """
        Inject value
        """

        self.hold = bool(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
