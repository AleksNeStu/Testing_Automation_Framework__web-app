#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Objects and Web-app URLs logic."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import urlparse

import os


class URL:
    """Class for work with URLs."""
    def __init__(self, base_url):
        self.APP_URL = base_url
        # Seconds parts of URLs
        self.HOME = "index"
        self.ADD_NEW = "edit"
        self.GROUPS = "group"
        self.NEXT_BIRTHDAYS = "birthdays"
        self.EXPORT = "export"
        self.IMPORT = "import"
        # Titles of URLs on web pages
        self._HOME = "home"
        self._ADD_NEW = "add new"
        self._GROUPS = "groups"
        self._GROUPS_ = "group page"
        self._NEXT_BIRTHDAYS = "next birthdays"
        self._PRINT_ALL = "print all"
        self._PRINT_PHONES = "print phones"
        self._MAP = "map"
        self._EXPORT = self.EXPORT
        self._IMPORT = self.IMPORT
        # Full URLs
        self.HOME_URL = urlparse.urljoin(
            self.APP_URL, self.form_second_part_url(self.HOME))
        self.ADD_NEW_URL = urlparse.urljoin(
            self.APP_URL, self.form_second_part_url(self.ADD_NEW))
        self.GROUPS_URL = urlparse.urljoin(
            self.APP_URL, self.form_second_part_url(self.GROUPS))
        self.NEXT_BIRTHDAYS_URL = urlparse.urljoin(
            self.APP_URL, self.form_second_part_url(self.NEXT_BIRTHDAYS))
        self.EXPORT_URL = (self.APP_URL, self.form_second_part_url(self.EXPORT))
        self.IMPORT_URL = (self.APP_URL, self.form_second_part_url(self.IMPORT))

    @staticmethod
    def form_second_part_url(url_part):
        return url_part + ".php"

    @staticmethod
    def check_second_part_url(full_url):
        full_part = urlparse.urlparse(full_url).path
        return os.path.split(full_part)[1]