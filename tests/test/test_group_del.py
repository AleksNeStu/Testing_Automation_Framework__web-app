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
    app.group.delete_first_group()


def test_del_all_groups(app):
    """Check the possibility of del all groups."""
    if app.group.count() == 0:
        [app.group.create(Group()) for _ in xrange(3)]
    app.group.delete_all_groups()