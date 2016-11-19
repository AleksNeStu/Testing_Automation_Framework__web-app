#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Class for implement fixtures for conftest."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixtures.application import Application


fixture = None

@pytest.fixture
def app(request):
    """Init fixture with validation."""
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login_admin()
    else:
        if not fixture.check_fixture_valid():
            fixture = Application()
            fixture.session.login_admin()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    """Destroy fixture."""
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)