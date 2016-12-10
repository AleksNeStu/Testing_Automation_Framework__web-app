#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modification groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_modify_name_of_first_group(app):
    """Check the possibility of modifying group's name."""
    if app.group.count() == 0:
        app.group.create(Group())
    group_name = Group(name=r_data(data.GROUP_NAME_NEW))
    first_groups = app.group.get_list_of_groups()
    group_name.id = first_groups[0].id
    app.group.modify_first_group(group_name)
    assert len(first_groups) == app.group.count()
    actual_groups = app.group.get_list_of_groups()
    expected_groups = [group_name] + first_groups[1:]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_groups, actual_groups))

def test_modify_first_group(app):
    """Check the possibility of modifying group's name, header, footer."""
    if app.group.count() == 0:
        app.group.create(Group())
    first_groups = app.group.get_list_of_groups()
    group = Group(name=r_data(data.GROUP_NAME_NEW),
                      header=r_data(data.GROUP_HEADER_NEW),
                      footer=r_data(data.GROUP_FOOTER_NEW))
    group.id = first_groups[0].id
    app.group.modify_first_group(group)
    assert len(first_groups) == app.group.count()
    actual_groups = app.group.get_list_of_groups()
    expected_groups = [group] + first_groups[1:]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_groups, actual_groups))