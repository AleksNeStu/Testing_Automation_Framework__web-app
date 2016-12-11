#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from model.group import Group
from tests.constants import url
from tests.utils import strings


class GroupHelper:
    """Class for represent Group."""
    def __init__(self, app):
        self.app = app

    group_cache = None

    def open_groups_page(self):
        """Open groups page."""
        self.app.open.open_link(url._GROUPS)

    def return_to_groups_page(self):
        """Return to groups page from another tab."""
        self.app.open.open_link(url._GROUPS_)

    def _change_field_value(self, field_name, text):
        """Change field value if test exist (is not None)."""
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        """Fill group forms of new data or modify exist data."""
        self._change_field_value("group_name", group.name)
        self._change_field_value("group_header", group.header)
        self._change_field_value("group_footer", group.footer)

    def select_group_by_index(self, index):
        """Select group by index."""
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        """Select first group."""
        self.select_group_by_index(0)

    def create(self, group):
        """Create group filling requirements fields."""
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill data
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        """Modify first group editing requirements fields."""
        self.modify_group_by_index(0, new_group_data)

    def  modify_group_by_index(self, index, new_group_data):
        """Modify group by index editing requirements fields."""
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def delete_group_by_index(self, index):
        """Delete group by index."""
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def delete_first_group(self):
        """Delete first group."""
        self.delete_group_by_index(0)

    def delete_all_groups(self):
        """Delete all groups."""
        wd = self.app.wd
        self.open_groups_page()
        # check that the group's list is not empty and check group elements
        if len(wd.find_elements_by_css_selector("#content input")) == 6:
            pass
        else:
            # check group's elements
            elements = wd.find_elements_by_name("selected[]")
            for i in range(1, len(elements)+1):
                wd.find_element_by_css_selector(
                    "#content input:nth-of-type({})".format(i+3)).click()
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def count(self):
        """Get the count of existing groups."""
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_list_of_groups(self):
        """Get list of groups."""
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for el in wd.find_elements_by_name("selected[]"):
                id = el.get_attribute("value")
                ext_text = el.get_attribute("title")
                text = strings.normal_select_title(ext_text)
                self.group_cache.append(Group(id=id, name=text))
        return self.group_cache