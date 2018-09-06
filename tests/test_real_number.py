from pyfield import RealNumber


def test_real_number():
    real_number = RealNumber('heigth')

    real_number('12.5')
    assert real_number.get == 12.5

    real_number(33.25)
    assert real_number.get == 33.25
