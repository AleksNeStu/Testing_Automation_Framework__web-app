#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for add contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data
from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email
from tests.model.contact import Contact


def test_add_contact(app):
    """Check the possibility of add contact."""
    old_contacts = app.contact.get_list_of_contacts()
    contact = Contact(name=r_data(data.CONTACT_NAME),
                      last_name=r_data(data.CONTACT_NAME_LAST),
                      email=r_email(data.CONTACT_EMAIL))
    app.contact.create(contact)
    actual_contacts = app.contact.get_list_of_contacts()
    assert len(old_contacts) + 1 == len(actual_contacts)