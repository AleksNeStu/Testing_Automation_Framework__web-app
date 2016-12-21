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
import jsonpickle
import subprocess

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
        config = load_json(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config["app_url"])
    fixture.session.ensure_login(config["ui_username"], config["ui_password"])
    return fixture


@pytest.fixture(scope="function", autouse=True)
def stop(request):
    """Destroy fixture."""
    global fixture
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def get_bash_output(command):
    """Run bash command with arguments and return its output as a string."""
    return subprocess.check_output(["bash", "-c", command]).strip("\n")


def pytest_addoption(parser):
    """Dynamically adding command line options."""
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


def load_and_call_used_getattr(full_path):
    """Load and call any module, class, method according full_path (elements
    have to separated by dot) used getattr method.
       Example:
       load_and_call("module.class.method")
    """
    components = full_path.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def load_json(full_path_to_file):
    """Load data from JSON file (load from JSON dicts items)."""
    with open(full_path_to_file) as json_f:
        return json.load(json_f)


def decode_json(full_path_to_file):
    """Deserialize data from JSON file (deserialize from JSON dicts items
    to objects attributes).
    """
    with open(full_path_to_file) as json_f:
        return jsonpickle.decode(json_f.read())


def pytest_generate_tests(metafunc):
    """"Injecting test data to the fixture.
    Custom dynamic parametrization scheme.
    """
    for fixture in metafunc.fixturenames:
        if fixture.startswith("generator_entities_"):
        # Encode objects attributes to JSON file
            fixturename_parts = fixture.split("_", 4)
            if len(fixturename_parts) == 5:
                _module = "generator.entities_factory"
                _cls = fixturename_parts[2]
                _method_generate = fixturename_parts[3]
                _method_create = fixturename_parts[4]
                _factory = _module + "." + _cls
                list_created_objs = load_and_call_used_getattr(
                    _factory + "." + _method_create)()
                test_data = [load_and_call_used_getattr(
                    _factory + "." + _method_generate)(list_created_objs)]
                metafunc.parametrize(fixture, test_data,
                                     ids=[str(x) for x in test_data])
        elif fixture.startswith("generator_templates_"):
        # Decode JSON file to objects attributes
            fixturename_parts = fixture.split("_")
            if len(fixturename_parts) == 3:
                _dir = fixturename_parts[0] + "/" + fixturename_parts[1]
                _file = fixturename_parts[2]
                _json_file = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "../{d}/{f}.json".format(d=_dir, f=_file))
                test_data = decode_json(full_path_to_file=_json_file)
                metafunc.parametrize(fixture, test_data,
                                     ids=[str(x) for x in test_data])