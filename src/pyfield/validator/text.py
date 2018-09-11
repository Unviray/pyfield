"""
Builtin validator for Text field
"""

import re
from expynent import patterns

from pyfield.error import InvalidError


def is_email_addr(arg):
    email_pattern = patterns.EMAIL_ADDRESS

    if not re.match(email_pattern, arg):
        raise InvalidError('Invalid Email')
