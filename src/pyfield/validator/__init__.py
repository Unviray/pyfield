"""
Builtin validator
"""

from pyfield.error import InvalidError


def valid_type(check_type=object):
    """
    Builtin type validator
    """

    def warped(to_valid):
        """
        This isn't a decorator but a function returned for execute in validator
        """

        if not isinstance(to_valid, check_type):
            typebase = type(check_type)
            typearg = type(to_valid)
            raise InvalidError(f'Input must be {typebase} not {typearg}')

    return warped
