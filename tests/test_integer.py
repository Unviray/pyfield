from pyfield import Integer


def test_integer():
    age = Integer('age')

    age('18')
    assert age.get == 18

    age(17)
    assert age.get == 17
