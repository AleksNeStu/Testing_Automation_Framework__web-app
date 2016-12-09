#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for deletion groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import messages
from tests.model.group import Group


def test_del_first_group(app):
    """Check the possibility of del first group."""
    if app.group.count() == 0:
        app.group.create(Group())
    first_groups = app.group.get_list_of_groups()
    app.group.delete_first_group()
    actual_groups = app.group.get_list_of_groups()
    assert len(first_groups) - 1 == len(actual_groups)
    expected_groups = first_groups[1:]
    assert expected_groups == actual_groups, messages.ERR_MSG_FORMAT.format(
        expected_groups, actual_groups)

def test_del_all_groups(app):
    """Check the possibility of del all groups."""
    if app.group.count() == 0:
        [app.group.create(Group()) for _ in xrange(3)]
    app.group.delete_all_groups()
    actual_groups = app.group.get_list_of_groups()
    assert len(actual_groups) == 0