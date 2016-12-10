#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for deletion contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import messages
from tests.model.contact import Contact


def test_del_some_contact(app):
    """Check the possibility of del first contact."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    first_contacts = app.contact.get_list_of_contacts()
    index = randrange(len(first_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(first_contacts) - 1 == app.contact.count()
    actual_contacts = app.contact.get_list_of_contacts()
    expected_contacts = first_contacts[:index] + first_contacts[(index + 1):]
    assert expected_contacts == actual_contacts, messages.ERR_MSG_FORMAT.format(
        expected_contacts, actual_contacts)

def test_del_all_contacts(app):
    """Check the possibility of del all contacts."""
    if app.contact.count() == 0:
        [app.contact.create(Contact()) for _ in xrange(3)]
    app.contact.delete_all_contacts()
    contacts = app.contact.get_list_of_contacts()
    assert len(contacts) == app.contact.count() == 0