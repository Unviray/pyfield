"""
All field are stored here
"""


class Field(object):
    """
    Base of all Field
    """

    def __init__(self):
        self.hold = object

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
