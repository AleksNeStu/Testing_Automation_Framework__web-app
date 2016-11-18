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
    """Check (validate) that app fixtures is exist."""
    global fixture
    try:
        fixture = Application()
        assert fixture != None and fixture.check_fixture_valid() == True
    except:
        request.addfinalizer(fixture.destroy)
        raise NameError("Error: {}".format("Fixture isn't available"))
    request.addfinalizer(fixture.destroy)
    return fixture