#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Contact fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import url
from tests.model.contact import Contact
from tests.utils import strs


class ContactHelper:
    """Class for represent Contact."""
    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_contacts_page(self):
        """Open contacts page."""
        self.app.open.open_url(url.HOME_URL)

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

    def select_contact_by_index(self, index):
        """Select contact by index."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        """Select first contact."""
        self.select_contact_by_index(0)

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
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        """Modify first contact editing requirements fields."""
        self.modify_contact_by_index(0, new_contact_data)

    def  modify_contact_by_index(self, index, new_contact_data):
        """Modify contact by index editing requirements fields."""
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_element_by_css_selector("[title=Edit]").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        """Delete contact by index."""
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        """Delete first contact."""
        self.delete_contact_by_index(0)

    def delete_all_contacts(self):
        """Delete all contacts."""
        wd = self.app.wd
        self.open_contacts_page()
        # check that the contact's list is not empty and check contact elements
        if len(wd.find_elements_by_css_selector("#content input")) == 5:
            pass
        else:
            # check contact's elements
            elements = wd.find_elements_by_name("selected[]")
            [el.click() for el in elements]
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        """Get the count of existing contacts."""
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_list_of_contacts(self):
        """Get list of contacts."""
        wd = self.app.wd
        self.open_contacts_page()
        self.contact_cache = []
        for el in wd.find_elements_by_name("selected[]"):
            id = el.get_attribute("value")
            ext_text = el.get_attribute("title")
            text = strs.normal_select_title(ext_text)
            email = el.get_attribute("accept")
            self.contact_cache.append(Contact(id=id, name=text, email=email))
        return self.contact_cache