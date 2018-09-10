import pytest

from pyfield import Integer

from pyfield.error import InvalidError


def test_integer():

    def add2(arg):
        return arg + 2

    def mult(arg):
        return arg + arg

    def maximum(arg):
        if arg > 200:
            raise InvalidError('You are dead')

    def minimum(arg):
        if arg < 10:
            raise InvalidError('Too young')

    age = Integer('age',
                  transformator=[add2, mult],
                  validator=[maximum, minimum])

    age('18')
    assert age.get == 40

    age(17)
    assert age.get == 38

    with pytest.raises(InvalidError):
        age('400')
        age(3)
