import pytest

from pyfield import Text
from pyfield.error import InvalidError

from pyfield.validator.text import is_credit_card
from pyfield.validator.text import is_credit_card_strict
from pyfield.validator.text import is_email_addr
from pyfield.validator.text import is_ipv4
from pyfield.validator.text import is_mac_addr


def test_text_credit_card():
    credit_card = Text('credit card',
                       validator=[is_credit_card])

    credit_card('3519 2073 7960 3241')
    assert credit_card.get == '3519 2073 7960 3241'
    credit_card('3519-2073-7960-3241')
    assert credit_card.get == '3519-2073-7960-3241'
    credit_card('3519207379603241')
    assert credit_card.get == '3519207379603241'

    credit_card('3519-2073 7960 3241')
    assert credit_card.get == '3519-2073 7960 3241'
    credit_card('3519-2073-7960 3241')
    assert credit_card.get == '3519-2073-7960 3241'
    credit_card('3519 2073-7960 3241')
    assert credit_card.get == '3519 2073-7960 3241'
    credit_card('3519 2073-7960-3241')
    assert credit_card.get == '3519 2073-7960-3241'
    credit_card('3519 2073 7960-3241')
    assert credit_card.get == '3519 2073 7960-3241'

    with pytest.raises(InvalidError):
        credit_card('1234')

    with pytest.raises(InvalidError):
        credit_card('123')

    with pytest.raises(InvalidError):
        credit_card('12341234123413245')

    with pytest.raises(InvalidError):
        credit_card('1234_1234_1234_1234')


def test_text_credit_card_strict():
    credit_card = Text('credit card',
                       validator=[is_credit_card_strict])

    credit_card('3519-2073-7960-3241')
    assert credit_card.get == '3519-2073-7960-3241'
    credit_card('3519207379603241')
    assert credit_card.get == '3519207379603241'

    with pytest.raises(InvalidError):
        credit_card('3519 2073 7960 3241')
    with pytest.raises(InvalidError):
        credit_card('3519-2073 7960 3241')
    with pytest.raises(InvalidError):
        credit_card('3519-2073-7960 3241')
    with pytest.raises(InvalidError):
        credit_card('3519 2073-7960 3241')
    with pytest.raises(InvalidError):
        credit_card('3519 2073-7960-3241')
    with pytest.raises(InvalidError):
        credit_card('3519 2073 7960-3241')

    with pytest.raises(InvalidError):
        credit_card('1234')

    with pytest.raises(InvalidError):
        credit_card('123')

    with pytest.raises(InvalidError):
        credit_card('12341234123413245')

    with pytest.raises(InvalidError):
        credit_card('1234_1234_1234_1234')


def test_text_email():
    email = Text('email',
                 validator=[is_email_addr])

    email('very.common@example.com')
    assert email.get == 'very.common@example.com'

    email('Indeed@strange.com')
    assert email.get == 'Indeed@strange.com'

    email('user.name+tag+sorting@example.com')
    assert email.get == 'user.name+tag+sorting@example.com'

    with pytest.raises(InvalidError):
        email('Abc.example.com')

    with pytest.raises(InvalidError):
        email('A@b@c@example.com')

    with pytest.raises(InvalidError):
        email('john.doe@example..com')


def test_text_ipv4():
    ipv4 = Text('ipv4',
                validator=[is_ipv4])

    IP_V4_DATA = {
        "1.1.1.1": True,
        "255.255.255.255": True,
        "192.168.1.1": True,
        "10.10.1.1": True,
        "132.254.111.10": True,
        "26.10.2.10": True,
        "127.0.0.1": True,
        "10.10.10": False,
        "10.10": False,
        "10": False,
        "a.a.a.a": False,
        "10.0.0.a": False,
        "10.10.10.256": False,
        "222.222.2.999": False,
        "999.10.10.20": False,
        "2222.22.22.22": False,
        "22.2222.22.2": False, }


    for ip, result in IP_V4_DATA.items():
        if result:
            ipv4(ip)
            assert ipv4.get == ip
        if not result:
            with pytest.raises(InvalidError):
                ipv4(ip)


def test_text_mac_addr():
    mac = Text('mac',
               validator=[is_mac_addr])

    mac('00:08:C7:1B:8C:02')
    assert mac.get == '00:08:C7:1B:8C:02'

    with pytest.raises(InvalidError):
        mac('48:H2:01:V6:00')
