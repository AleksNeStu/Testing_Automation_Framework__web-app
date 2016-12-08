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

    def return_to_contacts_page(self):
        """Return to contact page from another tab."""
        self.app.open.open_link(url._HOME)

    def change_field_value(self, field_name, text):
        """Change field value if test exist (is not None)."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        """Fill contact forms of new data or modify exist data."""
        self.change_field_value("firstname", contact.name)
        self.change_field_value("email", contact.email)

    def select_first_contact(self):
        """Select first contact."""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def create(self, contact):
        """Create contact filling requirements fields."""
        wd = self.app.wd
        # init contact creation
        self.open_contacts_page()
        # fill data
        self.change_field_value("address", contact.name)
        wd.find_element_by_css_selector("input[name=quickadd]").click()
        self.change_field_value("email", contact.email)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_contacts_page()

    def  modify_first_contact(self, new_contact_data):
        """Modify contact editing requirements fields."""
        wd = self.app.wd
        self.app.open.open_link(url._HOME)
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()

    def count(self):
        """Get the count of existing contacts."""
        wd = self.app.wd
        self.app.open.open_link(url._HOME)
        return len(wd.find_elements_by_name("selected[]"))