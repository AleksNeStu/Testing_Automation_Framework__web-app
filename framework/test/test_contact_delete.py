#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for deleting contacts."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages


@pytest.mark.smoke_tests
def test_del_some_contact(
        app, generator_entities_ContactFactory_generate_create_empty,
        generator_templates_contacts):
    """Check of a possibility to delete random contact via home (contacts)
    page.
    """
    contact = generator_templates_contacts
    if app.contact.count_of_contacts_home() == 0:
        app.contact.create_contact_add(contact)
    first_contacts = app.contact.list_of_contacts_home()
    ind = randrange(len(first_contacts))
    app.contact.delete_contact_home(ind)
    assert len(first_contacts) - 1 == app.contact.count_of_contacts_home()
    actual_contacts = app.contact.list_of_contacts_home()
    expected_contacts = first_contacts[:ind] + first_contacts[(ind + 1):]
    assert (expected_contacts == actual_contacts,
            messages.COMPARE_EXP_VS_GOT.format(expected_contacts,
                                               actual_contacts))


@pytest.mark.smoke_tests
def test_del_all_contacts(
        app, generator_entities_ContactFactory_generate_create_empty,
        generator_templates_contacts):
    """Check of a  possibility to delete all contacts via home (contacts)
    page.
    """
    contact = generator_templates_contacts
    if app.contact.count_of_contacts_home() == 0:
        [app.contact.create_contact_add(contact) for _ in xrange(3)]
    app.contact.delete_all_contacts_home()
    contacts = app.contact.list_of_contacts_home()
    assert len(contacts) == app.contact.count_of_contacts_home() == 0