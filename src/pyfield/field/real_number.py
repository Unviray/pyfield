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

    def __init__(self, name, **kwargs):
        super(RealNumber, self).__init__()

        self.name = name
        self.hold = 0.0

        self.transformator = kwargs.pop('transformator', [])

    def __call__(self, _input):
        """
        Inject value
        """

        _input = float(_input)

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        self.hold = float(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
