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

    def _select_contact_by_index(self, index):
        """Select contact by index."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _select_next(self):
        """Select Next button to continue actions."""
        wd = self.app.wd
        wd.find_element_by_css_selector("input[name=quickadd]").click()

    def _select_submit(self):
        """Select submit button to submit action."""
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def _select_edit(self):
        """Select edit element to open modification form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Edit]").click()

    def _select_details(self):
        """Select details element to open details form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Details]").click()

    def _select_update(self):
        """Select update button to update entered data."""
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def _select_delete(self):
        """Select delete button to delete contact(s)."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[value=Delete]").click()

    def _push_accept(self):
        """Push OK button accept action raised by js."""
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def _select_select_all(self):
        """Select all button to select all checkboxes."""
        wd = self.app.wd
        if len(wd.find_elements_by_id("content input")) == 5: pass
        else: wd.find_element_by_id("MassCB").click()

    def open_edit_form(self, index):
        """Open contact's edit form."""
        self._select_contact_by_index(index)
        self._select_edit()

    def open_details_form(self, index):
        """Open contact's details form."""
        self._select_contact_by_index(index)
        self._select_details()

    def fill_contact_form(self, contact):
        """Fill contact forms of new data or modify exist data."""
        self._change_field_value("firstname", contact.first_name)
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    def fill_data(self, contact):
        """Fill contact data."""
        self._change_field_value("address", contact.first_name)
        self._select_next()
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    def create(self, contact):
        """Create contact filling requirements fields."""
        self.open_contacts_add_page()
        self.fill_data(contact)
        self._select_submit()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        """Modify contact by index editing requirements fields."""
        self.open_contacts_page()
        self.open_edit_form(index)
        self.fill_contact_form(new_contact_data)
        self._select_update()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        """Delete contact by index."""
        self.open_contacts_page()
        self._select_contact_by_index(index)
        self._select_delete()
        self._push_accept()
        self.contact_cache = None

    def delete_all_contacts(self):
        """Delete all contacts."""
        wd = self.app.wd
        self.open_contacts_page()
        # check that the contact's list is not empty and check contact elements
        self._select_select_all()
        self._select_delete()
        self._push_accept()
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
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            fullname = cells[2].text
            firstname = strs.split_full_name_to_tuple(fullname)[1]
            lastname = strs.split_full_name_to_tuple(fullname)[0]
            email = cells[4].text
            self.contact_cache.append(Contact(
                id=id, first_name=firstname, last_name=lastname, email=email))
        return self.contact_cache