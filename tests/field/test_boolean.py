from pyfield import Boolean


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
