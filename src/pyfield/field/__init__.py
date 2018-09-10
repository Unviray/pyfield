"""
All field are stored here
"""


class Field(object):
    """
    Base of all Field
    """

    def __init__(self, name, **kwargs):
        self.name = name
        self.hold = object

        self.transformator = kwargs.pop('transformator', [])
        self.validator = kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            pass

    def __call__(self, _input):
        """
        Inject value
        """

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        # check validity
        for valida_call in self.validator:
            valida_call(_input)

        self.hold = _input

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
