#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modifying contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.contact import Contact


def test_modify_name_of_some_contact(app):
    """Check the possibility to modify some contact's name."""
    if app.contact.count_of_contacts_via_home() == 0:
        app.contact.create_contact(Contact())
    contact_name = Contact(first_name=r_data(data.CONTACT_FIRST_NAME_NEW))
    first_contacts = app.contact.list_of_contacts_via_home()
    contact_name.id = first_contacts[0].id
    index = randrange(len(first_contacts))
    app.contact.modify_contact(index, contact_name)
    assert len(first_contacts) == app.contact.count_of_contacts_via_home()
    actual_contacts = app.contact.list_of_contacts_via_home()
    expected_contacts = first_contacts[:index] + [contact_name] + first_contacts[index+1:]
    assert (
        sorted(expected_contacts, key=Contact.id_or_max) ==
        sorted(actual_contacts, key=Contact.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_contacts, actual_contacts))

def test_modify_some_contact(app):
    """Check the possibility to modify some contact."""
    if app.contact.count_of_contacts_via_home() == 0:
        app.contact.create_contact(Contact())
    first_contacts = app.contact.list_of_contacts_via_home()
    contact = Contact(first_name=r_data(data.CONTACT_FIRST_NAME_NEW),
                      last_name=r_data(data.CONTACT_LAST_NAME_NEW),
                      email=r_data(data.CONTACT_EMAIL_NEW))
    index = randrange(len(first_contacts))
    app.contact.modify_contact(index, contact)
    contact.id = first_contacts[0].id
    assert len(first_contacts) == app.contact.count_of_contacts_via_home()
    actual_contacts = app.contact.list_of_contacts_via_home()
    expected_contacts = first_contacts[:index] + [contact] + first_contacts[index+1:]
    assert (
        sorted(expected_contacts, key=Contact.id_or_max) ==
        sorted(actual_contacts, key=Contact.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_contacts, actual_contacts))