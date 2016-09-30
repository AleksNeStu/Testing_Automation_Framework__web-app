#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixtures.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(app.login_data)
    app.create_group(app.group_data)
    app.logout()


def test_add_group_empty(app):
    app.login(app.login_data)
    app.create_group(app.group_data_empty)
    app.logout()