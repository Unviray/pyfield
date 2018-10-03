"""
Builtin validator for Text field
"""

import re

from pyfield.error import InvalidError


def is_credit_card(arg):
    """
    Check if arg is an credit card
    """
    credit_card_pattern = r'^(\d{4}[-\s]?){3}\d{4}$'

    if not re.match(credit_card_pattern, arg):
        raise InvalidError('Invalid Credit card')


def is_credit_card_strict(arg):
    """
    Strict check if arg is an credit card
    """
    credit_card_strict_pattern = r'^((\d{4}){3}|(\d{4}-){3}|(\d{4}\s)\
        {3})\d{4}$'

    if not re.match(credit_card_strict_pattern, arg):
        raise InvalidError('Invalid Credit card')


def is_email_addr(arg):
    """
    Check if arg is an email
    """
    email_pattern = r"([A-Za-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[\
        a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"

    if not re.match(email_pattern, arg):
        raise InvalidError('Invalid Email')


def is_ipv4(arg):
    """
    Check if arg is an ipv4
    """
    bit = r"([01]?\d{1,2}|2(5[0-5]|[0-4]\d))"
    ipv4_pattern = r"^{0}\.{0}\.{0}\.{0}$".format(bit)

    if not re.match(ipv4_pattern, arg):
        raise InvalidError('Invalid ipv4')


def is_mac_addr(arg):
    """
    Check if arg is an mac address
    """
    mac_address_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}' \
                          r'([0-9A-Fa-f]{2})$'

    if not re.match(mac_address_pattern, arg):
        raise InvalidError('Invalid mac address')
