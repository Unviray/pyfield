from pyfield import Integer


def test_integer():
    integer = Integer('age')

    integer('18')
    assert integer.get == 18

    integer(17)
    assert integer.get == 17
