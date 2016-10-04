#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group fixture"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        # check that the group's list is not empty and check group elements
        if len(wd.find_elements_by_css_selector("#content input")) == 6:
            pass
        else:
            # check group's elements
            elements = wd.find_elements_by_name("selected[]")
            for i in range(1, len(elements)+1):
                wd.find_element_by_css_selector("#content input:nth-of-type({})".
                                                format(i+3)).click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()