#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Groups test."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_modify_group_name(app):
    """Check the possibility of modifying group name."""
    app.group.modify_first_group(Group(name=r_data("new_Group_", 5)))


def test_modify_group_header(app):
    """Check the possibility of modifying group header."""
    app.group.modify_first_group(Group(header=r_data("new_Group_", 5)))