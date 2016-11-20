#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Open fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import url


class OpenHelper:
    """Class for represent Open."""
    def __init__(self, app):
        self.app = app

    def open_url(self, full_url):
        """Open full url path used web driver get method."""
        wd = self.app.wd
        if self.is_obj_url_opened(full_url) is True:
            return
        else:
            wd.get(full_url)

    def open_link(self, link_text):
        """Open link used click method on web element."""
        wd = self.app.wd
        if self.is_obj_link_opened(link_text) is True:
            return
        else:
            wd.find_element_by_link_text(link_text).click()

    def is_obj_link_opened(self, link_text):
        wd = self.app.wd
        if url.form_second_part_url(link_text) == url.check_second_part_url(wd.current_url):
            return True
        else:
            return False

    def is_obj_url_opened(self, full_url):
        wd = self.app.wd
        if url.check_second_part_url(full_url) == url.check_second_part_url(wd.current_url):
            return True
        else:
            return False