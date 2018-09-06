"""
Module to hold integer field
"""

from pyfield.field import Field


class Integer(Field):
    """
    Integer field

    >>> from pyfield import Integer
    >>> age = Integer('age')
    >>> age('18')
    >>>print(age.get)
    18
    """

    def __init__(self, name):
        self.name = name
        self.hold = 0

    def __call__(self, _input):
        """
        Inject value
        """

        self.hold = int(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
