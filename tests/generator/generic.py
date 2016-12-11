#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Universal test model generator."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

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

def random_phone():
    """Generate random phone like 844-751-8951"""
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]