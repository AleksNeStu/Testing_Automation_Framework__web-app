#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Check session"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def test_check_session(app):
    app.session.login(username="admin", password="secret")
    assert app.session.check_session() == True
    app.session.logout()