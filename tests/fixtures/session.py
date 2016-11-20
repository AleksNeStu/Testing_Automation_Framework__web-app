#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Session fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data
from tests.constants import url

class SessionHelper:
    """Class for represent Session."""
    def __init__(self, app):
        self.app = app

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("#top b").text == "("+username+")"


    def login(self, username, password):
        """Login to the web-app used credentials."""
        wd = self.app.wd
        self.app.open.open_url(url.HOME_URL)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_login(self, username, password):
        """Intellectual login to the web-app used credentials."""
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_login_as_admin(self):
        """Intellectual login to the web-app used admin credentials."""
        self.ensure_login(data.LOGIN, data.PASSWORD)

    def logout(self):
        """Logout from the web-app."""
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        """Intellectual logout from the web-app."""
        if self.is_logged_in():
            self.logout()

    def check_session(self):
        """Check the actual session status."""
        wd = self.app.wd
        self.app.open.open_url(url.HOME_URL)
        if len(wd.find_elements_by_link_text("Logout")) == 1:
            return True
        else:
            return False