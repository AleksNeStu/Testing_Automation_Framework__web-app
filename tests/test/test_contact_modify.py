#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modification contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.contact import Contact


def test_modify_name_of_first_contact(app):
    """Check the possibility of modifying contact's name."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    contact_name = Contact(name=r_data(data.CONTACT_NAME_NEW))
    first_contacts = app.contact.get_list_of_contacts()
    contact_name.id = first_contacts[0].id
    app.contact.modify_first_contact(contact_name)
    assert len(first_contacts) == app.contact.count()
    actual_contacts = app.contact.get_list_of_contacts()
    expected_contacts = [contact_name] + first_contacts[1:]
    assert (
        sorted(expected_contacts, key=Contact.id_or_max) ==
        sorted(actual_contacts, key=Contact.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_contacts, actual_contacts))

def test_modify_first_contact(app):
    """Check the possibility of modifying contact's name, email."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    first_contacts = app.contact.get_list_of_contacts()
    contact = Contact(name=r_data(data.CONTACT_NAME_NEW),
                          last_name=r_data(data.CONTACT_NAME_LAST_NEW),
                          email=r_data(data.CONTACT_EMAIL_NEW))
    app.contact.modify_first_contact(contact)
    contact.id = first_contacts[0].id
    assert len(first_contacts) == app.contact.count()
    actual_contacts = app.contact.get_list_of_contacts()
    expected_contacts = [contact] + first_contacts[1:]
    assert (
        sorted(expected_contacts, key=Contact.id_or_max) ==
        sorted(actual_contacts, key=Contact.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_contacts, actual_contacts))