#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for check contacts phones."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import data, messages
from tests.generator.generic import (random_data as r_data,
                                     random_phone as r_phone,
                                     random_email as r_email)
from tests.model.contact import Contact
from tests.utils import strings


def test_check_contact_phones_via_home_and_edit(app):
    """Check contact's phones via home (contacts) page and edit form."""
    if app.contact.count_of_contacts_via_home() == 0:
        contact = Contact(first_name=r_data(data.CONTACT_FIRST_NAME),
                          middle_name=r_data(data.CONTACT_MIDDLE_NAME),
                          last_name=r_data(data.CONTACT_LAST_NAME),
                          home_phone=r_phone(), mobile_phone=r_phone(),
                          work_phone=r_phone(), secondary_phone=r_phone(),
                          email=r_email(data.CONTACT_EMAIL))
        app.contact.create_contact(contact)
    contacts_via_home = app.contact.list_of_contacts_via_home()
    index = randrange(len(contacts_via_home))
    contact_via_home = contacts_via_home[index]
    contact_via_edit = app.contact.contact_info_via_edit(index)
    edit_home_phone = strings.clean_phone(contact_via_edit.home_phone)
    edit_work_phone = strings.clean_phone(contact_via_edit.work_phone)
    edit_mobile_phone = strings.clean_phone(contact_via_edit.mobile_phone)
    edit_secondary_phone = strings.clean_phone(contact_via_edit.secondary_phone)
    assert (contact_via_home.home_phone == edit_home_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.home_phone, edit_home_phone))
    assert (contact_via_home.work_phone == edit_work_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.work_phone, edit_work_phone))
    assert (contact_via_home.mobile_phone == edit_mobile_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.mobile_phone, edit_mobile_phone))
    assert (contact_via_home.secondary_phone == edit_secondary_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.secondary_phone, edit_secondary_phone))


def test_check_contact_phones_via_home_and_details(app):
    """Check contact's phones via home (contacts) page and details form."""
    if app.contact.count_of_contacts_via_home() == 0:
        contact = Contact(first_name=r_data(data.CONTACT_FIRST_NAME),
                          middle_name=r_data(data.CONTACT_MIDDLE_NAME),
                          last_name=r_data(data.CONTACT_LAST_NAME),
                          home_phone=r_phone(), mobile_phone=r_phone(),
                          work_phone=r_phone(), secondary_phone=r_phone(),
                          email=r_email(data.CONTACT_EMAIL))
        app.contact.create_contact(contact)
    contacts_via_home = app.contact.list_of_contacts_via_home()
    index = randrange(len(contacts_via_home))
    contact_via_home = contacts_via_home[index]
    contact_via_details = app.contact.contact_info_via_details(index)
    details_home_phone = strings.clean_phone(contact_via_details.home_phone)
    details_work_phone = strings.clean_phone(contact_via_details.work_phone)
    details_mobile_phone = strings.clean_phone(
        contact_via_details.mobile_phone)
    details_secondary_phone = strings.clean_phone(
        contact_via_details.secondary_phone)
    assert (contact_via_home.home_phone == details_home_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.home_phone, details_home_phone))
    assert (contact_via_home.work_phone == details_work_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.work_phone, details_work_phone))
    assert (contact_via_home.mobile_phone == details_mobile_phone,
            messages.COMPARE_HOME_VS_EDIT.format(
                contact_via_home.mobile_phone, details_mobile_phone))
    assert (contact_via_home.secondary_phone == details_secondary_phone,
            messages. COMPARE_HOME_VS_EDIT.format(
                contact_via_home.secondary_phone, details_secondary_phone))