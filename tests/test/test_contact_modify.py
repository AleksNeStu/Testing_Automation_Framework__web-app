#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modifying contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from tests.constants import messages
from tests.generator import data
from tests.model.contact import Contact


test_data = data.test_contact_full + data.test_contact_empty

@pytest.mark.smoke_tests
@pytest.mark.parametrize("new_contact", test_data,
                         ids=[repr(x) for x in test_data])
def test_modify_some_contact(app, new_contact):
    """Check of a possibility to modify exist contact used random attributes of
    new object 'new_contact'.
    """
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