from pyfield import Text


def test_text():
    text = Text('test text')

    text('hello')
    assert text.get == 'hello'

    text('World')
    assert text.get == 'World'
