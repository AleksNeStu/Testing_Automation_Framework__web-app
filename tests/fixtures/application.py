#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from selenium.webdriver.firefox.webdriver import WebDriver
from session import SessionHelper
from group import GroupHelper
from contact import ContactHelper
from open import OpenHelper


class Application():
    """Class for represent Application."""
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open = OpenHelper(self)

    def destroy(self):
        """Quit method."""
        self.wd.quit()

    def check_fixture_valid(self):
        """Fixture validation."""
        try:
            self.wd.current_window_handle
            return True
        except:
            return False