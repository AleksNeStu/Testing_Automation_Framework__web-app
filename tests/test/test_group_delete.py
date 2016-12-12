#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for deleting groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

from tests.constants import messages
from tests.model.group import Group


def test_del_some_group(app):
    """Check the possibility to delete some group via home (contacts) page."""
    if app.group.count_of_groups_via_groups() == 0:
        app.group.create_group_via_groups(Group())
    first_groups = app.group.list_of_groups_via_groups()
    index = randrange(len(first_groups))
    app.group.delete_group_via_groups(index)
    assert len(first_groups) - 1 == app.group.count_of_groups_via_groups()
    actual_groups = app.group.list_of_groups_via_groups()
    expected_groups = first_groups[:index] + first_groups[(index + 1):]
    assert expected_groups == actual_groups, messages.COMPARE_EXP_VS_GOT.format(
        expected_groups, actual_groups)

def test_del_all_groups(app):
    """Check the possibility to delete all groups via home (contacts) page."""
    if app.group.count_of_groups_via_groups() == 0:
        [app.group.create_group_via_groups(Group()) for _ in xrange(3)]
    app.group.delete_all_groups_via_groups()
    actual_groups = app.group.list_of_groups_via_groups()
    assert len(actual_groups) == app.group.count_of_groups_via_groups() == 0