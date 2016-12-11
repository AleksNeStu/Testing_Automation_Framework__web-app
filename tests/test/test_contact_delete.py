#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for deleting contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import messages
from tests.model.contact import Contact


def test_del_some_contact(app):
    """Check the possibility to delete some contact via home (contacts) page."""
    if app.contact.count_of_contacts_via_home() == 0:
        app.contact.create_contact(Contact())
    first_contacts = app.contact.list_of_contacts_via_home()
    index = randrange(len(first_contacts))
    app.contact.delete_contact_via_home(index)
    assert len(first_contacts) - 1 == app.contact.count_of_contacts_via_home()
    actual_contacts = app.contact.list_of_contacts_via_home()
    expected_contacts = first_contacts[:index] + first_contacts[(index + 1):]
    assert expected_contacts == actual_contacts, messages.ERR_MSG_FORMAT.format(
        expected_contacts, actual_contacts)

def test_del_all_contacts(app):
    """Check the possibility to delete all contacts via home (contacts) page."""
    if app.contact.count_of_contacts_via_home() == 0:
        [app.contact.create_contact(Contact()) for _ in xrange(3)]
    app.contact.delete_all_contacts_via_home()
    contacts = app.contact.list_of_contacts_via_home()
    assert len(contacts) == app.contact.count_of_contacts_via_home() == 0