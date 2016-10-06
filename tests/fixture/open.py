#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Open fixture"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


class OpenHelper:

    def __init__(self, app):
        self.app = app
        self.url = "http://lamp/addressbook/"

    def open_group_page(self):
        wd = self.app.wd
        wd.get(self.url + "group.php")

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.url)