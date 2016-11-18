#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describing of the Group model."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class Group:
    """Group model entity."""
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer