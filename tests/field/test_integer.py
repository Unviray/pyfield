from pyfield import Integer


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
