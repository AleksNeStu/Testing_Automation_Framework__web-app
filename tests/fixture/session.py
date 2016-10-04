#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Session fixture"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open.open_group_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def check_session(self):
        wd = self.app.wd
        self.app.open.open_home_page()
        if len(wd.find_elements_by_link_text("Logout")) == 1:
            return True
        else:
            return False