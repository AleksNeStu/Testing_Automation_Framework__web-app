#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Contact model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from sys import maxsize


class Contact:
    """Contact model entity."""
    def __init__(self, id=None, first_name=None, last_name=None,
                 home_phone=None, mobile_phone=None, work_phone=None,
                 secondary_phone=None, email=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email

    def __repr__(self):
        return (
            "id:{id}, first_name:{first_name}, "
            "last_name:{last_name}, email:{email}").format(
            id=self.id, first_name=self.first_name,
            last_name=self.last_name, email=self.email)

    def __eq__(self, other):
        return (
            self.id is None or other.id is None or self.id == other.id) and (
            self.first_name == other.first_name and
            self.last_name == other.last_name)

    @staticmethod
    def id_or_max(contact):
        """Method to sorted contact objects by id or max value."""
        if contact.id: return int(contact.id)
        else: return maxsize