#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Session fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data


class SessionHelper:
    """Class for represent Session."""
    def __init__(self, app):
        self.app = app

    def _get_loged_user(self):
        """Get username of logged user."""
        wd = self.app.wd
        return wd.find_element_by_css_selector("#top b").text[1:-1]

    def _change_field_value(self, field_name, text):
        """Change field value if test exist (is not None)."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def is_logged_in(self):
        """Check if somebody logged."""
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        """Check if user with username logged."""
        return self._get_loged_user() == username

    def login(self, username, password):
        """Login to the web-app used credentials."""
        wd = self.app.wd
        self.app.open.open_url(self.app.url.HOME_URL)
        self._change_field_value("user", username)
        self._change_field_value("pass", password)
        wd.find_element_by_css_selector("input[type=submit]").click()

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
        if self.is_logged_in(): self.logout()

    def check_session(self):
        """Check the actual session status."""
        wd = self.app.wd
        if wd.current_url is not None and len(
                wd.find_elements_by_link_text("Logout")) == 1: return True
        else: return False