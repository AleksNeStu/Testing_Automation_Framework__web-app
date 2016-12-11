#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Data for filling."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


# login credentials
LOGIN = "admin"
PASSWORD = "secret"

# prefix for new objects
_NEW = "New_"

# data for creation (modification) contacts
CONTACT_FIRST_NAME = "Contact_firstname_"
CONTACT_MIDDLE_NAME = "Contact_middlename_"
CONTACT_LAST_NAME = "Contact_lastname_"
CONTACT_EMAIL = "@gmail.com"
CONTACT_FIRST_NAME_NEW = _NEW + CONTACT_FIRST_NAME
CONTACT_MIDDLE_NAME_NEW = _NEW + CONTACT_MIDDLE_NAME
CONTACT_LAST_NAME_NEW = _NEW + CONTACT_LAST_NAME
CONTACT_EMAIL_NEW = _NEW + CONTACT_EMAIL

# data for creation (modification) groups
GROUP_NAME = "Group_name_"
GROUP_HEADER = "Group_header_"
GROUP_FOOTER = "Group_footer_"
GROUP_NAME_NEW = _NEW + GROUP_NAME
GROUP_HEADER_NEW = _NEW + GROUP_HEADER
GROUP_FOOTER_NEW = _NEW + GROUP_FOOTER