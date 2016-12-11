#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for check contacts phones."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.utils import strs


def test_check_contact_phones_via_home_and_edit(app):
    """Check contact(s) phones via home (contacts) page and edit form."""
    contacts_via_home = app.contact.list_of_contacts_via_home()
    index = randrange(len(contacts_via_home))
    contact_via_edit = app.contact.contact_info_via_edit(index)
    contact_via_home = contacts_via_home[index]
    assert (
        contact_via_home.home_phone ==
        strs.phone_number_normalize(contact_via_edit.home_phone))
    assert (
        contact_via_home.work_phone ==
        strs.phone_number_normalize(contact_via_edit.work_phone))
    assert (
        contact_via_home.mobile_phone ==
        strs.phone_number_normalize(contact_via_edit.mobile_phone))
    assert (
        contact_via_home.secondary_phone ==
        strs.phone_number_normalize(contact_via_edit.secondary_phone))