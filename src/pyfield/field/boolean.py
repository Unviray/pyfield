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

    def __init__(self, name, **kwargs):
        super(Boolean, self).__init__(name, **kwargs)

        self.name = name
        self.hold = False

        self.transformator = kwargs.pop('transformator', [bool])

    def __call__(self, _input):
        """
        Inject value
        """

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        self.hold = bool(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
