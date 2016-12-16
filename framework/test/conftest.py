#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Pytest fixtures."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import json

import os.path
import pytest

from fixtures.application import Application

fixture = None
config = None

@pytest.fixture()
def app(request):
    """Init fixture with validation."""
    global fixture
    global config
    browser = request.config.getoption("--browser")
    if config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   request.config.getoption("--config"))
        with open(config_file) as f:
            config = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config["baseURL"])
    fixture.session.ensure_login(config["username"], config["password"])
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
    parser.addoption("--config", action="store", default="config.json")