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
    >>> print(age.get)
    18
    """

    def __init__(self, name, **kwargs):
        super(Integer, self).__init__()

        self.name = name
        self.hold = 0

        self.transformator = kwargs.pop('transformator', [])

    def __call__(self, _input):
        """
        Inject value
        """

        _input = int(_input)

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        self.hold = int(_input)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
