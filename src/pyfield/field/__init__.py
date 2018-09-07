"""
All field are stored here
"""


class Field(object):
    """
    Base of all Field
    """

    def __init__(self):
        self.hold = object

    def __call__(self, _input):
        self.hold = _input

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
