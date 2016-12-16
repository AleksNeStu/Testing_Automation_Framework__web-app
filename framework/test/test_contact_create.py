#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for creating contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from constants import messages
from generator.entities_factory import ContactFactory
from model.contact import Contact

test_data = ContactFactory.create() + ContactFactory.create_empty()

@pytest.mark.smoke_tests
@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    """Check of a possibility to create new random contact via home (contacts)
    page.
    """
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