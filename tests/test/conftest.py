#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Foobar.py: Description of what foobar does."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixture.application import Application


fixture = None

@pytest.fixture()
def app(request):
    global fixture
    try:
        fixture = Application()
        assert fixture != None and fixture.check_fixture_valid() == True
    except:
        request.addfinalizer(fixture.destroy)
        raise NameError("Error: {}".format("Fixture isn't available"))
    request.addfinalizer(fixture.destroy)
    return fixture