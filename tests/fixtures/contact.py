#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Contact fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import url


class ContactHelper:
    """Class for represent Contact."""
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        """Open contact page."""
        self.app.open.open_link(url._ADD_NEW)

    def create(self, contact):
        """Create contact filling requirements fields."""
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[2]").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()