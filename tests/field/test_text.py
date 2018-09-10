import pytest

from pyfield import Text

from pyfield.error import InvalidError


def test_test():
    text = Text('simple')

    text('good')
    assert text.get == 'good'

    text(34) # int
    assert text.get == '34' # str


def test_text_complex():

    ## Transformator ##
    def upper(arg):
        return arg.upper()

    def unicoder(arg):
        return arg.replace(' ', '_')

    ## Validator ##
    def length(arg):
        if len(arg) > 20:
            raise InvalidError('More than 20 char')
        if len(arg) < 5:
            raise InvalidError('Less than 5 char')

    text = Text('test text',
                default='Foo bar',
                transformator=[upper, unicoder],
                validator=[length])

    assert text.get == 'FOO_BAR'

    text('Username')
    assert text.get == 'USERNAME'

    text('hello world')
    assert text.get == 'HELLO_WORLD'

    with pytest.raises(InvalidError):
        text('Too long long long text')
        text('s')
