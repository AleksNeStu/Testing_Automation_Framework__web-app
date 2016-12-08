#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Objects and Web-app URLs logic."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import urlparse

import os


def form_second_part_url(url_part):
    return url_part + ".php"

def check_second_part_url(full_url):
    full_part = urlparse.urlparse(full_url).path
    return os.path.split(full_part)[1]

# First part of URLs
APP_URL = "http://127.0.0.1/addressbook/"

# Seconds parts of URLs
HOME = "index"
ADD_NEW = "edit"
GROUPS = "group"
NEXT_BIRTHDAYS = "birthdays"
EXPORT = "export"
IMPORT = "import"

# Titles of URLs on web pages
_HOME = "home"
_ADD_NEW = "add new"
_GROUPS = "groups"
_GROUPS_ = "group page"
_NEXT_BIRTHDAYS = "next birthdays"
_PRINT_ALL = "print all"
_PRINT_PHONES = "print phones"
_MAP = "map"
_EXPORT = EXPORT
_IMPORT = IMPORT

# Full URLs
HOME_URL = urlparse.urljoin(APP_URL, form_second_part_url(HOME))
ADD_NEW_URL = urlparse.urljoin(APP_URL, form_second_part_url(ADD_NEW))
GROUPS_URL = urlparse.urljoin(APP_URL, form_second_part_url(GROUPS))
NEXT_BIRTHDAYS_URL = urlparse.urljoin(APP_URL, form_second_part_url(NEXT_BIRTHDAYS))
EXPORT_URL = (APP_URL, form_second_part_url(EXPORT))
IMPORT_URL = (APP_URL, form_second_part_url(IMPORT))