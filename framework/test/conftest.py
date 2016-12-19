#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Pytest fixtures."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import json

import os.path
import pytest
from fixtures.application import Application
import generator.entities_factory


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
    """Dynamically adding command line options."""
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


def load_and_call(full_path):
    """Load and call any module, class, method according full_path (elements
    have to separated by dot).
       Example:
       load_and_call("module.class.method")
    """
    components = full_path.split('.')
    mod = __import__(components[0])
    print mod
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def pytest_generate_tests(metafunc):
    """"Dynamic test generation according fixture's name."""
    for fixture in metafunc.fixturenames:
        if fixture.startswith("generator_entities_"):
            fixturename_parts = fixture.split("_", 4)
            if len(fixturename_parts) == 5:
                _module = "generator.entities_factory"
                _cls = fixturename_parts[2]
                _method_generate = fixturename_parts[3]
                _method_create = fixturename_parts[4]
                _factory = _module + "." + _cls
                print _factory
                list_created_objs = load_and_call(
                    _factory + "." + _method_create)()
                test_data = load_and_call(
                    _factory + "." + _method_generate)(list_created_objs)
                metafunc.parametrize(
                    fixture, test_data, ids=[str(x) for x in test_data])