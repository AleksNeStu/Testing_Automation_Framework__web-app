#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Module for providing randoms data for web-app's entities."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import functools
import random
import string

from constants import data, repeat


class RandomData(object):
    """Class that provide random data for generate web-app objects."""

    @staticmethod
    def common_part(prefix, maxlen=repeat.RANDOM_DATA):
        """Random generator of the common parts."""
        symbols = string.ascii_letters + string.digits + string.punctuation
        return prefix + "".join(
            [random.choice(symbols) for _ in range(random.randint(1, maxlen))])

    @staticmethod
    def email_part(domain=data.CONTACT_EMAIL,
              maxlen=repeat.RANDOM_EMAIL):
        """Random generator of the email parts.
           Example:
           dosFS@gmail.com.
        """
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for _ in
                        range(random.randint(1, maxlen))]) + domain

    @staticmethod
    def phone(code=data.PHONE_CODE):
        """Random generator of the phone number (default for USA: code=1)
           Example:
           +1-844-751-8951
        """
        d = functools.partial(random.randint, 0, 9)
        phone = lambda: "+{}-{}{}{}-{}{}{}-{}{}{}{}".format(
            code, d(), d(), d(), d(), d(), d(), d(), d(), d(), d())
        return phone()