#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Fixture for groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from model.group import Group
from utils import strings


class GroupHelper:
    """Class helper for work with groups objects."""
    def __init__(self, app):
        self.app = app

    # Common
    group_cache = None

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
    def open_groups_page(self):
        """Open groups page via clicked on link."""
        self.app.open.open_link(self.app.url._GROUPS)

    def return_to_groups_page(self):
        """Return to groups page from another tab via clicked on link."""
        self.app.open.open_link(self.app.url._GROUPS_)

    # Groups page
    def select_group_by_index_groups(self, index):
        """Select checkbox for group by index on groups page to make
        actions.
        """
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def click_new_group_groups(self):
        """Select 'New group' button on groups page to open group create form.
        """
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def click_edit_group_groups(self):
        """Select 'Edit group' button on groups page to open group edit form.
        """
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def click_delete_groups_groups(self):
        """Select 'Delete group' button on groups page to delete
        selected group(s).
        """
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def select_all_groups_groups(self):
        """Select all checkboxes on groups page"""
        wd = self.app.wd
        elements = wd.find_elements_by_name("selected[]")
        [el.click() for el in elements]

    def open_edit_form_groups(self, index):
        """Open groups's editing form on groups page."""
        self.select_group_by_index_groups(index)
        self.click_edit_group_groups()

    def count_of_groups_groups(self):
        """Get the count of groups objects via groups page."""
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def list_of_groups_groups(self):
        """Get list of groups objects via groups page."""
        wd = self.app.wd
        self.open_groups_page()
        self.group_cache = []
        for el in wd.find_elements_by_name("selected[]"):
            id = el.get_attribute("value")
            full_group_name = el.get_attribute("title")
            groupname = strings.normal_select_title(full_group_name)
            self.group_cache.append(Group(id=id, name=groupname))
        return self.group_cache

    # Create form
    def click_enter_data_create(self):
        """Select 'Enter information' button on create form to submit action.
        """
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_form_create_or_edit(self, group):
        """Fill data on create form."""
        self._change_field_value("group_name", group.name)
        self._change_field_value("group_header", group.header)
        self._change_field_value("group_footer", group.footer)

    # Edit form
    def click_update_data_edit(self):
        """Select 'Update' button on edit form to update entered data."""
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    # Create, Modify, Delete procedures for groups(s)
    def create_group_groups(self, group):
        """Create new group."""
        self.open_groups_page()
        self.click_new_group_groups()
        self.fill_form_create_or_edit(group)
        self.click_enter_data_create()
        self.group_cache = None

    def modify_group_groups(self, index, new_group):
        """Modify group by 'index' according object's data 'new_group'."""
        self.open_groups_page()
        self.open_edit_form_groups(index)
        self.fill_form_create_or_edit(new_group)
        self.click_update_data_edit()
        self.group_cache = None

    def delete_group_groups(self, index):
        """Delete group by index via groups page."""
        self.open_groups_page()
        self.select_group_by_index_groups(index)
        self.click_delete_groups_groups()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_all_groups_groups(self):
        """Delete all groups via home (contacts) page."""
        self.open_groups_page()
        self.select_all_groups_groups()
        self.click_delete_groups_groups()
        self.group_cache = None