#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Fixture for contacts."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.model.contact import Contact
from tests.utils import strings


class ContactHelper:
    """Class helper for work with contacts objects."""
    def __init__(self, app):
        self.app = app

    # Common
    contacts_cache = None

    def _fill_form_common(self, contact):
        """Common (for create, edit forms) data for filling contact."""
        self._change_field_value("lastname", contact.last_name)
        self._change_field_value("middlename", contact.middle_name)
        self._change_field_value("address", contact.address)
        self._change_field_value("email", contact.email)
        self._change_field_value("email2", contact.email2)
        self._change_field_value("email3", contact.email3)
        self._change_field_value("home", contact.home_phone)
        self._change_field_value("mobile", contact.mobile_phone)
        self._change_field_value("work", contact.work_phone)
        self._change_field_value("phone2", contact.secondary_phone)

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
        self.app.open.open_url(self.app.url.HOME_URL)

    def open_add_form(self):
        """Open contacts add form via clicked on link."""
        self.app.open.open_link(self.app.url._ADD_NEW)

    # Contacts (home) page
    def select_contact_by_index_home(self, index):
        """Select checkbox for contact by index on contacts page to make
        actions.
        """
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def click_edit_contact_by_index_home(self, index):
        """Select 'Edit' element (link) for contact by index on contacts page
        to open modification form.
        """
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title=Edit]")[index].click()

    def click_contact_details_by_index_home(self, index):
        """Select 'Details' element (link) on contacts page to open details
        form.
        """
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title=Details]")[index].click()

    def click_select_all_contacts_home(self):
        """Select "Select all" checkbox on contacts page to select all contacts
        checkboxes.
        """
        wd = self.app.wd
        if len(wd.find_elements_by_id("content input")) == 5: pass
        else: wd.find_element_by_id("MassCB").click()

    def click_delete_contacts_home(self):
        """Select 'Delete' button on contacts page to delete selected
        contact(s).
        """
        wd = self.app.wd
        wd.find_element_by_css_selector("[value=Delete]").click()

    def accept_deletion_action_js(self):
        """Push 'OK' button on appeared js window on contacts page to
        accept action.
        """
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def open_edit_form_home(self, index):
        """Open contact's editing form on contacts page."""
        self.select_contact_by_index_home(index)
        self.click_edit_contact_by_index_home(index)

    def open_details_form_home(self, index):
        """Open contact's details form on contacts page."""
        self.select_contact_by_index_home(index)
        self.click_contact_details_by_index_home(index)

    def count_of_contacts_home(self):
        """Get the count of contacts objects via home (contacts) page."""
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def list_of_contacts_home(self):
        """Get list of contacts objects via home (contacts) page."""
        wd = self.app.wd
        self.open_contacts_page()
        self.contacts_cache = []
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            id = (cells[0].find_element_by_tag_name("input").
                  get_attribute("value"))
            fullname = cells[2].text
            address = cells[3].text
            allemails = cells[4].text
            allphones = cells[5].text
            self.contacts_cache.append(Contact(
                id=id, full_name_home=fullname, address=address,
                all_emails_home=allemails, all_phones_home=allphones))
        return self.contacts_cache

    # Create form
    def click_next_form_create(self):
        """Select 'Next' button on first create form to continue actions."""
        wd = self.app.wd
        wd.find_element_by_css_selector("input[name=quickadd]").click()

    def click_enter_data_create(self):
        """Select 'Enter' button on second create form to submit action."""
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_form_create(self, contact):
        """Fill data on first and second create forms."""
        self._change_field_value("address", contact.first_name)
        self.click_next_form_create()
        self._fill_form_common(contact)

    # Edit form
    def click_update_data_edit(self):
        """Select 'Update' button on edit form to update entered data."""
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def fill_form_edit(self, contact):
        """Fill data on edit forms."""
        self._change_field_value("firstname", contact.first_name)
        self._fill_form_common(contact)

    def contact_info_edit(self, index):
        """Get by index on home page contact info via edit form."""
        self.open_contacts_page()
        self.open_edit_form_home(index)
        id = self._get_field_value("id")
        firstname = self._get_field_value("firstname")
        middlename = self._get_field_value("middlename")
        lastname = self._get_field_value("lastname")
        address = self._get_field_value("address")
        email = self._get_field_value("email")
        email2 = self._get_field_value("email2")
        email3 = self._get_field_value("email3")
        homephone = self._get_field_value("home")
        mobilephone = self._get_field_value("mobile")
        workphone = self._get_field_value("work")
        secondaryphone = self._get_field_value("phone2")
        return Contact(
            id=id, first_name=firstname, middle_name=middlename,
            last_name=lastname, address=address, email=email, email2=email2,
            email3=email3, home_phone=homephone, mobile_phone=mobilephone,
            work_phone=workphone, secondary_phone=secondaryphone)

    # Details form
    def contact_info_details(self, index):
        """Get by index on home page contact info via details form."""
        wd = self.app.wd
        self.open_contacts_page()
        self.open_details_form_home(index)
        fullinfo = wd.find_element_by_id("content").text
        id = self._get_field_value("id")
        fullname = wd.find_element_by_css_selector("#content b").text
        homephone = strings._search_string_in_raw_text(fullinfo, r"H: (.*)")
        mobilephone = strings._search_string_in_raw_text(fullinfo, r"M: (.*)")
        workphone = strings._search_string_in_raw_text(fullinfo, r"W: (.*)")
        secondaryphone = strings._search_string_in_raw_text(fullinfo, r"P: (.*)")
        allemails = strings._findall_strings_in_raw_text(fullinfo,
                                                         r"[\w\.-]+@[\w\.-]+")
        return Contact(
            id=id, full_name_details=fullname, home_phone=homephone,
            mobile_phone=mobilephone, work_phone=workphone,
            secondary_phone=secondaryphone, all_emails_details=allemails)

    # Create, Modify, Delete procedures for contact(s)
    def create_contact_add(self, contact):
        """Create new contact."""
        self.open_add_form()
        self.fill_form_create(contact)
        self.click_enter_data_create()
        self.contacts_cache = None

    def modify_contact_home(self, index, new_contact):
        """Modify contact by 'index' according object's data 'new_contact'."""
        self.open_contacts_page()
        self.open_edit_form_home(index)
        self.fill_form_edit(new_contact)
        self.click_update_data_edit()
        self.contacts_cache = None

    def delete_contact_home(self, index):
        """Delete contact by index via home (contacts) page."""
        self.open_contacts_page()
        self.select_contact_by_index_home(index)
        self.click_delete_contacts_home()
        self.accept_deletion_action_js()
        self.contacts_cache = None

    def delete_all_contacts_home(self):
        """Delete all contact via home (contacts) page."""
        self.open_contacts_page()
        self.click_select_all_contacts_home()
        self.click_delete_contacts_home()
        self.accept_deletion_action_js()
        self.contacts_cache = None