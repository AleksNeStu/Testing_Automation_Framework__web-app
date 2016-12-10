#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for  contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email
from tests.model.contact import Contact


def test_add_contact(app):
    """Check the possibility of add contact."""
    old_contacts = app.contact.get_list_of_contacts_via_home()
    contact = Contact(first_name=r_data(data.CONTACT_FIRST_NAME),
                      last_name=r_data(data.CONTACT_LAST_NAME),
                      email=r_email(data.CONTACT_EMAIL))
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.get_count_of_contacts_via_home()
    actual_contacts = app.contact.get_list_of_contacts_via_home()
    contact.id = actual_contacts[-1].id
    expected_contacts = old_contacts + [contact]
    assert (
        sorted(expected_contacts, key=Contact.id_or_max) ==
        sorted(actual_contacts, key=Contact.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_contacts, actual_contacts))