#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Universal test model generator."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import functools
import random
import string


def random_data(prefix, maxlen=5):
    """Random string generator for common strings."""
    symbols = string.ascii_letters + string.digits
    return prefix + "".join(
        [random.choice(symbols) for _ in range(random.randint(1, maxlen))])

def random_email(domain="@gmail.com", maxlen=5):
    """Generate mail like data@gmail.com."""
    symbols = string.ascii_letters + string.digits
    return "".join(
        [random.choice(symbols) for _ in range(random.randint(1, maxlen))]) + domain

def random_phone(code=1):
    """Generate random phone number (default for USA: code=1)
       Example:
       +1-844-751-8951
    """
    d = functools.partial(random.randint, 0, 9)
    phone = lambda: "+{}-{}{}{}-{}{}{}-{}{}{}{}".format(
        code, d(), d(), d(), d(), d(), d(), d(), d(), d(), d())
    return phone()