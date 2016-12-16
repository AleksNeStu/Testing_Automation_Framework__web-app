#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Module for generate test data for work with model's objects (entities)."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from constants import data
from model.contact import Contact
from model.group import Group
from generator.random_data import RandomData as r_data

class EntitiesFactory(object):
    """Common factory class for entities."""


class ContactFactory(EntitiesFactory):
    """Factory class for Contact entity."""

    @staticmethod
    def create():
        """Create Contact entity with randomly filled fields."""
        return [Contact(
            first_name=r_data.common_part(data.CONTACT_FIRST_NAME),
            middle_name=r_data.common_part(data.CONTACT_MIDDLE_NAME),
            last_name=r_data.common_part(data.CONTACT_LAST_NAME),
            address=r_data.common_part(data.CONTACT_ADDRESS),
            email=r_data.email_part(data.CONTACT_EMAIL),
            email2=r_data.email_part(data.CONTACT_EMAIL),
            email3=r_data.email_part(data.CONTACT_EMAIL),
            home_phone=r_data.phone(), mobile_phone=r_data.phone(),
            work_phone=r_data.phone(), secondary_phone=r_data.phone())]

    @staticmethod
    def create_new():
        """Create new Contact entity with new randomly filled fields."""
        return [Contact(
            first_name=r_data.common_part(data.CONTACT_FIRST_NAME_NEW),
            middle_name=r_data.common_part(data.CONTACT_MIDDLE_NAME_NEW),
            last_name=r_data.common_part(data.CONTACT_LAST_NAME_NEW),
            address=r_data.common_part(data.CONTACT_ADDRESS_NEW),
            email=r_data.email_part(data.CONTACT_EMAIL_NEW),
            email2=r_data.email_part(data.CONTACT_EMAIL_NEW),
            email3=r_data.email_part(data.CONTACT_EMAIL_NEW),
            home_phone=r_data.phone(), mobile_phone=r_data.phone(),
            work_phone=r_data.phone(), secondary_phone=r_data.phone())]

    @staticmethod
    def create_empty():
        """Create Contact entity with empty filled fields."""
        return [Contact()]


class GroupFactory(EntitiesFactory):
    """Factory class for Group entity."""

    @staticmethod
    def create():
        """Create Group entity with randomly filled fields."""
        return [Group(
            name=r_data.common_part(data.GROUP_NAME),
            header=r_data.common_part(data.GROUP_HEADER),
            footer=r_data.common_part(data.GROUP_FOOTER))]

    @staticmethod
    def create_new():
        """Create new Group entity with new randomly filled fields."""
        return [Group(
            name=r_data.common_part(data.GROUP_NAME_NEW),
            header=r_data.common_part(data.GROUP_HEADER_NEW),
            footer=r_data.common_part(data.GROUP_FOOTER_NEW))]

    @staticmethod
    def create_empty():
        """Create Group entity with empty filled fields."""
        return [Group()]