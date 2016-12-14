#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module for generate test data for work with model's objects (entities)."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


from tests.constants import data
from tests.generator.generic import (
    random_data as r_data, random_email as r_email, random_phone as r_phone)
from tests.model.contact import Contact
from tests.model.group import Group


# Contact's entities
test_contact_full = [Contact(
    first_name=r_data(data.CONTACT_FIRST_NAME),
    middle_name=r_data(data.CONTACT_MIDDLE_NAME),
    last_name=r_data(data.CONTACT_LAST_NAME),
    address=r_data(data.CONTACT_ADDRESS), email=r_email(data.CONTACT_EMAIL),
    email2=r_email(data.CONTACT_EMAIL), email3=r_email(data.CONTACT_EMAIL),
    home_phone=r_phone(), mobile_phone=r_phone(), work_phone=r_phone(),
    secondary_phone=r_phone())]

test_contact_full_new = [Contact(
    first_name=r_data(data.CONTACT_FIRST_NAME_NEW),
    middle_name=r_data(data.CONTACT_MIDDLE_NAME_NEW),
    last_name=r_data(data.CONTACT_LAST_NAME_NEW),
    address=r_data(data.CONTACT_ADDRESS_NEW), email=r_email(data.CONTACT_EMAIL),
    email2=r_email(data.CONTACT_EMAIL), email3=r_email(data.CONTACT_EMAIL),
    home_phone=r_phone(), mobile_phone=r_phone(), work_phone=r_phone(),
    secondary_phone=r_phone())]

test_contact_empty = [Contact()]


# Group's entities
test_group_full = [Group(name=r_data(data.GROUP_NAME),
                         header=r_data(data.GROUP_HEADER),
                         footer=r_data(data.GROUP_FOOTER))]

test_group_full_new = [Group(name=r_data(data.GROUP_NAME_NEW),
                             header=r_data(data.GROUP_HEADER_NEW),
                             footer=r_data(data.GROUP_FOOTER_NEW))]

test_group_empty = [Group()]