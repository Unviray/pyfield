from pyfield.field import Field

from pyfield import Text
from pyfield import Boolean
from pyfield import Integer
from pyfield import RealNumber


def test_field():
    field = Field('just a field',
                  transformator=[str])

    field('string')
    assert field.get == 'string'

    field(34)
    assert field.get == '34'


def test_text():

    def upper(arg):
        return arg.upper()

    def unicoder(arg):
        return arg.replace(' ', '_')

    text = Text('test text',
                transformator=[upper, unicoder])

    text('Username')
    assert text.get == 'USERNAME'

    text('hello world')
    assert text.get == 'HELLO_WORLD'


def test_boolean():

    def revcall(arg):
        return not arg

    stay = Boolean('Stay connected')
    revers = Boolean('rev',
                     transformator=[revcall])

    stay(True)
    assert stay.get

    stay(False)
    assert not stay.get

    revers(True)
    assert not revers.get

    revers(False)
    assert revers.get


def test_integer():

    def add2(arg):
        return arg + 2

    def mult(arg):
        return arg + arg

    age = Integer('age',
                  transformator=[add2, mult])

    age('18')
    assert age.get == 40

    age(17)
    assert age.get == 38


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
