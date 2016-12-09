#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Contact fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import url
from tests.model.contact import Contact


class ContactHelper:
    """Class for represent Contact."""
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        """Open contacts page."""
        self.app.open.open_link(url._HOME)

    def open_contacts_add_page(self):
        """Open contacts add page."""
        self.app.open.open_link(url._ADD_NEW)

    def _change_field_value(self, field_name, text):
        """Change field value if test exist (is not None)."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        """Fill contact forms of new data or modify exist data."""
        self._change_field_value("firstname", contact.name)
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    def select_first_contact(self):
        """Select first contact."""
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def create(self, contact):
        """Create contact filling requirements fields."""
        wd = self.app.wd
        # init contact creation
        self.open_contacts_add_page()
        # fill data
        self._change_field_value("address", contact.name)
        wd.find_element_by_css_selector("input[name=quickadd]").click()
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.open_contacts_page()

    def  modify_first_contact(self, new_contact_data):
        """Modify contact editing requirements fields."""
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_contacts_page()

    def delete_first_contact(self):
        """Delete first contact on the contact page."""
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()

    def delete_all_contacts(self):
        """Delete all contacts on the contact page."""
        wd = self.app.wd
        self.open_contacts_page()
        # check that the contact's list is not empty and check contact elements
        if len(wd.find_elements_by_css_selector("#content input")) == 5:
            pass
        else:
            # check contact's elements
            elements = wd.find_elements_by_name("selected[]")
            [el.click() for el in elements]
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.open_contacts_page()

    def count(self):
        """Get the count of existing contacts."""
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_list_of_contacts(self):
        """Get list of contacts from groups page."""
        wd = self.app.wd
        self.open_contacts_page()
        ls_contacts = []
        for el in wd.find_elements_by_css_selector(
                "#maintable>tbody>tr>td:nth-child(3)"):
            full_name = el.text.split()
            if len(full_name) == 2:
                ls_contacts.append(Contact(name=full_name[0],
                                          last_name=full_name[1]))
            if len(full_name) == 1:
                ls_contacts.append(Contact(name=full_name[0]))
        return ls_contacts