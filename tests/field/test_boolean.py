from pyfield import Boolean


def test_boolean():
    stay = Boolean('Stay connected')

    stay(True)
    assert stay.get

    stay(False)
    assert not stay.get


def test_rev():

    def revcall(arg):
        return not arg

    revers = Boolean('rev',
                     transformator=[revcall])

    revers(True)
    assert not revers.get

    revers(False)
    assert revers.get
