#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Groups test"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def test_del_first_group(app):
    """Check the possibility of del first group."""
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_del_all_groups(app):
    """Check the possibility of del all groups."""
    app.session.login(username="admin", password="secret")
    app.group.delete_all_groups()
    app.session.logout()