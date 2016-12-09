#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for deletion contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.model.contact import Contact
from tests.constants import messages


def test_del_first_contact(app):
    """Check the possibility of del first contact."""
    if app.contact.count() == 0:
        app.contact.create(Contact())
    first_contacts = app.contact.get_list_of_contacts()
    app.contact.delete_first_contact()
    actual_contacts = app.contact.get_list_of_contacts()
    assert len(first_contacts) - 1 == len(actual_contacts)
    expected_contacts= first_contacts[1:]
    assert expected_contacts == actual_contacts, messages.ERR_MSG_FORMAT.format(
        expected_contacts, actual_contacts)

def test_del_all_contacts(app):
    """Check the possibility of del all contacts."""
    if app.contact.count() == 0:
        [app.contact.create(Contact()) for _ in xrange(3)]
    app.contact.delete_all_contacts()
    contacts = app.contact.get_list_of_contacts()
    assert len(contacts) == 0