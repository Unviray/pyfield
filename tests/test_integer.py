from pyfield import Integer


def test_text():
    text = Integer('age')

    text('18')
    assert text.get == 18

    text(17)
    assert text.get == 17
