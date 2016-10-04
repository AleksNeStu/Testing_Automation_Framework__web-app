#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Check session"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email
from tests.model.contact import Contact


def test_check_session(app):
    app.session.login(username="admin", password="secret")
    assert app.session.check_session() == True
    app.session.logout()