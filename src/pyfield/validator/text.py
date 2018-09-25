"""
Builtin validator for Text field
"""

import re

from pyfield.error import InvalidError


def is_email_addr(arg):
    """
    Check if arg is an email
    """

    email_pattern = r"([A-Za-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[\
        a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"

    if not re.match(email_pattern, arg):
        raise InvalidError('Invalid Email')
