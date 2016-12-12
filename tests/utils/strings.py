#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Utils for make operations with strings (text)."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import re

from tests.constants import data, keys


def search_string_in_raw_text(raw_text, regex, gr_number=1):
    """Search string in 'raw_text' according 'regex' and return matches for
    a group number 'gr_number': group(gr_number)
    Example:
    Find in raw text 'A: text' and return 'text'
    """
    phone_number = ""
    _reg = re.compile(regex)
    if _reg.search(raw_text):
        phone_number = _reg.search(raw_text).group(gr_number)
    return phone_number

def normal_select_title(ext_title):
    """Normalize extended title (exclude brackets).
    Example:
    'Select (title_name)' to 'title_name'
    """
    return ext_title[ext_title.find("(")+1:ext_title.find(")")]

def home_full_name_to_dict(full_name):
    """Convert full name text line to dictionary with predefined keys
    for home page.
    Example:
    'middle last first' to
    {'firstname': 'first', 'middlename': 'middle', 'lastname': 'last'}
    """
    _full_name = full_name.split()
    full_name_list = []
    for _name_part in _full_name:
        if data.CONTACT_FIRST_NAME in _name_part:
            full_name_list.append((keys.FIRST_NAME, _name_part))
        if data.CONTACT_MIDDLE_NAME in _name_part:
            full_name_list.append((keys.MIDDLE_NAME, _name_part))
        if data.CONTACT_LAST_NAME in _name_part:
            full_name_list.append((keys.LAST_NAME, _name_part))
    return dict(full_name_list)

def home_all_phones_to_list(all_phones):
    """Convert all phones multi lines to list for home page.
    Example:
    'home
     mobile
     work
     secondary' to ['home', 'mobile', 'work', 'secondary']
    """
    _all_phones = all_phones.splitlines()
    if len(_all_phones) == 4: return _all_phones
    else: return [None, None, None, None]

def merge_phones_like_home(contact):
    """Merge phones attributes's values of 'contact' object to row (text) view like
    all phones represent on home page.
    Example:
    ['+13620559771', '+18017067538', '+14844346575', '+15480292852']
    to
    '+13620559771
     +18017067538
     +14844346575
     +15480292852'
    """
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clean_phone(x),
                   filter(lambda x: x is not None,
                          [contact.home_phone, contact.work_phone,
                           contact.mobile_phone, contact.secondary_phone]))))

def clean_phone(phone_number):
    """Clean unnecessary parts from phone number text
    (exclude: '-', '(', ')', ' ')
    Example:
    '+1-377-368-4628' to '+13773684628'
    """
    return re.sub("[() -]","",phone_number)