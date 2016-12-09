#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modification groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.generator.generic import random_data as r_data
from tests.model.group import Group
from tests.constants import data


def test_modify_name_of_first_group(app):
    """Check the possibility of modifying group's name."""
    if app.group.count() == 0:
        app.group.create(Group())
    new_group_name = Group(name=r_data(data.GROUP_NAME_NEW))
    old_groups = app.group.get_list_of_groups()
    app.group.modify_first_group(new_group_name)
    new_groups = app.group.get_list_of_groups()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group(app):
    """Check the possibility of modifying group's name, header, footer."""
    if app.group.count() == 0:
        app.group.create(Group())
    old_groups = app.group.get_list_of_groups()
    new_group = Group(name=r_data(data.GROUP_NAME_NEW),
                      header=r_data(data.GROUP_HEADER_NEW),
                      footer=r_data(data.GROUP_FOOTER_NEW))
    app.group.modify_first_group(new_group)
    new_groups = app.group.get_list_of_groups()
    assert len(old_groups) == len(new_groups)