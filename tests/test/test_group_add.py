#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Groups test."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.constants import data
from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_add_group(app):
    """Check the possibility of add filling group."""
    old_groups = app.group.get_list_of_groups()
    group = Group(name=r_data(data.GROUP_NAME),
                  header=r_data(data.GROUP_HEADER),
                  footer=r_data(data.GROUP_FOOTER))
    app.group.create(group)
    new_groups = app.group.get_list_of_groups()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_group_empty(app):
    """Check the possibility of add empty group."""
    app.group.create(Group())