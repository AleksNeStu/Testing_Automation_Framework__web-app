#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for creating groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_add_group(app):
    """Check the possibility to create new group."""
    first_groups = app.group.get_list_of_groups()
    group = Group(name=r_data(data.GROUP_NAME),
                  header=r_data(data.GROUP_HEADER),
                  footer=r_data(data.GROUP_FOOTER))
    app.group.create(group)
    assert len(first_groups) + 1 == app.group.count()
    actual_groups = app.group.get_list_of_groups()
    group.id = actual_groups[-1].id
    expected_groups = first_groups + [group]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_groups, actual_groups))

def test_add_empty_group(app):
    """Check the possibility to create new empty group."""
    first_groups = app.group.get_list_of_groups()
    group = Group()
    app.group.create(group)
    assert len(first_groups) + 1 == app.group.count()
    actual_groups = app.group.get_list_of_groups()
    group.id = actual_groups[-1].id
    expected_groups = first_groups + [group]
    assert (
        sorted(expected_groups, key=Group.id_or_max) ==
        sorted(actual_groups, key=Group.id_or_max),
        messages.ERR_MSG_FORMAT.format(expected_groups, actual_groups))