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
        This isn't a decorator but a function
        returned and executed in validator
        """

        if not isinstance(to_valid, check_type):
            typebase = type(check_type)
            typearg = type(to_valid)
            raise InvalidError('Input must be {} not {}'.format(
                typebase, typearg))

    return warped
