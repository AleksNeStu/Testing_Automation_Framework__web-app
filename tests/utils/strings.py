#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Utils for make operations with strings (text)."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import re

from tests.constants import data, keys


def _list_strings_to_multi_line_text(strings):
    """Convert list of 'strings' to multi-line text.
    Example:
    ['value1', 'value2', 'value3', 'value4']
    to
    'value1
     value2
     value3
     value4'
    """
    return "\n".join(
        filter(lambda x: x != "", filter(lambda x: x is not None, strings)))

def _list_strings_to_single_line_text(strings):
    """Convert list of 'strings' to single-line text separated by a white space.
    Example:
    ['value1', 'value2', 'value3', 'value4'] to
    'value1 value2 value3 value4'
    """
    return " ".join(strings)

def _search_string_in_raw_text(raw_text, regex, gr_number=1):
    """Search string in 'raw_text' according 'regex' and return matches for
    a group number 'gr_number': group(gr_number)
    Example:
    Find in raw text 'A: text' and return 'text'
    """
    string = ""
    _reg = re.compile(regex)
    if _reg.search(raw_text):
        string = _reg.search(raw_text).group(gr_number)
    return string

def _findall_strings_in_raw_text(raw_text, regex):
    """Findall strings in 'raw_text' according 'regex' and return list of
    matches and then to multi-line text
    Example:
    Find in raw text
    'value@1
     value@2' to
    ['value@1', 'value@2'] to
    'value@1
     value@2'
    """
    list_strings = []
    _reg = re.compile(regex)
    if len(_reg.findall(raw_text)) > 1:
        list_strings = _reg.findall(raw_text)
    return _list_strings_to_multi_line_text(list_strings)

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

def clean_phone(phone_number):
    """Clean unnecessary parts from phone number text
    (exclude: '-', '(', ')', ' ')
    Example:
    '+1-377-368-4628' to '+13773684628'
    """
    return re.sub("[() -]","",phone_number)

def merge_name_parts_like_home_from_obj(contact):
    """Merge name parts attributes's values of 'contact' object to
    single-line text as on home page.
    """
    list_attrs = [contact.first_name, contact.middle_name, contact.last_name]
    return _list_strings_to_single_line_text(list_attrs)

def merge_emails_like_home_from_obj(contact):
    """Merge emails attributes's values of 'contact' object to
    multi-line text as on home page.
    """
    list_attrs = [contact.email, contact.email2, contact.email3]
    return _list_strings_to_multi_line_text(list_attrs)

def merge_phones_like_home_from_obj(contact):
    """Merge phones attributes's values of 'contact' object to
    multi-line text as on home page.
    """
    list_attrs = [contact.home_phone, contact.work_phone,
                  contact.mobile_phone, contact.secondary_phone]
    return clean_phone(_list_strings_to_multi_line_text(list_attrs))