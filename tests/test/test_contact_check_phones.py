#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for check contacts phones."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from tests.constants import data, messages
from tests.generator.generic import (random_data as r_data,
                                     random_phone as r_phone,
                                     random_email as r_email)
from tests.model.contact import Contact
from tests.utils import strings


test_data = [Contact(first_name=r_data(data.CONTACT_FIRST_NAME),
                     middle_name=r_data(data.CONTACT_MIDDLE_NAME),
                     last_name=r_data(data.CONTACT_LAST_NAME),
                     home_phone=r_phone(), mobile_phone=r_phone(),
                     work_phone=r_phone(), secondary_phone=r_phone(),
                     email=r_email(data.CONTACT_EMAIL))]

@pytest.mark.smoke_tests
@pytest.mark.parametrize("contact", test_data)
def test_check_contact_phones_via_home_and_edit(app, contact):
    """Check contact's phones via home (contacts) page and edit form."""
    if app.contact.count_of_contacts_via_home() == 0:
        app.contact.create_contact_via_add(contact)
    contacts_via_home = app.contact.list_of_contacts_via_home()
    ind = randrange(len(contacts_via_home))
    contact_via_home = contacts_via_home[ind]
    contact_via_edit = app.contact.contact_info_via_edit(ind)
    contact_all_phones_via_home = contact_via_home.all_phones_home
    contact_all_phones_via_edit = strings.merge_phones_like_home(
        contact_via_edit)
    assert (contact_all_phones_via_home == contact_all_phones_via_edit,
            messages.COMPARE_HOME_VS_EDIT.format(contact_all_phones_via_home,
                                                 contact_all_phones_via_edit))

@pytest.mark.smoke_tests
@pytest.mark.parametrize("contact", test_data)
def test_check_contact_phones_via_home_and_details(app, contact):
    """Check contact's phones via home (contacts) page and details form."""
    if app.contact.count_of_contacts_via_home() == 0:
        app.contact.create_contact_via_add(contact)
    contacts_via_home = app.contact.list_of_contacts_via_home()
    ind = randrange(len(contacts_via_home))
    contact_via_home = contacts_via_home[ind]
    contact_via_details = app.contact.contact_info_via_details(ind)
    contact_all_phones_via_home = contact_via_home.all_phones_home
    contact_all_phones_via_details = strings.merge_phones_like_home(
        contact_via_details)
    assert (contact_all_phones_via_home == contact_all_phones_via_details,
            messages.COMPARE_HOME_VS_EDIT.format(contact_all_phones_via_home,
                                                 contact_all_phones_via_details))