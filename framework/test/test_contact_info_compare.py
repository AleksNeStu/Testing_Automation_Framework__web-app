#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for check contacts phones."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages
from utils import strings


@pytest.mark.smoke_tests
def test_compare_contact_info_via_home_and_edit(
        app, generator_entities_ContactFactory_generate_create_empty,
        generator_templates_contacts):
    """Comparison contact's full info via home (contacts) page and edit form."""
    contact = generator_templates_contacts
    if app.contact.count_of_contacts_home() == 0:
        app.contact.create_contact_add(contact)
    contacts_home = app.contact.list_of_contacts_home()
    ind = randrange(len(contacts_home))
    contact_home = contacts_home[ind]
    contact_edit = app.contact.contact_info_edit(ind)
    contact_edit_full_name = strings.merge_name_parts_like_home_from_obj(
        contact_edit)
    contact_edit_address = contact_edit.address
    contact_edit_all_emails = strings.merge_emails_like_home_from_obj(
        contact_edit)
    contact_edit_all_phones = strings.merge_phones_like_home_from_obj(
        contact_edit)
    contact_home_full_info = (contact_home.full_name_home, contact_home.address,
                              contact_home.all_emails_home,
                              contact_home.all_phones_home)
    contact_edit_full_info = (contact_edit_full_name, contact_edit_address,
                              contact_edit_all_emails, contact_edit_all_phones)
    assert (contact_home_full_info == contact_edit_full_info,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_home.all_phones_home, contact_edit_all_phones))


@pytest.mark.smoke_tests
def test_compare_contact_phones_via_home_and_details(
        app, generator_entities_ContactFactory_generate_create_empty,
        generator_templates_contacts):
    """Comparison contact's full info via home (contacts) page and
    details form."""
    contact = generator_templates_contacts
    if app.contact.count_of_contacts_home() == 0:
        app.contact.create_contact_add(contact)
    contacts_home = app.contact.list_of_contacts_home()
    ind = randrange(len(contacts_home))
    contact_home = contacts_home[ind]
    contact_details = app.contact.contact_info_details(ind)
    contact_details_full_name = contact_details.full_name_details
    contact_details_all_emails = contact_details.all_emails_details
    contact_details_all_phones = strings.merge_phones_like_home_from_obj(
        contact_details)
    contact_home_full_info = (contact_home.full_name_home,
                              contact_home.all_emails_home,
                              contact_home.all_phones_home)
    contact_details_full_info = (contact_details_full_name,
                                 contact_details_all_emails,
                                 contact_details_all_phones)
    assert (contact_home_full_info == contact_details_full_info,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_home.all_phones_home, contact_details_full_info))