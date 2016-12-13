#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from selenium import  webdriver

from contact import ContactHelper
from group import GroupHelper
from open import OpenHelper
from session import SessionHelper
from tests.constants.url import URL


class Application():
    """Class for represent Application."""
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open = OpenHelper(self)
        self.url = URL(base_url)

    def destroy(self):
        """Web driver quit method."""
        self.wd.quit()

    def is_valid(self):
        """Fixture validation."""
        try: self.wd.current_url; return True
        except: return False