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
        """Change field value (text)."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def _get_field_value(self, field_name):
        """Get field value (text)"""
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

    # Open URLs and links
    def open_contacts_page(self):
        """Open contacts page (home page) via get url."""
        self.app.open.open_url(url.HOME_URL)

    def open_add_form(self):
        """Open contacts add form via clicked on link."""
        self.app.open.open_link(url._ADD_NEW)

    # Contacts (home) page
    def _select_by_index_via_home(self, index):
        """Select checkbox for contact by index on contacts page to make actions."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _select_edit_via_home(self):
        """Select 'Edit' element (link) on contacts page to open modification form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Edit]").click()

    def _select_select_all_via_home(self):
        """Select "Select all" checkbox on contacts page to select all contacts checkboxes."""
        wd = self.app.wd
        if len(wd.find_elements_by_id("content input")) == 5: pass
        else: wd.find_element_by_id("MassCB").click()

    def _select_details_via_home(self):
        """Select 'Details' element (link) on contacts page to open details form."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Details]").click()

    def _select_delete_via_home(self):
        """Select 'Delete' button on contacts page to delete selected contact(s)."""
        wd = self.app.wd
        wd.find_element_by_css_selector("[value=Delete]").click()

    def _push_ok_js(self):
        """Push 'OK' button on appeared js window on contacts page to accept action."""
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def open_edit_form_via_home(self, index):
        """Open contact's editing form on contacts page."""
        self._select_by_index_via_home(index)
        self._select_edit_via_home()

    def open_details_form_via_home(self, index):
        """Open contact's details form on contacts page."""
        self._select_by_index_via_home(index)
        self._select_details_via_home()

    # Create form
    def _create_select_next(self):
        """Select 'Next' button on first create form to continue actions."""
        wd = self.app.wd
        wd.find_element_by_css_selector("input[name=quickadd]").click()

    def _select_enter_via_create(self):
        """Select 'Enter' button on second create form to submit action."""
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_form_via_create(self, contact):
        """Fill data on first and second create forms."""
        self._change_field_value("address", contact.first_name)
        self._create_select_next()
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("home", contact.home_phone)
        self._change_field_value("mobile", contact.mobile_phone)
        self._change_field_value("work", contact.work_phone)
        self._change_field_value("phone2", contact.secondary_phone)
        self._change_field_value("email", contact.email)

    # Edit form
    def _select_update_via_edit(self):
        """Select 'Update' button on edit form to update entered data."""
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def _fill_form_via_edit(self, contact):
        """Fill data on edit forms."""
        self._change_field_value("firstname", contact.first_name)
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("email", contact.email)

    # Create, Delete, Modify procedures for contact(s)
    def create_contact(self, contact):
        """Create new contact."""
        self.open_add_form()
        self.fill_form_via_create(contact)
        self._select_enter_via_create()
        self.contact_cache = None

    def modify_contact(self, index, new_contact):
        """Modify contact by 'index' according object's data 'new_contact'."""
        self.open_contacts_page()
        self.open_edit_form_via_home(index)
        self._fill_form_via_edit(new_contact)
        self._select_update_via_edit()
        self.contact_cache = None

    def delete_contact_via_home(self, index):
        """Delete contact by index via home (contacts) page."""
        self.open_contacts_page()
        self._select_by_index_via_home(index)
        self._select_delete_via_home()
        self._push_ok_js()
        self.contact_cache = None

    def delete_all_contacts_via_home(self):
        """Delete all contact via home (contacts) page."""
        self.open_contacts_page()
        self._select_select_all_via_home()
        self._select_delete_via_home()
        self._push_ok_js()
        self.contact_cache = None

    def count_of_contacts_via_home(self):
        """Get the count of contacts objects via home (contacts) page."""
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def list_of_contacts_via_home(self):
        """Get list of contacts objects via home (contacts) page."""
        wd = self.app.wd
        self.open_contacts_page()
        self.contact_cache = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
            full_name = cells[2].text
            firstname = strs.full_name_to_list_of_parts(full_name)[1]
            lastname = strs.full_name_to_list_of_parts(full_name)[0]
            all_phones = cells[5].text
            homephone = strs.all_phones_to_list_of_parts(all_phones)[0]
            mobilephone = strs.all_phones_to_list_of_parts(all_phones)[1]
            workphone = strs.all_phones_to_list_of_parts(all_phones)[2]
            secondaryphone = strs.all_phones_to_list_of_parts(all_phones)[3]
            email = cells[4].text
            self.contact_cache.append(Contact(
                id=id, first_name=firstname, last_name=lastname,
                home_phone=homephone, mobile_phone=mobilephone,
                work_phone=workphone, secondary_phone=secondaryphone,
                email=email))
        return self.contact_cache

    def contact_info_via_edit(self, index):
        """Get by index contact info via edit form."""
        self.open_contacts_page()
        self.open_edit_form_via_home(index)
        id = self._get_field_value("id")
        firstname = self._get_field_value("firstname")
        lastname = self._get_field_value("lastname")
        homephone = self._get_field_value("home")
        mobilephone = self._get_field_value("mobile")
        workphone = self._get_field_value("work")
        secondaryphone = self._get_field_value("phone2")
        email = self._get_field_value("email")
        return Contact(
            id=id, first_name=firstname, last_name=lastname,
            home_phone=homephone, mobile_phone=mobilephone,
            work_phone=workphone, secondary_phone=secondaryphone,
            email=email)