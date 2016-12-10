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
    if app.group.count() == 0:
        app.group.create(Group())
    first_groups = app.group.get_list_of_groups()
    index = randrange(len(first_groups))
    app.group.delete_group_by_index(index)
    assert len(first_groups) - 1 == app.group.count()
    actual_groups = app.group.get_list_of_groups()
    expected_groups = first_groups[:index] + first_groups[(index + 1):]
    assert expected_groups == actual_groups, messages.ERR_MSG_FORMAT.format(
        expected_groups, actual_groups)

def test_del_all_groups(app):
    """Check the possibility to delete all groups via home (contacts) page."""
    if app.group.count() == 0:
        [app.group.create(Group()) for _ in xrange(3)]
    app.group.delete_all_groups()
    actual_groups = app.group.get_list_of_groups()
    assert len(actual_groups) == app.group.count() == 0