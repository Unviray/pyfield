# -*- coding: utf-8 -*-
"""
Field collection for you form
"""

from pkg_resources import get_distribution, DistributionNotFound

from pyfield.field.boolean import Boolean
from pyfield.field.integer import Integer
from pyfield.field.real_number import RealNumber
from pyfield.field.text import Text

__all__ = ('Boolean', 'Integer', 'RealNumber', 'Text')

try:
    DIST_NAME = __name__
    __version__ = get_distribution(DIST_NAME).version
except DistributionNotFound:  # pragma: no cover
    __version__ = 'unknown'
finally:
    del get_distribution
    del DistributionNotFound
