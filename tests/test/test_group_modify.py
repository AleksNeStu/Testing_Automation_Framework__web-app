#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modifying groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_modify_name_of_some_group(app):
    """Check the possibility to modify some group's name."""
    if app.group.count_of_groups_via_groups() == 0:
        app.group.create_group_via_groups(Group())
    group_name = Group(name=r_data(data.GROUP_NAME_NEW))
    first_groups = app.group.list_of_groups_via_groups()
    group_name.id = first_groups[0].id
    index = randrange(len(first_groups))
    app.group.modify_group_via_groups(index, group_name)
    assert len(first_groups) == app.group.count_of_groups_via_groups()
    actual_groups = app.group.list_of_groups_via_groups()
    expected_groups = first_groups[:index] + [group_name] + first_groups[index+1:]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))

def test_modify_some_group(app):
    """Check the possibility to modify some group."""
    if app.group.count_of_groups_via_groups() == 0:
        app.group.create_group_via_groups(Group())
    first_groups = app.group.list_of_groups_via_groups()
    group = Group(name=r_data(data.GROUP_NAME_NEW),
                      header=r_data(data.GROUP_HEADER_NEW),
                      footer=r_data(data.GROUP_FOOTER_NEW))
    group.id = first_groups[0].id
    index = randrange(len(first_groups))
    app.group.modify_group_via_groups(index, group)
    assert len(first_groups) == app.group.count_of_groups_via_groups()
    actual_groups = app.group.list_of_groups_via_groups()
    expected_groups = first_groups[:index] + [group] + first_groups[index+1:]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))