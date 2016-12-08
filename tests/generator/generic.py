#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Universal test model generator."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import random
import string


def random_data(prefix, maxlen):
    """Random str generator for common strs."""
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randint(1, maxlen))])


def random_email(maxlen, domain="@gmail.com"):
    """Random str generator for mail."""
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randint(1, maxlen))]) + domain