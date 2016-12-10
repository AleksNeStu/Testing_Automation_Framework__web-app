#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from selenium.webdriver.firefox.webdriver import WebDriver

from contact import ContactHelper
from group import GroupHelper
from open import OpenHelper
from session import SessionHelper


class Application():
    """Class for represent Application."""
    def __init__(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open = OpenHelper(self)

    def destroy(self):
        """Web driver quit method."""
        self.wd.quit()

    def is_valid(self):
        """Fixture validation."""
        self.wd = WebDriver()
        try: self.wd.current_url; return True
        except: return False