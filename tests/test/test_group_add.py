#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Groups test."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.generator.generic import random_data as r_data
from tests.model.group import Group


def test_add_group(app):
    """Check the possibility of add filling group."""
    app.session.login_admin()
    app.group.create(Group(name=r_data("Group_", 5), header=r_data("Header_", 5),
                           footer=r_data("Footer_", 5)))
    app.session.logout()


def test_add_group_empty(app):
    """Check the possibility of add empty group."""
    app.session.login_admin()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()