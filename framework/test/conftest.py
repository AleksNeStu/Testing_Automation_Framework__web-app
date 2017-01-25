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
from fixtures.db import DbFixture


app_fixture = None
config = None


@pytest.fixture()
def app(request):
    """Core fixture to initialization TAF."""
    global app_fixture
    web_config = load_config(request.config.getoption("--config"))["web"]
    browser = request.config.getoption("--browser")
    if app_fixture is None or not app_fixture.is_valid():
        app_fixture = Application(browser=browser,
                                  base_url=web_config["app_url"])
    app_fixture.session.ensure_login(web_config["ui_username"],
                                     web_config["ui_password"])
    return app_fixture


@pytest.fixture(scope="session")
def db(request):
    """Data base fixture."""
    db_config = load_config(request.config.getoption("--config"))["db"]
    db_server_ip = get_ip_of_docker_container(db_config["db_container"])
    DB_SERVER = db_config["db_server_ip"] if \
        db_server_ip == str(db_config["db_server_ip"]) else db_server_ip
    DB_NAME = db_config["db_name"]
    DB_USER = db_config["db_username"]
    DB_PASSWORD = db_config["db_password"]
    db_fixture = DbFixture(host=DB_SERVER, database=DB_NAME, user=DB_USER,
                           password=DB_PASSWORD)
    def fin():
        db_fixture.destroy()
    request.addfinalizer(fin)
    return db_fixture


def pytest_addoption(parser):
    """Dynamically adding command line options."""
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


def load_config(file):
    """Load a file with JSON format according to the it placement."""
    global config
    if config is None:
        config_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), file)
        config = load_json(config_file)
    return config


@pytest.fixture(scope="function", autouse=True)
def stop(request):
    """Destroy fixture."""
    global app_fixture
    def fin():
        if app_fixture is not None:
            app_fixture.session.ensure_logout()
            app_fixture.destroy()
    request.addfinalizer(fin)
    return app_fixture


def get_bash_output(command):
    """Run bash command with arguments and return its output as a string."""
    return subprocess.check_output(["bash", "-c", command]).strip("\n")


def get_ip_of_docker_container(container_name):
    """Get IP address of the container according to container_name.
    Return IP (str).
    """
    db_server_ip_cmd = "docker inspect -f '{{range .NetworkSettings.Networks}}" \
                       "{{.IPAddress}}{{end}}' " + container_name
    db_server_ip = get_bash_output(db_server_ip_cmd)
    return db_server_ip


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