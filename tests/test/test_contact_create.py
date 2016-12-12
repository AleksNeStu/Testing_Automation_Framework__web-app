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


test_data = [Contact(first_name=first_name, middle_name=middle_name,
                     last_name=last_name, home_phone=home_phone,
                     mobile_phone=mobile_phone, work_phone=work_phone,
                     secondary_phone=secondary_phone, email=email)
             for first_name in ["", r_data(data.CONTACT_FIRST_NAME)]
             for middle_name in ["", r_data(data.CONTACT_MIDDLE_NAME)]
             for last_name in ["", r_data(data.CONTACT_LAST_NAME)]
             for home_phone in ["", r_phone()]
             for mobile_phone in ["", r_phone()]
             for work_phone in ["", r_phone()]
             for secondary_phone in ["", r_phone()]
             for email in ["", r_email(data.CONTACT_EMAIL)]]

@pytest.mark.smoke_tests
@pytest.mark.parametrize("contact", test_data)
def test_add_contact(app, contact):
    """Check of a possibility to create new random contact via home (contacts)
    page.
    """
    old_contacts = app.contact.list_of_contacts_via_home()
    app.contact.create_contact_via_add(contact)
    assert len(old_contacts) + 1 == app.contact.count_of_contacts_via_home()
    actual_contacts = app.contact.list_of_contacts_via_home()
    contact.id = actual_contacts[-1].id
    expected_contacts = old_contacts + [contact]
    assert (sorted(expected_contacts, key=Contact.id_or_max) ==
            sorted(actual_contacts, key=Contact.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_contacts,
                                               actual_contacts))