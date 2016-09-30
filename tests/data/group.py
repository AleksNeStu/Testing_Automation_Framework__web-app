#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class Group:
    """Parameters for group data"""
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer