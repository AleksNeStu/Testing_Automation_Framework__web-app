#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Group model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class Group:
    """Group model entity."""
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return ("id:{id}, name:{name}, header:{header}, footer:{footer}").format(
            id=self.id, name=self.name, header=self.header, footer=self.footer)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name