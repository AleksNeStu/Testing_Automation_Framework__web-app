#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from data.group import Group
from generator.generic import random_data as rd

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        # wd.driver.switch_to.alert().text
        return True
    except:
        return False


class group_add_data(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.group_data = Group(name=rd("name_",5), header=rd("header_",5),
                                footer=rd("footer_",5))
        self.login_data = {"username": "admin", "password": "secret"}

    def test_add_Group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, **self.login_data)
        self.open_groups_page(wd)
        self.create_group(wd, self.group_data)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://lamp/addressbook/group.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        # wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()