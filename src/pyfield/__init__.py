# -*- coding: utf-8 -*-
"""
Field collection for you form
"""

from pkg_resources import get_distribution, DistributionNotFound

from pyfield.field.text import Text
from pyfield.field.integer import Integer
from pyfield.field.real_number import RealNumber

__all__ = ('Text', 'Integer', 'RealNumber')

try:
    DIST_NAME = __name__
    __version__ = get_distribution(DIST_NAME).version
except DistributionNotFound:  # pragma: no cover
    __version__ = 'unknown'
