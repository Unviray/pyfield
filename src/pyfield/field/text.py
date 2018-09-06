from pyfield.field import Field


class Text(Field):
    def __init__(self, name, **kwargs):
        self.name = name
        self.hold = ''

    def __call__(self, _input):
        self.hold = _input

    @property
    def get(self):
        return self.hold
