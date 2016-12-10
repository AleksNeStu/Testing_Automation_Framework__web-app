#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Fixture for contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import url
from tests.model.contact import Contact
from tests.utils import strs


class ContactHelper:
    """Class helper for work with contacts objects."""
    def __init__(self, app):
        self.app = app

    # Common
    contact_cache = None

    def _change_field_value(self, field_name, text):
        """Change field value to 'text' if it is not None."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # Open URLs and links
    def open_contacts_page(self):
        """Open contacts page (home page) via get url."""
        self.app.open.open_url(url.HOME_URL)

    def open_add_form(self):
        """Open contacts add form via clicked on link."""
        self.app.open.open_link(url._ADD_NEW)

    # Contacts (home) page
    def _contacts_select_by_index(self, index):
        """Select checkbox for contact by index on contacts page to make actions."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _contacts_select_edit(self):
        """Select 'Edit' element (link) on contacts page to open modification form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Edit]").click()

    def _contacts_select_select_all(self):
        """Select "Select all" checkbox on contacts page to select all contacts checkboxes."""
        wd = self.app.wd
        if len(wd.find_elements_by_id("content input")) == 5: pass
        else: wd.find_element_by_id("MassCB").click()

    def _contacts_select_details(self):
        """Select 'Details' element (link) on contacts page to open details form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Details]").click()

    def _contacts_select_delete(self):
        """Select 'Delete' button on contacts page to delete selected contact(s)."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[value=Delete]").click()

    def _contacts_push_ok(self):
        """Push 'OK' button on appeared js window on contacts page to accept action."""
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def contacts_open_edit_form(self, index):
        """Open contact's editing form on contacts page."""
        self._contacts_select_by_index(index)
        self._contacts_select_edit()

    def contacts_open_details_form(self, index):
        """Open contact's details form on contacts page."""
        self._contacts_select_by_index(index)
        self._contacts_select_details()

    # Creation form
    def _creation_select_next(self):
        """Select 'Next' button on first creation form to continue actions."""
        wd = self.app.wd
        wd.find_element_by_css_selector("input[name=quickadd]").click()

    def _creation_select_enter(self):
        """Select 'Enter' button on second creation form to submit action."""
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def creation_fill_form(self, contact):
        """Fill data on first and second creation forms."""
        self._change_field_value("address", contact.first_name)
        self._creation_select_next()
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    # Editing form
    def _editing_select_update(self):
        """Select 'Update' button on editing form to update entered data."""
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def editing_fill_form(self, contact):
        """Fill data on editing forms."""
        self._change_field_value("firstname", contact.first_name)
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    # Creation, Deletion, Modification procedures for contact(s)
    def create_contact(self, contact):
        """Create new contact."""
        self.open_add_form()
        self.creation_fill_form(contact)
        self._creation_select_enter()
        self.contact_cache = None

    def modify_contact(self, index, new_contact):
        """Modify contact by 'index' according object's data 'new_contact'."""
        self.open_contacts_page()
        self.contacts_open_edit_form(index)
        self.editing_fill_form(new_contact)
        self._editing_select_update()
        self.contact_cache = None

    def delete_contact_via_home(self, index):
        """Delete contact by index via home (contacts) page."""
        self.open_contacts_page()
        self._contacts_select_by_index(index)
        self._contacts_select_delete()
        self._contacts_push_ok()
        self.contact_cache = None

    def delete_all_contacts_via_home(self):
        """Delete contact by index via home (contacts) page."""
        self.open_contacts_page()
        self._contacts_select_select_all()
        self._contacts_select_delete()
        self._contacts_push_ok()
        self.contact_cache = None

    def get_count_of_contacts_via_home(self):
        """Get the count of contacts objects via home (contacts) page."""
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_list_of_contacts_via_home(self):
        """Get list of contacts objects via home (contacts) page."""
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