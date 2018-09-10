import pytest

from pyfield import Integer

from pyfield.error import InvalidError


def test_integer():
    number = Integer('number')

    number(45)
    assert number.get == 45

    number('33') # str
    assert number.get == 33


def test_integer_complex():

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
                  default=16,
                  transformator=[add2, mult],
                  validator=[maximum, minimum])

    assert age.get == 36

    age('18')
    assert age.get == 40

    age(17)
    assert age.get == 38

    with pytest.raises(InvalidError):
        age('400')
        age(3)
