#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for modifying contacts."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages
from model.contact import Contact


@pytest.mark.smoke_tests
def test_modify_some_contact(
        app, generator_entities_ContactFactory_generate_create_mixed,
        generator_templates_contacts):
    """Check of a possibility to modify exist contact used random attributes of
    new object 'new_contact'.
    """
    new_contact = generator_templates_contacts
    if app.contact.count_of_contacts_home() == 0:
        app.contact.create_contact_add(Contact())
    first_contacts = app.contact.list_of_contacts_home()
    ind = randrange(len(first_contacts))
    app.contact.modify_contact_home(ind, new_contact)
    new_contact.id = first_contacts[0].id
    assert len(first_contacts) == app.contact.count_of_contacts_home()
    actual_contacts = app.contact.list_of_contacts_home()
    expected_contacts = (first_contacts[:ind] + [new_contact] +
                         first_contacts[ind+1:])
    assert (sorted(expected_contacts, key=Contact.id_or_max) ==
            sorted(actual_contacts, key=Contact.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_contacts,
                                               actual_contacts))