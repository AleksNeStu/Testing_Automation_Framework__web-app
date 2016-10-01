#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Foobar.py: Description of what foobar does."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture