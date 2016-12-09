#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Utils for make operations with text."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

def normal_select_title(ext_title):
    """Convert extended title to normal view.
    Example:
        "Select (title_name)" to "title_name"
    """
    return ext_title[ext_title.find("(")+1:ext_title.find(")")]

def split_full_name_to_tuple(full_name):
    """Split full name to parts.
    Example:
        "Selenium Driver" to ("Selenium", "Driver")
    """
    return (full_name.split())


