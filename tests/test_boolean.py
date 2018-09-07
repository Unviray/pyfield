from pyfield import Boolean


def test_boolean():
    stay = Boolean('Stay connected')

    stay(True)
    assert stay.get

    stay(False)
    assert not stay.get
