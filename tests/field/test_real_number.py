import pytest

from pyfield import RealNumber

from pyfield.error import InvalidError


def test_real_number():
    heigth = RealNumber('heigth')

    heigth(3.5)
    assert heigth.get == 3.5

    heigth('34.6') # str
    assert heigth.get == 34.6 # float


def test_real_number_complex():

    def addl(arg):
        return arg + 0.03

    def mult(arg):
        return arg * 0.6

    def maximum(arg):
        if arg > 30.0:
            raise InvalidError('More than 30.0')

    def minimum(arg):
        if arg < 5.0:
            raise InvalidError('Less than 5.0')

    real_number = RealNumber('volume',
                             default=20.3,
                             transformator=[addl, mult],
                             validator=[maximum, minimum])

    assert real_number.get == 12.198

    real_number('12.5')
    assert 7.6 > real_number.get > 7.5

    real_number(33.25)
    assert real_number.get == 19.968

    with pytest.raises(InvalidError):
        real_number(46.3)
        real_number('2.5')
