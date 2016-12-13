#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Class for implement fixtures for conftest."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from tests.fixtures.application import Application

fixture = None

@pytest.fixture()
def app(request):
    """Init fixture with validation."""
    global fixture
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseURL")
        fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login_as_admin()
    return fixture

@pytest.fixture(scope="function", autouse=True)
def stop(request):
    """Destroy fixture."""
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption(
        "--baseURL", action="store", default="http://localhost/addressbook/")