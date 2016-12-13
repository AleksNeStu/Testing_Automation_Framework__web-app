#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for creating contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from tests.constants import data, messages
from tests.generator.generic import (
    random_data as r_data, random_email as r_email, random_phone as r_phone)
from tests.model.contact import Contact

test_data = [Contact(
    first_name=r_data(data.CONTACT_FIRST_NAME),
    middle_name=r_data(data.CONTACT_MIDDLE_NAME),
    last_name=r_data(data.CONTACT_LAST_NAME),
    address=r_data(data.CONTACT_ADDRESS), email=r_email(data.CONTACT_EMAIL),
    email2=r_email(data.CONTACT_EMAIL), email3=r_email(data.CONTACT_EMAIL),
    home_phone=r_phone(), mobile_phone=r_phone(), work_phone=r_phone(),
    secondary_phone=r_phone())] + [Contact()]

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