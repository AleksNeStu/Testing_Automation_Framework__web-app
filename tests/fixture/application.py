#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Application fixture"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from selenium.webdriver.firefox.webdriver import WebDriver
from session import SessionHelper
from group import GroupHelper
from contact import ContactHelper
from open import OpenHelper
# from tests.model.group import Group
# from tests.generator.generic import random_data as r_data


class Application():

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.open = OpenHelper(self)
        # login_data = {"login": "admin", "password": "secret"}
        # group_data = Group(name=r_data("name_", 5), header=r_data("header_", 5),
        #                    footer=r_data("footer_", 5))

    def destroy(self):
        self.wd.quit()

    def check_fixture_valid(self):
        try:
            self.wd.current_window_handle
            return True
        except:
            return False