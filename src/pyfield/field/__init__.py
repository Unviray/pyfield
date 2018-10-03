"""
All field are stored here
"""

from pyfield.validator import valid_type


class Field(object):
    """
    Base of all Field
    """

    def __init__(self, name, **kwargs):
        self.name = name
        self.hold = object()
        self.base = kwargs.pop('base', object())

        self.transformator = kwargs.pop('transformator', [])
        self.validator = kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None

    def set_up(self, **kwargs):
        """
        get all transformator and validator from kwargs
        """

        self.transformator = [self.base] + kwargs.pop('transformator', [])
        self.validator = [valid_type(self.base)] + kwargs.pop('validator', [])

        try:
            # __call__
            self.default = self(kwargs.pop('default'))
        except KeyError:
            self.default = None

    def __call__(self, _input):
        """
        Inject value

        ex: email('alice@gmail.com')
        """

        # Apply transformation
        for transf_call in self.transformator:
            _input = transf_call(_input)

        # check validity
        for valida_call in self.validator:
            valida_call(_input)

        self.hold = _input
        return _input

    def prompt_input(self):
        """
        Build prompt for input

        ex: Would you like to exit [yes|no]:
        """

        if self.default is None:
            return ' {}: '.format(self.name)
        else:
            return ' {} [{}]: '.format(self.name, self.default)

    @property
    def get(self):
        """
        Get holded value
        """

        return self.hold
