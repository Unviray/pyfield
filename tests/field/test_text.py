from pyfield import Text


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
