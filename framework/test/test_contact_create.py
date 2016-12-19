#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for creating contacts."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from constants import messages
from model.contact import Contact


@pytest.mark.smoke_tests
def test_add_contact(app,
                     generator_entities_ContactFactory_generate_create_mixed):
    """Check of a possibility to create new random contact via home (contacts)
    page.
    """
    contact = generator_entities_ContactFactory_generate_create_mixed
    old_contacts = app.contact.list_of_contacts_home()
    app.contact.create_contact_add(contact)
    assert len(old_contacts) + 1 == app.contact.count_of_contacts_home()
    actual_contacts = app.contact.list_of_contacts_home()
    contact.id = actual_contacts[-1].id
    expected_contacts = old_contacts + [contact]
    assert (sorted(expected_contacts, key=Contact.id_or_max) ==
            sorted(actual_contacts, key=Contact.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_contacts,
                                               actual_contacts))