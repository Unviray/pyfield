from pyfield import RealNumber


def test_real_number():

    def addl(arg):
        return arg + 0.03

    def mult(arg):
        return arg * 0.6

    real_number = RealNumber('heigth',
                             transformator=[addl, mult])

    real_number('12.5')
    assert 7.6 > real_number.get > 7.5

    real_number(33.25)
    assert real_number.get == 19.968
