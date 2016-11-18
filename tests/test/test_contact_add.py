#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Contacts test."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email
from tests.model.contact import Contact


def test_add_contact(app):
    """Check the possibility of add contact."""
    app.session.login_admin()
    app.contact.create(Contact(name=r_data("Contact_", 5),
                               email=r_email(5, "@gmail.com")))
    app.session.logout()