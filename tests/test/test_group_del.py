#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Groups test"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.model.group import Group


def test_del_first_group(app):
    """Check the possibility of del first group."""
    if app.group.count() == 0:
        app.group.create(Group())
    old_groups = app.group.get_list_of_groups()
    app.group.delete_first_group()
    new_groups = app.group.get_list_of_groups()
    assert len(old_groups) - 1 == len(new_groups)


def test_del_all_groups(app):
    """Check the possibility of del all groups."""
    old_groups = app.group.get_list_of_groups()
    if app.group.count() == 0:
        [app.group.create(Group()) for _ in xrange(3)]
    app.group.delete_all_groups()
    groups = app.group.get_list_of_groups()
    assert len(groups) == 0