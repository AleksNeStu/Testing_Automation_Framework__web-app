#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Contact model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from sys import maxsize


class Contact:
    """Contact model entity."""
    def __init__(self, id=None, name=None, last_name=None, email=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return ("id:{id}, name:{name}, last_name:{last_name}, email:{email}").format(
            id=self.id, name=self.name, last_name=self.last_name, email=self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name == other.name) and (self.last_name == other.last_name)

    @staticmethod
    def id_or_max(contact):
        """Method to sorted contact objects by id or max value."""
        if contact.id:
            return int(contact.id)
        else:
            return maxsize