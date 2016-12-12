#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Universal test model generator."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import functools
import random
import string

from tests.constants import data, repeat


def random_data(prefix, maxlen=repeat.RANDOM_DATA):
    """Random string generator for common strings."""
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join(
        [random.choice(symbols) for _ in range(random.randint(1, maxlen))])

def random_email(domain=data.CONTACT_EMAIL, maxlen=repeat.RANDOM_EMAIL):
    """Generate mail like data@gmail.com."""
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in
                    range(random.randint(1, maxlen))]) + domain

def random_phone(code=data.PHONE_CODE):
    """Generate random phone number (default for USA: code=1)
       Example:
       +1-844-751-8951
    """
    d = functools.partial(random.randint, 0, 9)
    phone = lambda: "+{}-{}{}{}-{}{}{}-{}{}{}{}".format(
        code, d(), d(), d(), d(), d(), d(), d(), d(), d(), d())
    return phone()