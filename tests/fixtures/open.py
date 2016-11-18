#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Open fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class OpenHelper:
    """Class for represent Open."""
    def __init__(self, app):
        self.app = app
        self.url = "http://127.0.0.1/addressbook/"

    def open_group_page(self):
        """Open full url path of group page."""
        wd = self.app.wd
        wd.get(self.url + "group.php")

    def open_home_page(self):
        """Open full url path of home page"""
        wd = self.app.wd
        wd.get(self.url)