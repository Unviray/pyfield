import pytest

from pyfield import Text
from pyfield.error import InvalidError
from pyfield.validator.text import is_email_addr


def test_text_email():
    email = Text('email',
                 validator=[is_email_addr])

    email('very.common@example.com')
    assert email.get == 'very.common@example.com'

    email('Indeed@Strange.COM')
    assert email.get == 'Indeed@Strange.COM'

    email('user.name+tag+sorting@example.com')
    assert email.get == 'user.name+tag+sorting@example.com'

    with pytest.raises(InvalidError):
        email('Abc.example.com')
        email('A@b@c@example.com')
        email('john.doe@example..com')
