"""
Module to hold real number field
"""

from pyfield.field import Field


class RealNumber(Field):
    """
    Real number field

    >>> from pyfield import RealNumber
    >>> heigth = RealNumber('heigth')
    >>> heigth('1.85')
    >>> print(heigth.get)
    1.85
    """

    def __init__(self, name):
        super(RealNumber, self).__init__()

        self.name = name
        self.hold = 0.0

    def __call__(self, _input):
        """
        Inject value
        """

        self.hold = float(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
