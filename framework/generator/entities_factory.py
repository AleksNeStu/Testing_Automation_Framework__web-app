#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Module for generate test data for work with model's objects (entities)."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from constants import data
from generator.random_data import RandomData as r_data
from model.contact import Contact
from model.group import Group
import json
import random
# import getopt
# import sys
import os


# n = 5
# o = "generate"
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "n:o:", ["number of objects", "operation (type)"])
# except getopt.GetoptError as err:
#     getopt.usage()
#     sys.exit(2)


class EntitiesFactory(object):
    """Common factory class for entities."""

    @classmethod
    def generate_json(cls, test_data, file):
        obj_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "templates/" + file)
        with open(obj_file, "w") as obj_f:
            obj_f.write(json.dumps(test_data, default=lambda x: x.__dict__,
                                   indent=2))

class ContactFactory(EntitiesFactory):
    """Factory class for Contact entity."""

    @classmethod
    def create(cls):
        """Create Contact entity with randomly filled fields and
        return list of objects.
        """
        contact =  [Contact(
            first_name=r_data.common_part(data.CONTACT_FIRST_NAME),
            middle_name=r_data.common_part(data.CONTACT_MIDDLE_NAME),
            last_name=r_data.common_part(data.CONTACT_LAST_NAME),
            address=r_data.common_part(data.CONTACT_ADDRESS),
            email=r_data.email_part(data.CONTACT_EMAIL_DOMAIN),
            email2=r_data.email_part(data.CONTACT_EMAIL_DOMAIN),
            email3=r_data.email_part(data.CONTACT_EMAIL_DOMAIN),
            home_phone=r_data.phone(), mobile_phone=r_data.phone(),
            work_phone=r_data.phone(), secondary_phone=r_data.phone())]
        return contact

    @classmethod
    def create_empty(cls):
        """Create Contact entity with empty filled fields and
        return list of objects.
        """
        contact = [Contact()]
        return contact

    @classmethod
    def create_mixed(cls, n=5):
        """Create Contact entities with mixed filled fields and
        return list of objects.
        """
        contacts =  [Contact(
            first_name=first_name, middle_name=middle_name, last_name=last_name,
            address=address, email=email, email2=email2, email3=email3,
            home_phone=home_phone, mobile_phone=mobile_phone,
            work_phone=work_phone, secondary_phone=secondary_phone)
                for first_name in [
                    "", r_data.common_part(data.CONTACT_FIRST_NAME)]
                for middle_name in [
                    "", r_data.common_part(data.CONTACT_MIDDLE_NAME)]
                for last_name in [
                    "", r_data.common_part(data.CONTACT_LAST_NAME)]
                for address in [
                    "", r_data.common_part(data.CONTACT_ADDRESS)]
                for email in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for email2 in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for email3 in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for home_phone in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for mobile_phone in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for work_phone in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]
                for secondary_phone in [
                    "", r_data.email_part(data.CONTACT_EMAIL_DOMAIN)]]
        return [random.choice(contacts) for _ in xrange (0, n)]

    @classmethod
    def generate(cls, create_type):
        cls.generate_json(test_data=create_type, file="contact.json")
        return create_type


class GroupFactory(EntitiesFactory):
    """Factory class for Group entity."""

    @classmethod
    def create(cls):
        """Create Group entity with randomly filled fields."""
        return [Group(name=r_data.common_part(data.GROUP_NAME),
                      header=r_data.common_part(data.GROUP_HEADER),
                      footer=r_data.common_part(data.GROUP_FOOTER))]

    @classmethod
    def create_empty(cls):
        """Create Group entity with empty filled fields."""
        return [Group()]

    @classmethod
    def create_mixed(cls):
        """Create Group entities with mixed filled fields and
        return list of objects.
        """
        return [Group(name=name, header=header, footer=footer)
                for name in ["", r_data.common_part(data.GROUP_NAME)]
                for header in ["", r_data.common_part(data.GROUP_HEADER)]
                for footer in ["", r_data.common_part(data.GROUP_FOOTER)]]

    @classmethod
    def generate(cls, create_type):
        cls.generate_json(test_data=create_type, file="group.json")
        return create_type