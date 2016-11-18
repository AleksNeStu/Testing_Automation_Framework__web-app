#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Contact model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class Contact:
    """Contact model entity."""
    def __init__(self, name, email):
        self.name = name
        self.email = email