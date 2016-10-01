#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()