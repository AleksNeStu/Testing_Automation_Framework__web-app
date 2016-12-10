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
        "Lastname Firstname" to ("Lastname", "Firstname")
    """
    _full_name = full_name.split()
    if len(_full_name) == 2: return _full_name
    if len(_full_name) == 1: return _full_name * 2
    if len(_full_name) == 0 or len(_full_name) >= 3: return [None, None]