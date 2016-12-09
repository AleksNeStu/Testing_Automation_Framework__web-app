#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Contact model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class Contact:
    """Contact model entity."""
    def __init__(self, name=None, last_name=None, email=None):
        self.name = name
        self.last_name = last_name
        self.email = email